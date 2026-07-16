package desu.life;

import com.sun.jna.Library;
import com.sun.jna.Memory;
import com.sun.jna.Native;
import com.sun.jna.NativeLibrary;
import com.sun.jna.Pointer;
import com.sun.jna.Structure;
import com.sun.jna.Union;

import java.io.File;
import java.nio.ByteBuffer;
import java.nio.ByteOrder;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import java.util.OptionalDouble;
import java.util.OptionalInt;

/**
 * JNA bindings for the Interoptopus 0.16.3 ABI exposed by rosu_pp_ffi.
 *
 * <p>Interoptopus 0.16 does not publish a Java backend, so this file mirrors
 * the generated C# ABI. The API guard prevents loading an incompatible native
 * library.</p>
 */
@SuppressWarnings({"unused", "SpellCheckingInspection"})
public final class RosuFFI {
    private static final long API_GUARD = 0x697593acafdd88bbL;

    private RosuFFI() {}

    public enum Mode {
        Osu(0), Taiko(1), Catch(2), Mania(3);
        public final byte value;
        Mode(int value) { this.value = (byte) value; }
        public static Mode fromValue(byte value) {
            for (var mode : values()) if (mode.value == value) return mode;
            throw new IllegalArgumentException("Unknown mode: " + Byte.toUnsignedInt(value));
        }
    }

    public enum HitResultPriority {
        BestCase(0), WorstCase(1);
        public final byte value;
        HitResultPriority(int value) { this.value = (byte) value; }
    }

    public enum OsuScoreOrigin {
        Stable(0), WithSliderAcc(1), WithoutSliderAcc(2);
        public final byte value;
        OsuScoreOrigin(int value) { this.value = (byte) value; }
    }

    public enum TooSuspicious {
        Density(0), Length(1), ObjectCount(2), RedFlag(3), SliderPositions(4), SliderRepeats(5);
        public final byte value;
        TooSuspicious(int value) { this.value = (byte) value; }
        public static TooSuspicious fromValue(byte value) {
            for (var item : values()) if (item.value == value) return item;
            throw new IllegalArgumentException("Unknown suspicion: " + Byte.toUnsignedInt(value));
        }
    }

    public enum HitObjectKind { Circle, Slider, Spinner, Hold }

    public static final class FFIError {
        public static final int OK = 0;
        public static final int NULL = 100;
        public static final int PANIC = 200;
        public static final int IO_ERROR = 300;
        public static final int SERIALIZE_ERROR = 600;
        public static final int CONVERT_ERROR = 700;
        public static final int UNKNOWN = 1000;
        private FFIError() {}
    }

    public static final class FFIException extends RuntimeException {
        public final int code;
        public FFIException(String message, int code) {
            super(message + " (FFI error " + code + ")");
            this.code = code;
        }
    }

    public interface NativeApi extends Library {
        long __api_guard();

        long interoptopus_string_create(Pointer utf8, long len, Utf8String out);
        long interoptopus_string_destroy(Utf8String.ByValue value);
        void interoptopus_wire_destroy_78044(Pointer data, int len, int capacity);

        ServiceResult.ByValue beatmap_from_bytes(SliceU8.ByValue data);
        ServiceResult.ByValue beatmap_from_path(Utf8String.ByValue path);
        void beatmap_destroy(Pointer context);
        byte beatmap_convert(Pointer context, byte mode, Pointer mods);
        double beatmap_bpm(Pointer context);
        double beatmap_total_break_time(Pointer context);
        int beatmap_version(Pointer context);
        byte beatmap_is_convert(Pointer context);
        float beatmap_stack_leniency(Pointer context);
        byte beatmap_mode(Pointer context);
        float beatmap_ar(Pointer context);
        float beatmap_cs(Pointer context);
        float beatmap_hp(Pointer context);
        float beatmap_od(Pointer context);
        double beatmap_slider_multiplier(Pointer context);
        double beatmap_slider_tick_rate(Pointer context);
        OptionTooSuspicious.ByValue beatmap_check_suspicious(Pointer context);
        WireHitObjects.ByValue beatmap_hit_objects(Pointer context);

        ServiceResult.ByValue beatmap_attributes_builder_create();
        void beatmap_attributes_builder_destroy(Pointer context);
        void beatmap_attributes_builder_mode(Pointer context, byte mode);
        void beatmap_attributes_builder_p_mods(Pointer context, Pointer mods);
        void beatmap_attributes_builder_i_mods(Pointer context, int mods);
        void beatmap_attributes_builder_s_mods(Pointer context, Utf8String.ByValue mods);
        void beatmap_attributes_builder_clock_rate(Pointer context, double value);
        void beatmap_attributes_builder_ar(Pointer context, float value);
        void beatmap_attributes_builder_cs(Pointer context, float value);
        void beatmap_attributes_builder_hp(Pointer context, float value);
        void beatmap_attributes_builder_od(Pointer context, float value);
        double beatmap_attributes_builder_get_clock_rate(Pointer context);
        BeatmapAttributes.ByValue beatmap_attributes_builder_build(Pointer context, Pointer beatmap);

