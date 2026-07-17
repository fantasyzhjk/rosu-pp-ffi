package desu.life;

import org.junit.jupiter.api.Test;

import java.io.IOException;
import java.lang.foreign.MemorySegment;
import java.lang.reflect.Modifier;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Arrays;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;

class RosuFFITest {
    private static final Path WORKSPACE = Path.of(System.getProperty("user.dir")).toAbsolutePath().getParent();
    private static final Path RESOURCES = WORKSPACE.resolve("SharpRosuPP/RosuPP.Tests/resources");

    static {
        String os = System.getProperty("os.name").toLowerCase();
        String library = os.contains("win")
            ? "rosu_pp_ffi.dll"
            : os.contains("mac") ? "librosu_pp_ffi.dylib" : "librosu_pp_ffi.so";
        System.setProperty(
            "rosu.pp.ffi.library",
            WORKSPACE.resolve("target/release").resolve(library).toString()
        );
    }

    @Test
    void calculatesPayloadEnumsForEveryMode() {
        var maps = List.of(
            new ModeMap("657916.osu", RosuFFI.Mode.Osu),
            new ModeMap("1028484.osu", RosuFFI.Mode.Taiko),
            new ModeMap("2118524.osu", RosuFFI.Mode.Catch),
            new ModeMap("1638954.osu", RosuFFI.Mode.Mania)
        );

        for (var test : maps) {
            try (
                var beatmap = new RosuFFI.Beatmap(RESOURCES.resolve(test.file()).toString());
                var difficulty = new RosuFFI.Difficulty();
                var performance = new RosuFFI.Performance()
            ) {
                var difficultyAttributes = difficulty.calculate(beatmap);
                var performanceAttributes = performance.calculate(beatmap);

                assertEquals(test.mode(), beatmap.mode());
                assertEquals(test.mode(), difficultyAttributes.mode());
                assertEquals(test.mode(), performanceAttributes.mode());
            }
        }
    }

    @Test
    void transfersHitObjectsThroughWire() {
        try (var beatmap = new RosuFFI.Beatmap(RESOURCES.resolve("657916.osu").toString())) {
            try (var wire = beatmap.hitObjects()) {
                var hitObjects = wire.unwire();

                assertEquals(1368, hitObjects.size());
                assertEquals(RosuFFI.HitObjectKind.Slider, hitObjects.get(0).kind());
                assertTrue(hitObjects.stream().anyMatch(hitObject -> hitObject.kind() == RosuFFI.HitObjectKind.Slider));
            }
        }
    }

    @Test
    void ownsUtf8InputsAndOutputs() throws IOException {
        Path directory = Files.createTempDirectory("rosu-java-路径-");
        Path unicodePath = Files.copy(RESOURCES.resolve("657916.osu"), directory.resolve("谱面.osu"));

        try (
            var beatmap = new RosuFFI.Beatmap(unicodePath.toString());
            var difficulty = new RosuFFI.Difficulty();
            var mods = RosuFFI.Mods.fromAcronyms("HDDT", RosuFFI.Mode.Osu)
        ) {
            var attributes = difficulty.calculate(beatmap);

            assertEquals(RosuFFI.Mode.Osu, beatmap.mode());
            assertTrue(mods.json().contains("\"DT\""));
            assertEquals(1.5, mods.clockRate().orElseThrow());
            assertFalse(RosuFFI.debug(attributes).isBlank());
        }
    }

    @Test
    void supportsGradualServiceLifecycle() {
        try (
            var beatmap = new RosuFFI.Beatmap(RESOURCES.resolve("657916.osu").toString());
            var difficulty = new RosuFFI.Difficulty();
            var gradual = RosuFFI.GradualDifficulty.create(difficulty, beatmap)
        ) {
            assertEquals(1368, gradual.length());
            assertEquals(RosuFFI.Mode.Osu, gradual.next().orElseThrow().mode());
        }
    }

    @Test
    void passesPayloadEnumsBackIntoNativeFunctions() throws IOException {
        byte[] bytes = Files.readAllBytes(RESOURCES.resolve("657916.osu"));

        try (
            var beatmap = new RosuFFI.Beatmap(bytes);
            var difficulty = new RosuFFI.Difficulty();
            var performance = new RosuFFI.Performance();
            var builder = new RosuFFI.BeatmapAttributesBuilder()
        ) {
            var difficultyAttributes = difficulty.calculate(beatmap);
            var performanceAttributes = performance.calculate(difficultyAttributes);
            var state = performance.generateState(difficultyAttributes);
            var beatmapAttributes = builder.build(beatmap);

            assertEquals(RosuFFI.Mode.Osu, performanceAttributes.mode());
            assertTrue(performanceAttributes.asOsu().pp > 0);
            assertEquals(1368, state.n300);
            assertEquals(1.0, RosuFFI.calculateAccuracy(
                state,
                difficultyAttributes,
                RosuFFI.OsuScoreOrigin.Stable
            ));
            assertTrue(beatmapAttributes.ar > 0);
            assertFalse(RosuFFI.debug(performanceAttributes).isBlank());
            assertFalse(RosuFFI.debug(state).isBlank());
        }
    }

