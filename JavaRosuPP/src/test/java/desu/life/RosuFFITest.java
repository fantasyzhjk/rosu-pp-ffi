package desu.life;

import org.junit.jupiter.api.Test;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
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

    private record ModeMap(String file, RosuFFI.Mode mode) {}
}