        ServiceResult.ByValue difficulty_create();
        void difficulty_destroy(Pointer context);
        void difficulty_p_mods(Pointer context, Pointer mods);
        void difficulty_i_mods(Pointer context, int mods);
        void difficulty_s_mods(Pointer context, Utf8String.ByValue mods);
        void difficulty_passed_objects(Pointer context, int value);
        void difficulty_clock_rate(Pointer context, double value);
        void difficulty_ar(Pointer context, float value);
        void difficulty_cs(Pointer context, float value);
        void difficulty_hp(Pointer context, float value);
        void difficulty_od(Pointer context, float value);
        void difficulty_hardrock_offsets(Pointer context, byte value);
        void difficulty_lazer(Pointer context, byte value);
        DifficultyAttributes.ByValue difficulty_calculate(Pointer context, Pointer beatmap);
        double difficulty_get_clock_rate(Pointer context);

        ServiceResult.ByValue performance_create();
        void performance_destroy(Pointer context);
        void performance_mode(Pointer context, byte mode);
        void performance_p_mods(Pointer context, Pointer mods);
        void performance_i_mods(Pointer context, int mods);
        void performance_s_mods(Pointer context, Utf8String.ByValue mods);
        void performance_passed_objects(Pointer context, int value);
        void performance_legacy_total_score(Pointer context, int value);
        void performance_clock_rate(Pointer context, double value);
        void performance_ar(Pointer context, float value);
        void performance_cs(Pointer context, float value);
        void performance_hp(Pointer context, float value);
        void performance_od(Pointer context, float value);
        void performance_hardrock_offsets(Pointer context, byte value);
        void performance_state(Pointer context, ScoreState.ByValue value);
        void performance_accuracy(Pointer context, double value);
        void performance_misses(Pointer context, int value);
        void performance_combo(Pointer context, int value);
        void performance_hitresult_priority(Pointer context, byte value);
        void performance_lazer(Pointer context, byte value);
        void performance_large_tick_hits(Pointer context, int value);
        void performance_small_tick_hits(Pointer context, int value);
        void performance_slider_end_hits(Pointer context, int value);
        void performance_n300(Pointer context, int value);
        void performance_n100(Pointer context, int value);
        void performance_n50(Pointer context, int value);
        void performance_n_katu(Pointer context, int value);
        void performance_n_geki(Pointer context, int value);
        ScoreState.ByValue performance_generate_state(Pointer context, Pointer beatmap);
        ScoreState.ByValue performance_generate_state_from_difficulty(Pointer context, DifficultyAttributes.ByValue attrs);
        PerformanceAttributes.ByValue performance_calculate(Pointer context, Pointer beatmap);
        PerformanceAttributes.ByValue performance_calculate_from_difficulty(Pointer context, DifficultyAttributes.ByValue attrs);
        double performance_get_clock_rate(Pointer context);

        ServiceResult.ByValue mods_create(byte mode);
        ServiceResult.ByValue mods_from_acronyms(Utf8String.ByValue value, byte mode);
        ServiceResult.ByValue mods_from_bits(int value, byte mode);
        ServiceResult.ByValue mods_from_json(Utf8String.ByValue value, byte mode, byte denyUnknown);
        void mods_destroy(Pointer context);
        void mods_remove_unknown_mods(Pointer context);
        void mods_sanitize(Pointer context);
        int mods_bits(Pointer context);
        int mods_len(Pointer context);
        Utf8String.ByValue mods_json(Pointer context);
        byte mods_insert_json(Pointer context, Utf8String.ByValue value, byte denyUnknown);
        void mods_insert(Pointer context, Utf8String.ByValue value);
        byte mods_contains(Pointer context, Utf8String.ByValue value);
        void mods_clear(Pointer context);
        OptionDouble.ByValue mods_clock_rate(Pointer context);

        ServiceResult.ByValue gradual_difficulty_create(Pointer difficulty, Pointer beatmap);
        ServiceResult.ByValue gradual_difficulty_new_with_mode(Pointer difficulty, Pointer beatmap, byte mode);
        void gradual_difficulty_destroy(Pointer context);
        OptionDifficultyAttributes.ByValue gradual_difficulty_next(Pointer context);
        OptionDifficultyAttributes.ByValue gradual_difficulty_nth(Pointer context, int n);
        int gradual_difficulty_len(Pointer context);

        ServiceResult.ByValue gradual_performance_create(Pointer difficulty, Pointer beatmap);
        ServiceResult.ByValue gradual_performance_new_with_mode(Pointer difficulty, Pointer beatmap, byte mode);
        void gradual_performance_destroy(Pointer context);
        OptionPerformanceAttributes.ByValue gradual_performance_next(Pointer context, ScoreState.ByValue state);
        OptionPerformanceAttributes.ByValue gradual_performance_last(Pointer context, ScoreState.ByValue state);
        OptionPerformanceAttributes.ByValue gradual_performance_nth(Pointer context, ScoreState.ByValue state, int n);
        int gradual_performance_len(Pointer context);