    @Test
    void synchronizesMutableFacadePayloadsBackToNative() {
        try (
            var beatmap = new RosuFFI.Beatmap(RESOURCES.resolve("657916.osu").toString());
            var difficulty = new RosuFFI.Difficulty();
            var performance = new RosuFFI.Performance()
        ) {
            var difficultyAttributes = difficulty.calculate(beatmap);
            difficultyAttributes.asOsu().stars = 12345.678;
            assertTrue(RosuFFI.debug(difficultyAttributes).contains("12345.678"));

            var performanceAttributes = performance.calculate(beatmap);
            performanceAttributes.asOsu().pp = 87654.321;
            performanceAttributes.asOsu().difficulty.stars = 23456.789;
            String debug = RosuFFI.debug(performanceAttributes);
            assertTrue(debug.contains("87654.321"));
            assertTrue(debug.contains("23456.789"));
        }
    }

    @Test
    void rejectsOutOfRangeUnsignedArguments() {
        try (var difficulty = new RosuFFI.Difficulty()) {
            assertThrows(IllegalArgumentException.class, () -> difficulty.passedObjects(-1));
            assertThrows(IllegalArgumentException.class, () -> difficulty.passedObjects(0x1_0000_0000L));
        }
    }

    @Test
    void rejectsReadingAClosedWire() {
        try (var beatmap = new RosuFFI.Beatmap(RESOURCES.resolve("657916.osu").toString())) {
            var wire = beatmap.hitObjects();
            wire.close();
            assertThrows(IllegalStateException.class, wire::unwire);
        }
    }

    @Test
    void representsOptionalUintWithoutLosingUnsignedValues() {
        var value = new RosuFFI.OptionUint();
        value.set(4_000_000_000L);
        assertEquals(4_000_000_000L, value.toOptional().orElseThrow());

        value.clear();
        assertTrue(value.toOptional().isEmpty());
        assertThrows(IllegalArgumentException.class, () -> value.set(0x1_0000_0000L));
    }

    @Test
    void exposesEveryModsInputForm() throws NoSuchMethodException {
        for (Class<?> service : List.of(
            RosuFFI.Difficulty.class,
            RosuFFI.Performance.class,
            RosuFFI.BeatmapAttributesBuilder.class
        )) {
            service.getMethod("mods", RosuFFI.Mods.class);
            service.getMethod("mods", long.class);
            service.getMethod("mods", String.class);
        }
    }

    @Test
    void facadeAttributeSchemasMatchGeneratedRawSchemasBothWays() {
        assertSchema(RosuFFI.OsuDifficultyAttributes.class, desu.life.raw.OsuDifficultyAttributes.class);
        assertSchema(RosuFFI.TaikoDifficultyAttributes.class, desu.life.raw.TaikoDifficultyAttributes.class);
        assertSchema(RosuFFI.CatchDifficultyAttributes.class, desu.life.raw.CatchDifficultyAttributes.class);
        assertSchema(RosuFFI.ManiaDifficultyAttributes.class, desu.life.raw.ManiaDifficultyAttributes.class);
        assertSchema(RosuFFI.OsuPerformanceAttributes.class, desu.life.raw.OsuPerformanceAttributes.class);
        assertSchema(RosuFFI.TaikoPerformanceAttributes.class, desu.life.raw.TaikoPerformanceAttributes.class);
        assertSchema(RosuFFI.CatchPerformanceAttributes.class, desu.life.raw.CatchPerformanceAttributes.class);
        assertSchema(RosuFFI.ManiaPerformanceAttributes.class, desu.life.raw.ManiaPerformanceAttributes.class);
        assertSchema(RosuFFI.ScoreState.class, desu.life.raw.ScoreState.class);
        assertSchema(RosuFFI.HitWindows.class, desu.life.raw.HitWindows.class);
        assertSchema(RosuFFI.BeatmapAttributes.class, desu.life.raw.BeatmapAttributes.class);
    }

    private static void assertSchema(Class<?> facade, Class<?> raw) {
        Set<String> facadeFields = Arrays.stream(facade.getFields())
            .filter(field -> !Modifier.isStatic(field.getModifiers()))
            .map(field -> field.getName())
            .collect(Collectors.toSet());
        Set<String> rawFields = Arrays.stream(raw.getMethods())
            .filter(method -> Modifier.isStatic(method.getModifiers()))
            .filter(method -> method.getParameterCount() == 1)
            .filter(method -> method.getParameterTypes()[0] == MemorySegment.class)
            .filter(method -> method.getReturnType() != void.class)
            .map(method -> method.getName())
            .collect(Collectors.toSet());
        assertEquals(rawFields, facadeFields, facade.getSimpleName());
    }

    private record ModeMap(String file, RosuFFI.Mode mode) {}
}