        Utf8String.ByValue debug_difficulty_attributes(DifficultyAttributes attrs);
        Utf8String.ByValue debug_performance_attributes(PerformanceAttributes attrs);
        Utf8String.ByValue debug_score_state(ScoreState state);
        double calculate_accuacy(ScoreState state, DifficultyAttributes attrs, byte origin);
    }

    private static final NativeApi NATIVE = loadNative();

    private static NativeApi loadNative() {
        String configured = System.getProperty("rosu.pp.ffi.library");
        NativeApi api;

        if (configured != null && !configured.isBlank()) {
            api = Native.load(new File(configured).getAbsolutePath(), NativeApi.class);
        } else {
            String mapped = NativeLibrary.getInstance("rosu_pp_ffi").getFile().getAbsolutePath();
            api = Native.load(mapped, NativeApi.class);
        }

        long actual = api.__api_guard();
        if (actual != API_GUARD) {
            throw new UnsatisfiedLinkError(
                "rosu_pp_ffi ABI mismatch: native=0x" + Long.toHexString(actual)
                    + ", Java=0x" + Long.toHexString(API_GUARD)
            );
        }

        return api;
    }

    private static byte bool(boolean value) { return (byte) (value ? 1 : 0); }

    @Structure.FieldOrder({"variant", "payload"})
    public static class ServiceResult extends Structure {
        public int variant;
        public Payload payload;
        public static class Payload extends Union {
            public Pointer ok;
            public short error;
        }
        public static class ByValue extends ServiceResult implements Structure.ByValue {}
        @Override public void read() {
            super.read();
            payload.setType(variant == 0 ? Pointer.class : short.class);
            payload.read();
        }
        Pointer unwrap(String operation) {
            if (variant == 0 && payload.ok != null) return payload.ok;
            int code = variant == 1 ? Short.toUnsignedInt(payload.error)
                : variant == 2 ? FFIError.PANIC : FFIError.NULL;
            throw new FFIException(operation, code);
        }
    }

    @Structure.FieldOrder({"ptr", "len", "capacity"})
    public static class Utf8String extends Structure {
        public Pointer ptr;
        public long len;
        public long capacity;
        public static class ByValue extends Utf8String implements Structure.ByValue {}

        static ByValue fromJava(String value) {
            byte[] bytes = value.getBytes(StandardCharsets.UTF_8);
            Memory memory = bytes.length == 0 ? null : new Memory(bytes.length);
            if (memory != null) memory.write(0, bytes, 0, bytes.length);
            Utf8String out = new Utf8String();
            NATIVE.interoptopus_string_create(memory, bytes.length, out);
            out.read();
            ByValue result = new ByValue();
            result.ptr = out.ptr;
            result.len = out.len;
            result.capacity = out.capacity;
            result.write();
            return result;
        }

        String consume() {
            String value = len == 0 ? "" : new String(ptr.getByteArray(0, Math.toIntExact(len)), StandardCharsets.UTF_8);
            ByValue owned = new ByValue();
            owned.ptr = ptr;
            owned.len = len;
            owned.capacity = capacity;
            owned.write();
            NATIVE.interoptopus_string_destroy(owned);
            ptr = null;
            len = 0;
            capacity = 0;
            return value;
        }
    }

    @Structure.FieldOrder({"data", "len"})
    public static class SliceU8 extends Structure {
        public Pointer data;
        public long len;
        protected Memory owner;
        public static class ByValue extends SliceU8 implements Structure.ByValue {}
        static ByValue from(byte[] bytes) {
            ByValue value = new ByValue();
            value.owner = bytes.length == 0 ? null : new Memory(bytes.length);
            if (value.owner != null) value.owner.write(0, bytes, 0, bytes.length);
            value.data = value.owner;
            value.len = bytes.length;
            value.write();
            return value;
        }
    }

    @Structure.FieldOrder({"variant", "some"})
    public static class OptionDouble extends Structure {
        public int variant;
        public double some;
        public static class ByValue extends OptionDouble implements Structure.ByValue {}
        public OptionalDouble toOptional() {
            return variant == 0 ? OptionalDouble.of(some) : OptionalDouble.empty();
        }
    }

    @Structure.FieldOrder({"variant", "some"})
    public static class OptionUint extends Structure {
        public int variant;
        public int some;
        public static class ByValue extends OptionUint implements Structure.ByValue {}
        public OptionalInt toOptional() {
            return variant == 0 ? OptionalInt.of(some) : OptionalInt.empty();
        }
    }

    @Structure.FieldOrder({"variant", "some"})
    public static class OptionTooSuspicious extends Structure {
        public int variant;
        public byte some;
        public static class ByValue extends OptionTooSuspicious implements Structure.ByValue {}
        public Optional<TooSuspicious> toOptional() {
            return variant == 0 ? Optional.of(TooSuspicious.fromValue(some)) : Optional.empty();
        }
    }

    @Structure.FieldOrder({"aim", "aim_difficult_slider_count", "speed", "flashlight", "reading",
        "slider_factor", "aim_top_weighted_slider_factor", "speed_top_weighted_slider_factor",
        "speed_note_count", "aim_difficult_strain_count", "speed_difficult_strain_count",
        "reading_difficult_note_count", "nested_score_per_object", "legacy_score_base_multiplier",
        "maximum_legacy_combo_score", "ar", "great_hit_window", "ok_hit_window", "meh_hit_window",
        "hp", "n_circles", "n_sliders", "n_large_ticks", "n_spinners", "stars", "max_combo"})
    public static class OsuDifficultyAttributes extends Structure {
        public double aim, aim_difficult_slider_count, speed, flashlight, reading, slider_factor;
        public double aim_top_weighted_slider_factor, speed_top_weighted_slider_factor, speed_note_count;
        public double aim_difficult_strain_count, speed_difficult_strain_count, reading_difficult_note_count;
        public double nested_score_per_object, legacy_score_base_multiplier, maximum_legacy_combo_score;
        public double ar, great_hit_window, ok_hit_window, meh_hit_window, hp;
        public int n_circles, n_sliders, n_large_ticks, n_spinners;
        public double stars;
        public int max_combo;
    }

    @Structure.FieldOrder({"stamina", "rhythm", "color", "reading", "great_hit_window", "ok_hit_window",
        "mono_stamina_factor", "mechanical_difficulty", "consistency_factor", "stars", "max_combo", "is_convert"})
    public static class TaikoDifficultyAttributes extends Structure {
        public double stamina, rhythm, color, reading, great_hit_window, ok_hit_window;
        public double mono_stamina_factor, mechanical_difficulty, consistency_factor, stars;
        public int max_combo;
        public byte is_convert;
    }

    @Structure.FieldOrder({"stars", "preempt", "n_fruits", "n_droplets", "n_tiny_droplets", "is_convert"})
    public static class CatchDifficultyAttributes extends Structure {
        public double stars, preempt;
        public int n_fruits, n_droplets, n_tiny_droplets;
        public byte is_convert;
    }

    @Structure.FieldOrder({"stars", "n_objects", "n_hold_notes", "max_combo", "is_convert"})
    public static class ManiaDifficultyAttributes extends Structure {
        public double stars;
        public int n_objects, n_hold_notes, max_combo;
        public byte is_convert;
    }

    public static class DifficultyPayload extends Union {
        public OsuDifficultyAttributes osu;
        public TaikoDifficultyAttributes taiko;
        public CatchDifficultyAttributes catchValue;
        public ManiaDifficultyAttributes mania;
    }

    @Structure.FieldOrder({"variant", "payload"})
    public static class DifficultyAttributes extends Structure {
        public byte variant;
        public DifficultyPayload payload;
        public DifficultyAttributes() {}
        protected DifficultyAttributes(Pointer memory) { super(memory); }
        public static class ByValue extends DifficultyAttributes implements Structure.ByValue {
            public ByValue() {}
            private ByValue(Pointer memory) { super(memory); }
        }
        @Override public void read() {
            super.read();
            payload.setType(switch (variant) {
                case 0 -> OsuDifficultyAttributes.class;
                case 1 -> TaikoDifficultyAttributes.class;
                case 2 -> CatchDifficultyAttributes.class;
                case 3 -> ManiaDifficultyAttributes.class;
                default -> throw new IllegalStateException("Invalid difficulty variant " + variant);
            });
            payload.read();
        }
        public Mode mode() { return Mode.fromValue(variant); }
        public OsuDifficultyAttributes asOsu() { require(Mode.Osu); return payload.osu; }
        public TaikoDifficultyAttributes asTaiko() { require(Mode.Taiko); return payload.taiko; }
        public CatchDifficultyAttributes asCatch() { require(Mode.Catch); return payload.catchValue; }
        public ManiaDifficultyAttributes asMania() { require(Mode.Mania); return payload.mania; }
        private void require(Mode mode) {
            if (variant != mode.value) throw new IllegalStateException("Expected " + mode + ", got " + mode());
        }
    }

    @Structure.FieldOrder({"difficulty", "pp", "pp_acc", "pp_aim", "pp_flashlight", "pp_reading",
        "pp_speed", "effective_miss_count", "speed_deviation", "combo_based_estimated_miss_count",
        "score_based_estimated_miss_count", "aim_estimated_slider_breaks", "speed_estimated_slider_breaks"})
    public static class OsuPerformanceAttributes extends Structure {
        public OsuDifficultyAttributes difficulty;
        public double pp, pp_acc, pp_aim, pp_flashlight, pp_reading, pp_speed, effective_miss_count;
        public OptionDouble speed_deviation;
        public double combo_based_estimated_miss_count;
        public OptionDouble score_based_estimated_miss_count;
        public double aim_estimated_slider_breaks, speed_estimated_slider_breaks;
    }

    @Structure.FieldOrder({"difficulty", "pp", "pp_acc", "pp_difficulty", "estimated_unstable_rate"})
    public static class TaikoPerformanceAttributes extends Structure {
        public TaikoDifficultyAttributes difficulty;
        public double pp, pp_acc, pp_difficulty;
        public OptionDouble estimated_unstable_rate;
    }

    @Structure.FieldOrder({"difficulty", "pp"})
    public static class CatchPerformanceAttributes extends Structure {
        public CatchDifficultyAttributes difficulty;
        public double pp;
    }

    @Structure.FieldOrder({"difficulty", "pp", "pp_difficulty"})
    public static class ManiaPerformanceAttributes extends Structure {
        public ManiaDifficultyAttributes difficulty;
        public double pp, pp_difficulty;
    }

    public static class PerformancePayload extends Union {
        public OsuPerformanceAttributes osu;
        public TaikoPerformanceAttributes taiko;
        public CatchPerformanceAttributes catchValue;
        public ManiaPerformanceAttributes mania;
    }

    @Structure.FieldOrder({"variant", "payload"})
    public static class PerformanceAttributes extends Structure {
        public byte variant;
        public PerformancePayload payload;
        public static class ByValue extends PerformanceAttributes implements Structure.ByValue {}
        @Override public void read() {
            super.read();
            payload.setType(switch (variant) {
                case 0 -> OsuPerformanceAttributes.class;
                case 1 -> TaikoPerformanceAttributes.class;
                case 2 -> CatchPerformanceAttributes.class;
                case 3 -> ManiaPerformanceAttributes.class;
                default -> throw new IllegalStateException("Invalid performance variant " + variant);
            });
            payload.read();
        }
        public Mode mode() { return Mode.fromValue(variant); }
        public OsuPerformanceAttributes asOsu() { require(Mode.Osu); return payload.osu; }
        public TaikoPerformanceAttributes asTaiko() { require(Mode.Taiko); return payload.taiko; }
        public CatchPerformanceAttributes asCatch() { require(Mode.Catch); return payload.catchValue; }
        public ManiaPerformanceAttributes asMania() { require(Mode.Mania); return payload.mania; }
        private void require(Mode mode) {
            if (variant != mode.value) throw new IllegalStateException("Expected " + mode + ", got " + mode());
        }
    }

    @Structure.FieldOrder({"variant", "some"})
    public static class OptionDifficultyAttributes extends Structure {
        public int variant;
        public DifficultyAttributes some;
        public static class ByValue extends OptionDifficultyAttributes implements Structure.ByValue {}
        public Optional<DifficultyAttributes> toOptional() {
            if (variant != 0) return Optional.empty();
            some.read();
            return Optional.of(some);
        }
    }

    @Structure.FieldOrder({"variant", "some"})
    public static class OptionPerformanceAttributes extends Structure {
        public int variant;
        public PerformanceAttributes some;
        public static class ByValue extends OptionPerformanceAttributes implements Structure.ByValue {}
        public Optional<PerformanceAttributes> toOptional() {
            if (variant != 0) return Optional.empty();
            some.read();
            return Optional.of(some);
        }
    }

    @Structure.FieldOrder({"max_combo", "osu_large_tick_hits", "osu_small_tick_hits", "slider_end_hits",
        "n_geki", "n_katu", "n300", "n100", "n50", "misses", "legacy_total_score"})
    public static class ScoreState extends Structure {
        public int max_combo, osu_large_tick_hits, osu_small_tick_hits, slider_end_hits;
        public int n_geki, n_katu, n300, n100, n50, misses;
        public OptionUint legacy_total_score;
        public static class ByValue extends ScoreState implements Structure.ByValue {}
        ByValue byValue() {
            write();
            ByValue value = new ByValue();
            value.useMemory(getPointer());
            value.read();
            return value;
        }
    }

    @Structure.FieldOrder({"ar", "od_perfect", "od_great", "od_good", "od_ok", "od_meh"})
    public static class HitWindows extends Structure {
        public OptionDouble ar, od_perfect, od_great, od_good, od_ok, od_meh;
    }

    @Structure.FieldOrder({"ar", "od", "cs", "hp", "clock_rate", "hit_windows"})
    public static class BeatmapAttributes extends Structure {
        public double ar, od;
        public float cs, hp;
        public double clock_rate;
        public HitWindows hit_windows;
        public static class ByValue extends BeatmapAttributes implements Structure.ByValue {}
    }

    public record SliderData(long repeats, OptionalDouble expectedDistance) {}
    public record HitObject(float x, float y, double startTime, HitObjectKind kind,
                            SliderData slider, double duration) {}

    @Structure.FieldOrder({"data", "len", "capacity"})
    public static class WireHitObjects extends Structure implements AutoCloseable {
        public Pointer data;
        public int len;
        public int capacity;
        public static class ByValue extends WireHitObjects implements Structure.ByValue {}

        public List<HitObject> unwire() {
            if (data == null || len == 0) return List.of();
            ByteBuffer buffer = data.getByteBuffer(0, len).order(ByteOrder.LITTLE_ENDIAN);
            int count = buffer.getInt();
            List<HitObject> result = new ArrayList<>(count);
            for (int i = 0; i < count; i++) {
                float x = buffer.getFloat();
                float y = buffer.getFloat();
                double start = buffer.getDouble();
                int tag = Byte.toUnsignedInt(buffer.get());
                HitObjectKind kind = HitObjectKind.values()[tag];
                SliderData slider = null;
                double duration = 0;
                if (kind == HitObjectKind.Slider) {
                    long repeats = Integer.toUnsignedLong(buffer.getInt());
                    int option = Byte.toUnsignedInt(buffer.get());
                    OptionalDouble distance = option == 0
                        ? OptionalDouble.of(buffer.getDouble()) : OptionalDouble.empty();
                    slider = new SliderData(repeats, distance);
                } else if (kind == HitObjectKind.Spinner || kind == HitObjectKind.Hold) {
                    duration = buffer.getDouble();
                }
                result.add(new HitObject(x, y, start, kind, slider, duration));
            }
            return result;
        }

        @Override public void close() {
            if (data != null) {
                NATIVE.interoptopus_wire_destroy_78044(data, len, capacity);
                data = null;
                len = 0;
                capacity = 0;
            }
        }
    }

    private abstract static class Service implements AutoCloseable {
        private Pointer context;
        Service(Pointer context) { this.context = context; }
        final Pointer context() {
            if (context == null) throw new IllegalStateException("Service already closed");
            return context;
        }
        abstract void destroy(Pointer context);
        @Override public final void close() {
            if (context != null) {
                destroy(context);
                context = null;
            }
        }
    }

    public static final class Beatmap extends Service {
        public Beatmap(byte[] data) {
            super(NATIVE.beatmap_from_bytes(SliceU8.from(data)).unwrap("beatmap_from_bytes"));
        }
        public Beatmap(String path) {
            super(NATIVE.beatmap_from_path(Utf8String.fromJava(path)).unwrap("beatmap_from_path"));
        }
        @Override void destroy(Pointer context) { NATIVE.beatmap_destroy(context); }
        public boolean convert(Mode mode, Mods mods) { return NATIVE.beatmap_convert(context(), mode.value, mods.context()) != 0; }
        public boolean convert(Mode mode) {
            try (var mods = Mods.create(mode)) { return convert(mode, mods); }
        }
        public double bpm() { return NATIVE.beatmap_bpm(context()); }
        public double totalBreakTime() { return NATIVE.beatmap_total_break_time(context()); }
        public int version() { return NATIVE.beatmap_version(context()); }
        public boolean isConvert() { return NATIVE.beatmap_is_convert(context()) != 0; }
        public float stackLeniency() { return NATIVE.beatmap_stack_leniency(context()); }
        public Mode mode() { return Mode.fromValue(NATIVE.beatmap_mode(context())); }
        public float ar() { return NATIVE.beatmap_ar(context()); }
        public float cs() { return NATIVE.beatmap_cs(context()); }
        public float hp() { return NATIVE.beatmap_hp(context()); }
        public float od() { return NATIVE.beatmap_od(context()); }
        public double sliderMultiplier() { return NATIVE.beatmap_slider_multiplier(context()); }
        public double sliderTickRate() { return NATIVE.beatmap_slider_tick_rate(context()); }
        public Optional<TooSuspicious> checkSuspicious() { return NATIVE.beatmap_check_suspicious(context()).toOptional(); }
        public WireHitObjects.ByValue hitObjects() { return NATIVE.beatmap_hit_objects(context()); }
    }

    public static final class Mods extends Service {
        private Mods(Pointer context) { super(context); }
        public static Mods create(Mode mode) { return new Mods(NATIVE.mods_create(mode.value).unwrap("mods_create")); }
        public static Mods fromAcronyms(String value, Mode mode) {
            return new Mods(NATIVE.mods_from_acronyms(Utf8String.fromJava(value), mode.value).unwrap("mods_from_acronyms"));
        }
        public static Mods fromBits(long value, Mode mode) {
            return new Mods(NATIVE.mods_from_bits((int) value, mode.value).unwrap("mods_from_bits"));
        }
        public static Mods fromJson(String value, Mode mode, boolean denyUnknown) {
            return new Mods(NATIVE.mods_from_json(Utf8String.fromJava(value), mode.value, bool(denyUnknown)).unwrap("mods_from_json"));
        }
        @Override void destroy(Pointer context) { NATIVE.mods_destroy(context); }
        public void removeUnknownMods() { NATIVE.mods_remove_unknown_mods(context()); }
        public void sanitize() { NATIVE.mods_sanitize(context()); }
        public long bits() { return Integer.toUnsignedLong(NATIVE.mods_bits(context())); }
        public long length() { return Integer.toUnsignedLong(NATIVE.mods_len(context())); }
        public String json() { return NATIVE.mods_json(context()).consume(); }
        public boolean insertJson(String value, boolean denyUnknown) {
            return NATIVE.mods_insert_json(context(), Utf8String.fromJava(value), bool(denyUnknown)) != 0;
        }
        public void insert(String value) { NATIVE.mods_insert(context(), Utf8String.fromJava(value)); }
        public boolean contains(String value) { return NATIVE.mods_contains(context(), Utf8String.fromJava(value)) != 0; }
        public void clear() { NATIVE.mods_clear(context()); }
        public OptionalDouble clockRate() { return NATIVE.mods_clock_rate(context()).toOptional(); }
    }

    public static final class Difficulty extends Service {
        public Difficulty() { super(NATIVE.difficulty_create().unwrap("difficulty_create")); }
        @Override void destroy(Pointer context) { NATIVE.difficulty_destroy(context); }
        public void mods(Mods value) { NATIVE.difficulty_p_mods(context(), value.context()); }
        public void mods(long value) { NATIVE.difficulty_i_mods(context(), (int) value); }
        public void mods(String value) { NATIVE.difficulty_s_mods(context(), Utf8String.fromJava(value)); }
        public void passedObjects(long value) { NATIVE.difficulty_passed_objects(context(), (int) value); }
        public void clockRate(double value) { NATIVE.difficulty_clock_rate(context(), value); }
        public void ar(float value) { NATIVE.difficulty_ar(context(), value); }
        public void cs(float value) { NATIVE.difficulty_cs(context(), value); }
        public void hp(float value) { NATIVE.difficulty_hp(context(), value); }
        public void od(float value) { NATIVE.difficulty_od(context(), value); }
        public void hardrockOffsets(boolean value) { NATIVE.difficulty_hardrock_offsets(context(), bool(value)); }
        public void lazer(boolean value) { NATIVE.difficulty_lazer(context(), bool(value)); }
        public DifficultyAttributes calculate(Beatmap beatmap) { return NATIVE.difficulty_calculate(context(), beatmap.context()); }
        public double clockRate() { return NATIVE.difficulty_get_clock_rate(context()); }
    }

    public static final class Performance extends Service {
        public Performance() { super(NATIVE.performance_create().unwrap("performance_create")); }
        @Override void destroy(Pointer context) { NATIVE.performance_destroy(context); }
        public void mode(Mode value) { NATIVE.performance_mode(context(), value.value); }
        public void mods(Mods value) { NATIVE.performance_p_mods(context(), value.context()); }
        public void mods(long value) { NATIVE.performance_i_mods(context(), (int) value); }
        public void mods(String value) { NATIVE.performance_s_mods(context(), Utf8String.fromJava(value)); }
        public void passedObjects(long value) { NATIVE.performance_passed_objects(context(), (int) value); }
        public void legacyTotalScore(long value) { NATIVE.performance_legacy_total_score(context(), (int) value); }
        public void clockRate(double value) { NATIVE.performance_clock_rate(context(), value); }
        public void ar(float value) { NATIVE.performance_ar(context(), value); }
        public void cs(float value) { NATIVE.performance_cs(context(), value); }
        public void hp(float value) { NATIVE.performance_hp(context(), value); }
        public void od(float value) { NATIVE.performance_od(context(), value); }
        public void hardrockOffsets(boolean value) { NATIVE.performance_hardrock_offsets(context(), bool(value)); }
        public void state(ScoreState value) { NATIVE.performance_state(context(), value.byValue()); }
        public void accuracy(double value) { NATIVE.performance_accuracy(context(), value); }
        public void misses(long value) { NATIVE.performance_misses(context(), (int) value); }
        public void combo(long value) { NATIVE.performance_combo(context(), (int) value); }
        public void hitResultPriority(HitResultPriority value) { NATIVE.performance_hitresult_priority(context(), value.value); }
        public void lazer(boolean value) { NATIVE.performance_lazer(context(), bool(value)); }
        public void largeTickHits(long value) { NATIVE.performance_large_tick_hits(context(), (int) value); }
        public void smallTickHits(long value) { NATIVE.performance_small_tick_hits(context(), (int) value); }
        public void sliderEndHits(long value) { NATIVE.performance_slider_end_hits(context(), (int) value); }
        public void n300(long value) { NATIVE.performance_n300(context(), (int) value); }
        public void n100(long value) { NATIVE.performance_n100(context(), (int) value); }
        public void n50(long value) { NATIVE.performance_n50(context(), (int) value); }
        public void nKatu(long value) { NATIVE.performance_n_katu(context(), (int) value); }
        public void nGeki(long value) { NATIVE.performance_n_geki(context(), (int) value); }
        public ScoreState generateState(Beatmap beatmap) { return NATIVE.performance_generate_state(context(), beatmap.context()); }
        public ScoreState generateState(DifficultyAttributes attrs) {
            return NATIVE.performance_generate_state_from_difficulty(context(), asDifficultyValue(attrs));
        }
        public PerformanceAttributes calculate(Beatmap beatmap) { return NATIVE.performance_calculate(context(), beatmap.context()); }
        public PerformanceAttributes calculate(DifficultyAttributes attrs) {
            return NATIVE.performance_calculate_from_difficulty(context(), asDifficultyValue(attrs));
        }
        public double clockRate() { return NATIVE.performance_get_clock_rate(context()); }
    }

    public static final class BeatmapAttributesBuilder extends Service {
        public BeatmapAttributesBuilder() { super(NATIVE.beatmap_attributes_builder_create().unwrap("beatmap_attributes_builder_create")); }
        @Override void destroy(Pointer context) { NATIVE.beatmap_attributes_builder_destroy(context); }
        public void mode(Mode value) { NATIVE.beatmap_attributes_builder_mode(context(), value.value); }
        public void mods(Mods value) { NATIVE.beatmap_attributes_builder_p_mods(context(), value.context()); }
        public void mods(long value) { NATIVE.beatmap_attributes_builder_i_mods(context(), (int) value); }
        public void mods(String value) { NATIVE.beatmap_attributes_builder_s_mods(context(), Utf8String.fromJava(value)); }
        public void clockRate(double value) { NATIVE.beatmap_attributes_builder_clock_rate(context(), value); }
        public void ar(float value) { NATIVE.beatmap_attributes_builder_ar(context(), value); }
        public void cs(float value) { NATIVE.beatmap_attributes_builder_cs(context(), value); }
        public void hp(float value) { NATIVE.beatmap_attributes_builder_hp(context(), value); }
        public void od(float value) { NATIVE.beatmap_attributes_builder_od(context(), value); }
        public double clockRate() { return NATIVE.beatmap_attributes_builder_get_clock_rate(context()); }
        public BeatmapAttributes build(Beatmap beatmap) { return NATIVE.beatmap_attributes_builder_build(context(), beatmap.context()); }
    }

    public static final class GradualDifficulty extends Service {
        private GradualDifficulty(Pointer context) { super(context); }
        public static GradualDifficulty create(Difficulty difficulty, Beatmap beatmap) {
            return new GradualDifficulty(NATIVE.gradual_difficulty_create(difficulty.context(), beatmap.context()).unwrap("gradual_difficulty_create"));
        }
        public static GradualDifficulty create(Difficulty difficulty, Beatmap beatmap, Mode mode) {
            return new GradualDifficulty(NATIVE.gradual_difficulty_new_with_mode(difficulty.context(), beatmap.context(), mode.value).unwrap("gradual_difficulty_new_with_mode"));
        }
        @Override void destroy(Pointer context) { NATIVE.gradual_difficulty_destroy(context); }
        public Optional<DifficultyAttributes> next() { return NATIVE.gradual_difficulty_next(context()).toOptional(); }
        public Optional<DifficultyAttributes> nth(long n) { return NATIVE.gradual_difficulty_nth(context(), (int) n).toOptional(); }
        public long length() { return Integer.toUnsignedLong(NATIVE.gradual_difficulty_len(context())); }
    }

    public static final class GradualPerformance extends Service {
        private GradualPerformance(Pointer context) { super(context); }
        public static GradualPerformance create(Difficulty difficulty, Beatmap beatmap) {
            return new GradualPerformance(NATIVE.gradual_performance_create(difficulty.context(), beatmap.context()).unwrap("gradual_performance_create"));
        }
        public static GradualPerformance create(Difficulty difficulty, Beatmap beatmap, Mode mode) {
            return new GradualPerformance(NATIVE.gradual_performance_new_with_mode(difficulty.context(), beatmap.context(), mode.value).unwrap("gradual_performance_new_with_mode"));
        }
        @Override void destroy(Pointer context) { NATIVE.gradual_performance_destroy(context); }
        public Optional<PerformanceAttributes> next(ScoreState state) {
            return NATIVE.gradual_performance_next(context(), state.byValue()).toOptional();
        }
        public Optional<PerformanceAttributes> last(ScoreState state) {
            return NATIVE.gradual_performance_last(context(), state.byValue()).toOptional();
        }
        public Optional<PerformanceAttributes> nth(ScoreState state, long n) {
            return NATIVE.gradual_performance_nth(context(), state.byValue(), (int) n).toOptional();
        }
        public long length() { return Integer.toUnsignedLong(NATIVE.gradual_performance_len(context())); }
    }

    private static DifficultyAttributes.ByValue asDifficultyValue(DifficultyAttributes attrs) {
        attrs.write();
        DifficultyAttributes.ByValue value = new DifficultyAttributes.ByValue(attrs.getPointer());
        value.read();
        return value;
    }

    public static String debug(DifficultyAttributes value) {
        value.write();
        return NATIVE.debug_difficulty_attributes(value).consume();
    }

    public static String debug(PerformanceAttributes value) {
        value.write();
        return NATIVE.debug_performance_attributes(value).consume();
    }

    public static String debug(ScoreState value) {
        value.write();
        return NATIVE.debug_score_state(value).consume();
    }

    public static double calculateAccuracy(ScoreState state, DifficultyAttributes attrs, OsuScoreOrigin origin) {
        state.write();
        attrs.write();
        return NATIVE.calculate_accuacy(state, attrs, origin.value);
    }
}
