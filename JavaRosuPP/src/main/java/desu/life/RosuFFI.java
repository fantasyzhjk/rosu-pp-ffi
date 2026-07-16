package desu.life;

import desu.life.raw.RosuNative;

import java.lang.foreign.Arena;
import java.lang.foreign.MemorySegment;
import java.lang.foreign.ValueLayout;
import java.lang.reflect.Field;
import java.lang.reflect.Method;
import java.lang.reflect.Modifier;
import java.nio.ByteBuffer;
import java.nio.ByteOrder;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import java.util.OptionalDouble;
import java.util.OptionalInt;

/** Java 22 FFM facade for the Interoptopus 0.16.3 ABI. */
@SuppressWarnings({"unused", "SpellCheckingInspection"})
public final class RosuFFI {
    private static final long API_GUARD = 0x697593acafdd88bbL;
    private static final Arena RESULTS = Arena.ofAuto();

    static {
        String configured = System.getProperty("rosu.pp.ffi.library");
        if (configured == null || configured.isBlank()) System.loadLibrary("rosu_pp_ffi");
        else System.load(java.nio.file.Path.of(configured).toAbsolutePath().toString());
        long actual = RosuNative.__api_guard();
        if (actual != API_GUARD) throw new UnsatisfiedLinkError(
            "rosu_pp_ffi ABI mismatch: native=0x" + Long.toHexString(actual)
                + ", Java=0x" + Long.toHexString(API_GUARD));
    }

    private RosuFFI() {}

    public enum Mode {
        Osu(0), Taiko(1), Catch(2), Mania(3);
        public final byte value;
        Mode(int value) { this.value = (byte) value; }
        static Mode fromValue(int value) {
            for (var x : values()) if (Byte.toUnsignedInt(x.value) == value) return x;
            throw new IllegalArgumentException("Unknown mode: " + value);
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
        static TooSuspicious fromValue(int value) {
            for (var x : values()) if (Byte.toUnsignedInt(x.value) == value) return x;
            throw new IllegalArgumentException("Unknown suspicion: " + value);
        }
    }
    public enum HitObjectKind { Circle, Slider, Spinner, Hold }

    public static final class FFIError {
        public static final int OK=0, NULL=100, PANIC=200, IO_ERROR=300;
        public static final int SERIALIZE_ERROR=600, CONVERT_ERROR=700, UNKNOWN=1000;
        private FFIError() {}
    }
    public static final class FFIException extends RuntimeException {
        public final int code;
        FFIException(String message, int code) { super(message + " (FFI error " + code + ")"); this.code = code; }
    }

    private static MemorySegment unwrap(MemorySegment result, String operation) {
        int variant = desu.life.raw.ResultPtrFFIError.variant(result);
        MemorySegment payload = desu.life.raw.ResultPtrFFIError.payload(result);
        if (variant == 0) {
            MemorySegment pointer = desu.life.raw.ResultPtrFFIError.payload.ok(payload);
            if (!pointer.equals(MemorySegment.NULL)) return pointer;
        }
        int code = variant == 1 ? desu.life.raw.ResultPtrFFIError.payload.err(payload)
            : variant == 2 ? FFIError.PANIC : FFIError.NULL;
        throw new FFIException(operation, code);
    }

    private static MemorySegment utf8(Arena arena, String value) {
        byte[] bytes = value.getBytes(StandardCharsets.UTF_8);
        MemorySegment input = bytes.length == 0 ? MemorySegment.NULL : arena.allocateFrom(ValueLayout.JAVA_BYTE, bytes);
        MemorySegment out = desu.life.raw.String_.allocate(arena);
        RosuNative.interoptopus_string_create(input, bytes.length, out);
        return out;
    }

    private static String consumeString(MemorySegment value) {
        long len = desu.life.raw.String_.len(value);
        MemorySegment ptr = desu.life.raw.String_.ptr(value);
        String result = len == 0 ? "" : new String(ptr.reinterpret(len).toArray(java.lang.foreign.ValueLayout.JAVA_BYTE), StandardCharsets.UTF_8);
        RosuNative.interoptopus_string_destroy(value);
        return result;
    }

    private static MemorySegment keep(MemorySegment value, long size) {
        MemorySegment copy = RESULTS.allocate(size, 8);
        MemorySegment.copy(value, 0, copy, 0, size);
        return copy;
    }

    public static class OptionDouble {
        public int variant; public double some;
        OptionalDouble toOptional() { return variant == 0 ? OptionalDouble.of(some) : OptionalDouble.empty(); }
    }
    public static class OptionUint {
        public int variant; public int some;
        public OptionalInt toOptional() { return variant == 0 ? OptionalInt.of(some) : OptionalInt.empty(); }
    }

    public static class OsuDifficultyAttributes {
        public double aim, aim_difficult_slider_count, speed, flashlight, reading, slider_factor;
        public double aim_top_weighted_slider_factor, speed_top_weighted_slider_factor, speed_note_count;
        public double aim_difficult_strain_count, speed_difficult_strain_count, reading_difficult_note_count;
        public double nested_score_per_object, legacy_score_base_multiplier, maximum_legacy_combo_score;
        public double ar, great_hit_window, ok_hit_window, meh_hit_window, hp;
        public int n_circles, n_sliders, n_large_ticks, n_spinners;
        public double stars; public int max_combo;
    }
    public static class TaikoDifficultyAttributes {
        public double stamina, rhythm, color, reading, great_hit_window, ok_hit_window;
        public double mono_stamina_factor, mechanical_difficulty, consistency_factor, stars;
        public int max_combo; public boolean is_convert;
    }
    public static class CatchDifficultyAttributes {
        public double stars, preempt; public int n_fruits, n_droplets, n_tiny_droplets; public boolean is_convert;
    }
    public static class ManiaDifficultyAttributes {
        public double stars; public int n_objects, n_hold_notes, max_combo; public boolean is_convert;
    }

    public static class DifficultyAttributes {
        final MemorySegment segment;
        public final byte variant;
        private final Object payload;
        DifficultyAttributes(MemorySegment source) {
            segment = keep(source, desu.life.raw.DifficultyAttributes.sizeof());
            variant = (byte) desu.life.raw.DifficultyAttributes.variant(segment);
            MemorySegment union = desu.life.raw.DifficultyAttributes.payload(segment);
            payload = switch (variant) {
                case 0 -> decode(desu.life.raw.DifficultyAttributes.payload.osu(union), OsuDifficultyAttributes.class, desu.life.raw.OsuDifficultyAttributes.class);
                case 1 -> decode(desu.life.raw.DifficultyAttributes.payload.taiko(union), TaikoDifficultyAttributes.class, desu.life.raw.TaikoDifficultyAttributes.class);
                case 2 -> decode(desu.life.raw.DifficultyAttributes.payload.catch_(union), CatchDifficultyAttributes.class, desu.life.raw.CatchDifficultyAttributes.class);
                case 3 -> decode(desu.life.raw.DifficultyAttributes.payload.mania(union), ManiaDifficultyAttributes.class, desu.life.raw.ManiaDifficultyAttributes.class);
                default -> throw new IllegalStateException("Invalid difficulty variant " + variant);
            };
        }
        public Mode mode() { return Mode.fromValue(Byte.toUnsignedInt(variant)); }
        public OsuDifficultyAttributes asOsu() { return require(Mode.Osu, OsuDifficultyAttributes.class); }
        public TaikoDifficultyAttributes asTaiko() { return require(Mode.Taiko, TaikoDifficultyAttributes.class); }
        public CatchDifficultyAttributes asCatch() { return require(Mode.Catch, CatchDifficultyAttributes.class); }
        public ManiaDifficultyAttributes asMania() { return require(Mode.Mania, ManiaDifficultyAttributes.class); }
        private <T> T require(Mode mode, Class<T> type) {
            if (mode() != mode) throw new IllegalStateException("Expected " + mode + ", got " + mode());
            return type.cast(payload);
        }
    }

    public static class OsuPerformanceAttributes {
        public OsuDifficultyAttributes difficulty;
        public double pp, pp_acc, pp_aim, pp_flashlight, pp_reading, pp_speed, effective_miss_count;
        public OptionDouble speed_deviation;
        public double combo_based_estimated_miss_count;
        public OptionDouble score_based_estimated_miss_count;
        public double aim_estimated_slider_breaks, speed_estimated_slider_breaks;
    }
    public static class TaikoPerformanceAttributes {
        public TaikoDifficultyAttributes difficulty;
        public double pp, pp_acc, pp_difficulty;
        public OptionDouble estimated_unstable_rate;
    }
    public static class CatchPerformanceAttributes { public CatchDifficultyAttributes difficulty; public double pp; }
    public static class ManiaPerformanceAttributes { public ManiaDifficultyAttributes difficulty; public double pp, pp_difficulty; }

    public static class PerformanceAttributes {
        final MemorySegment segment;
        public final byte variant;
        private final Object payload;
        PerformanceAttributes(MemorySegment source) {
            segment = keep(source, desu.life.raw.PerformanceAttributes.sizeof());
            variant = (byte) desu.life.raw.PerformanceAttributes.variant(segment);
            MemorySegment union = desu.life.raw.PerformanceAttributes.payload(segment);
            payload = switch (variant) {
                case 0 -> decode(desu.life.raw.PerformanceAttributes.payload.osu(union), OsuPerformanceAttributes.class, desu.life.raw.OsuPerformanceAttributes.class);
                case 1 -> decode(desu.life.raw.PerformanceAttributes.payload.taiko(union), TaikoPerformanceAttributes.class, desu.life.raw.TaikoPerformanceAttributes.class);
                case 2 -> decode(desu.life.raw.PerformanceAttributes.payload.catch_(union), CatchPerformanceAttributes.class, desu.life.raw.CatchPerformanceAttributes.class);
                case 3 -> decode(desu.life.raw.PerformanceAttributes.payload.mania(union), ManiaPerformanceAttributes.class, desu.life.raw.ManiaPerformanceAttributes.class);
                default -> throw new IllegalStateException("Invalid performance variant " + variant);
            };
        }
        public Mode mode() { return Mode.fromValue(Byte.toUnsignedInt(variant)); }
        public OsuPerformanceAttributes asOsu() { return require(Mode.Osu, OsuPerformanceAttributes.class); }
        public TaikoPerformanceAttributes asTaiko() { return require(Mode.Taiko, TaikoPerformanceAttributes.class); }
        public CatchPerformanceAttributes asCatch() { return require(Mode.Catch, CatchPerformanceAttributes.class); }
        public ManiaPerformanceAttributes asMania() { return require(Mode.Mania, ManiaPerformanceAttributes.class); }
        private <T> T require(Mode mode, Class<T> type) {
            if (mode() != mode) throw new IllegalStateException("Expected " + mode + ", got " + mode());
            return type.cast(payload);
        }
    }

    public static class ScoreState {
        public int max_combo, osu_large_tick_hits, osu_small_tick_hits, slider_end_hits;
        public int n_geki, n_katu, n300, n100, n50, misses;
        public OptionUint legacy_total_score = new OptionUint();
        public ScoreState() {}
        ScoreState(MemorySegment s) { decodeInto(s, this, desu.life.raw.ScoreState.class); }
        MemorySegment encode(Arena arena) {
            MemorySegment s = desu.life.raw.ScoreState.allocate(arena);
            setRaw(s, desu.life.raw.ScoreState.class, this);
            return s;
        }
    }
    public static class HitWindows {
        public OptionDouble ar, od_perfect, od_great, od_good, od_ok, od_meh;
    }
    public static class BeatmapAttributes {
        public double ar, od; public float cs, hp; public double clock_rate; public HitWindows hit_windows;
        BeatmapAttributes(MemorySegment s) { decodeInto(s, this, desu.life.raw.BeatmapAttributes.class); }
    }

    public record SliderData(long repeats, OptionalDouble expectedDistance) {}
    public record HitObject(float x, float y, double startTime, HitObjectKind kind, SliderData slider, double duration) {}

    public static class WireHitObjects implements AutoCloseable {
        private MemorySegment data; private int len, capacity;
        WireHitObjects(MemorySegment s) {
            data=desu.life.raw.Wire_Vec_HitObject.data(s); len=desu.life.raw.Wire_Vec_HitObject.len(s);
            capacity=desu.life.raw.Wire_Vec_HitObject.capacity(s);
        }
        public List<HitObject> unwire() {
            if (data.equals(MemorySegment.NULL) || len == 0) return List.of();
            ByteBuffer b=data.reinterpret(len).asByteBuffer().order(ByteOrder.LITTLE_ENDIAN);
            int count=b.getInt(); List<HitObject> result=new ArrayList<>(count);
            for(int i=0;i<count;i++) {
                float x=b.getFloat(), y=b.getFloat(); double start=b.getDouble();
                HitObjectKind kind=HitObjectKind.values()[Byte.toUnsignedInt(b.get())];
                SliderData slider=null; double duration=0;
                if(kind==HitObjectKind.Slider) {
                    long repeats=Integer.toUnsignedLong(b.getInt()); int option=Byte.toUnsignedInt(b.get());
                    slider=new SliderData(repeats, option==0?OptionalDouble.of(b.getDouble()):OptionalDouble.empty());
                } else if(kind==HitObjectKind.Spinner||kind==HitObjectKind.Hold) duration=b.getDouble();
                result.add(new HitObject(x,y,start,kind,slider,duration));
            }
            return result;
        }
        public void close() {
            if(!data.equals(MemorySegment.NULL)) {
                RosuNative.interoptopus_wire_destroy_78044(data,len,capacity);
                data=MemorySegment.NULL; len=capacity=0;
            }
        }
    }

    private abstract static class Service implements AutoCloseable {
        private MemorySegment context;
        Service(MemorySegment context) { this.context=context; }
        final MemorySegment context() {
            if(context.equals(MemorySegment.NULL)) throw new IllegalStateException("Service already closed");
            return context;
        }
        abstract void destroy(MemorySegment context);
        public final void close() { if(!context.equals(MemorySegment.NULL)){ destroy(context); context=MemorySegment.NULL; } }
    }

    public static final class Beatmap extends Service {
        public Beatmap(byte[] data) { super(fromBytes(data)); }
        private static MemorySegment fromBytes(byte[] data) {
            try(Arena a=Arena.ofConfined()) {
                MemorySegment slice=desu.life.raw.Slice_u8.allocate(a);
                MemorySegment bytes=data.length==0?MemorySegment.NULL:a.allocateFrom(ValueLayout.JAVA_BYTE,data);
                desu.life.raw.Slice_u8.data(slice,bytes); desu.life.raw.Slice_u8.len(slice,data.length);
                return unwrap(RosuNative.beatmap_from_bytes(a,slice),"beatmap_from_bytes");
            }
        }
        public Beatmap(String path) { super(fromPath(path)); }
        private static MemorySegment fromPath(String path) {
            try(Arena a=Arena.ofConfined()) { return unwrap(RosuNative.beatmap_from_path(a,utf8(a,path)),"beatmap_from_path"); }
        }
        void destroy(MemorySegment c){RosuNative.beatmap_destroy(c);}
        public boolean convert(Mode m,Mods mods){return RosuNative.beatmap_convert(context(),m.value,mods.context());}
        public boolean convert(Mode m){try(var mods=Mods.create(m)){return convert(m,mods);}}
        public double bpm(){return RosuNative.beatmap_bpm(context());}
        public double totalBreakTime(){return RosuNative.beatmap_total_break_time(context());}
        public int version(){return RosuNative.beatmap_version(context());}
        public boolean isConvert(){return RosuNative.beatmap_is_convert(context());}
        public float stackLeniency(){return RosuNative.beatmap_stack_leniency(context());}
        public Mode mode(){return Mode.fromValue(RosuNative.beatmap_mode(context()));}
        public float ar(){return RosuNative.beatmap_ar(context());} public float cs(){return RosuNative.beatmap_cs(context());}
        public float hp(){return RosuNative.beatmap_hp(context());} public float od(){return RosuNative.beatmap_od(context());}
        public double sliderMultiplier(){return RosuNative.beatmap_slider_multiplier(context());}
        public double sliderTickRate(){return RosuNative.beatmap_slider_tick_rate(context());}
        public Optional<TooSuspicious> checkSuspicious(){try(Arena a=Arena.ofConfined()){var s=RosuNative.beatmap_check_suspicious(a,context());return desu.life.raw.Option_TooSuspicious.variant(s)==0?Optional.of(TooSuspicious.fromValue(desu.life.raw.Option_TooSuspicious.some(s))):Optional.empty();}}
        public WireHitObjects hitObjects(){try(Arena a=Arena.ofConfined()){return new WireHitObjects(RosuNative.beatmap_hit_objects(a,context()));}}
    }

    public static final class Mods extends Service {
        private Mods(MemorySegment c){super(c);}
        public static Mods create(Mode m){try(Arena a=Arena.ofConfined()){return new Mods(unwrap(RosuNative.mods_create(a,m.value),"mods_create"));}}
        public static Mods fromAcronyms(String v,Mode m){try(Arena a=Arena.ofConfined()){return new Mods(unwrap(RosuNative.mods_from_acronyms(a,utf8(a,v),m.value),"mods_from_acronyms"));}}
        public static Mods fromBits(long v,Mode m){try(Arena a=Arena.ofConfined()){return new Mods(unwrap(RosuNative.mods_from_bits(a,(int)v,m.value),"mods_from_bits"));}}
        public static Mods fromJson(String v,Mode m,boolean deny){try(Arena a=Arena.ofConfined()){return new Mods(unwrap(RosuNative.mods_from_json(a,utf8(a,v),m.value,deny),"mods_from_json"));}}
        void destroy(MemorySegment c){RosuNative.mods_destroy(c);}
        public void removeUnknownMods(){RosuNative.mods_remove_unknown_mods(context());} public void sanitize(){RosuNative.mods_sanitize(context());}
        public long bits(){return Integer.toUnsignedLong(RosuNative.mods_bits(context()));} public long length(){return Integer.toUnsignedLong(RosuNative.mods_len(context()));}
        public String json(){try(Arena a=Arena.ofConfined()){return consumeString(RosuNative.mods_json(a,context()));}}
        public boolean insertJson(String v,boolean deny){try(Arena a=Arena.ofConfined()){return RosuNative.mods_insert_json(context(),utf8(a,v),deny);}}
        public void insert(String v){try(Arena a=Arena.ofConfined()){RosuNative.mods_insert(context(),utf8(a,v));}}
        public boolean contains(String v){try(Arena a=Arena.ofConfined()){return RosuNative.mods_contains(context(),utf8(a,v));}}
        public void clear(){RosuNative.mods_clear(context());}
        public OptionalDouble clockRate(){try(Arena a=Arena.ofConfined()){var s=RosuNative.mods_clock_rate(a,context());return desu.life.raw.Option_f64.variant(s)==0?OptionalDouble.of(desu.life.raw.Option_f64.some(s)):OptionalDouble.empty();}}
    }

    public static final class Difficulty extends Service {
        public Difficulty(){super(create());} private static MemorySegment create(){try(Arena a=Arena.ofConfined()){return unwrap(RosuNative.difficulty_create(a),"difficulty_create");}}
        void destroy(MemorySegment c){RosuNative.difficulty_destroy(c);}
        public void mods(Mods v){RosuNative.difficulty_p_mods(context(),v.context());} public void mods(long v){RosuNative.difficulty_i_mods(context(),(int)v);}
        public void mods(String v){try(Arena a=Arena.ofConfined()){RosuNative.difficulty_s_mods(context(),utf8(a,v));}}
        public void passedObjects(long v){RosuNative.difficulty_passed_objects(context(),(int)v);} public void clockRate(double v){RosuNative.difficulty_clock_rate(context(),v);}
        public void ar(float v){RosuNative.difficulty_ar(context(),v);} public void cs(float v){RosuNative.difficulty_cs(context(),v);}
        public void hp(float v){RosuNative.difficulty_hp(context(),v);} public void od(float v){RosuNative.difficulty_od(context(),v);}
        public void hardrockOffsets(boolean v){RosuNative.difficulty_hardrock_offsets(context(),v);} public void lazer(boolean v){RosuNative.difficulty_lazer(context(),v);}
        public DifficultyAttributes calculate(Beatmap b){try(Arena a=Arena.ofConfined()){return new DifficultyAttributes(RosuNative.difficulty_calculate(a,context(),b.context()));}}
        public double clockRate(){return RosuNative.difficulty_get_clock_rate(context());}
    }

    public static final class Performance extends Service {
        public Performance(){super(create());} private static MemorySegment create(){try(Arena a=Arena.ofConfined()){return unwrap(RosuNative.performance_create(a),"performance_create");}}
        void destroy(MemorySegment c){RosuNative.performance_destroy(c);}
        public void mode(Mode v){RosuNative.performance_mode(context(),v.value);} public void mods(Mods v){RosuNative.performance_p_mods(context(),v.context());}
        public void mods(long v){RosuNative.performance_i_mods(context(),(int)v);} public void mods(String v){try(Arena a=Arena.ofConfined()){RosuNative.performance_s_mods(context(),utf8(a,v));}}
        public void passedObjects(long v){RosuNative.performance_passed_objects(context(),(int)v);} public void legacyTotalScore(long v){RosuNative.performance_legacy_total_score(context(),(int)v);}
        public void clockRate(double v){RosuNative.performance_clock_rate(context(),v);} public void ar(float v){RosuNative.performance_ar(context(),v);}
        public void cs(float v){RosuNative.performance_cs(context(),v);} public void hp(float v){RosuNative.performance_hp(context(),v);} public void od(float v){RosuNative.performance_od(context(),v);}
        public void hardrockOffsets(boolean v){RosuNative.performance_hardrock_offsets(context(),v);} public void accuracy(double v){RosuNative.performance_accuracy(context(),v);}
        public void misses(long v){RosuNative.performance_misses(context(),(int)v);} public void combo(long v){RosuNative.performance_combo(context(),(int)v);}
        public void hitResultPriority(HitResultPriority v){RosuNative.performance_hitresult_priority(context(),v.value);} public void lazer(boolean v){RosuNative.performance_lazer(context(),v);}
        public void largeTickHits(long v){RosuNative.performance_large_tick_hits(context(),(int)v);} public void smallTickHits(long v){RosuNative.performance_small_tick_hits(context(),(int)v);}
        public void sliderEndHits(long v){RosuNative.performance_slider_end_hits(context(),(int)v);} public void n300(long v){RosuNative.performance_n300(context(),(int)v);}
        public void n100(long v){RosuNative.performance_n100(context(),(int)v);} public void n50(long v){RosuNative.performance_n50(context(),(int)v);}
        public void nKatu(long v){RosuNative.performance_n_katu(context(),(int)v);} public void nGeki(long v){RosuNative.performance_n_geki(context(),(int)v);}
        public void state(ScoreState v){try(Arena a=Arena.ofConfined()){RosuNative.performance_state(context(),v.encode(a));}}
        public ScoreState generateState(Beatmap b){try(Arena a=Arena.ofConfined()){return new ScoreState(RosuNative.performance_generate_state(a,context(),b.context()));}}
        public ScoreState generateState(DifficultyAttributes v){try(Arena a=Arena.ofConfined()){return new ScoreState(RosuNative.performance_generate_state_from_difficulty(a,context(),v.segment));}}
        public PerformanceAttributes calculate(Beatmap b){try(Arena a=Arena.ofConfined()){return new PerformanceAttributes(RosuNative.performance_calculate(a,context(),b.context()));}}
        public PerformanceAttributes calculate(DifficultyAttributes v){try(Arena a=Arena.ofConfined()){return new PerformanceAttributes(RosuNative.performance_calculate_from_difficulty(a,context(),v.segment));}}
        public double clockRate(){return RosuNative.performance_get_clock_rate(context());}
    }

    public static final class BeatmapAttributesBuilder extends Service {
        public BeatmapAttributesBuilder(){super(create());} private static MemorySegment create(){try(Arena a=Arena.ofConfined()){return unwrap(RosuNative.beatmap_attributes_builder_create(a),"beatmap_attributes_builder_create");}}
        void destroy(MemorySegment c){RosuNative.beatmap_attributes_builder_destroy(c);}
        public void mode(Mode v){RosuNative.beatmap_attributes_builder_mode(context(),v.value);} public void mods(Mods v){RosuNative.beatmap_attributes_builder_p_mods(context(),v.context());}
        public void mods(long v){RosuNative.beatmap_attributes_builder_i_mods(context(),(int)v);} public void mods(String v){try(Arena a=Arena.ofConfined()){RosuNative.beatmap_attributes_builder_s_mods(context(),utf8(a,v));}}
        public void clockRate(double v){RosuNative.beatmap_attributes_builder_clock_rate(context(),v);} public void ar(float v){RosuNative.beatmap_attributes_builder_ar(context(),v);}
        public void cs(float v){RosuNative.beatmap_attributes_builder_cs(context(),v);} public void hp(float v){RosuNative.beatmap_attributes_builder_hp(context(),v);}
        public void od(float v){RosuNative.beatmap_attributes_builder_od(context(),v);} public double clockRate(){return RosuNative.beatmap_attributes_builder_get_clock_rate(context());}
        public BeatmapAttributes build(Beatmap b){try(Arena a=Arena.ofConfined()){return new BeatmapAttributes(RosuNative.beatmap_attributes_builder_build(a,context(),b.context()));}}
    }

    public static final class GradualDifficulty extends Service {
        private GradualDifficulty(MemorySegment c){super(c);}
        public static GradualDifficulty create(Difficulty d,Beatmap b){try(Arena a=Arena.ofConfined()){return new GradualDifficulty(unwrap(RosuNative.gradual_difficulty_create(a,d.context(),b.context()),"gradual_difficulty_create"));}}
        public static GradualDifficulty create(Difficulty d,Beatmap b,Mode m){try(Arena a=Arena.ofConfined()){return new GradualDifficulty(unwrap(RosuNative.gradual_difficulty_new_with_mode(a,d.context(),b.context(),m.value),"gradual_difficulty_new_with_mode"));}}
        void destroy(MemorySegment c){RosuNative.gradual_difficulty_destroy(c);}
        public Optional<DifficultyAttributes> next(){try(Arena a=Arena.ofConfined()){return optionalDifficulty(RosuNative.gradual_difficulty_next(a,context()));}}
        public Optional<DifficultyAttributes> nth(long n){try(Arena a=Arena.ofConfined()){return optionalDifficulty(RosuNative.gradual_difficulty_nth(a,context(),(int)n));}}
        public long length(){return Integer.toUnsignedLong(RosuNative.gradual_difficulty_len(context()));}
    }
    public static final class GradualPerformance extends Service {
        private GradualPerformance(MemorySegment c){super(c);}
        public static GradualPerformance create(Difficulty d,Beatmap b){try(Arena a=Arena.ofConfined()){return new GradualPerformance(unwrap(RosuNative.gradual_performance_create(a,d.context(),b.context()),"gradual_performance_create"));}}
        public static GradualPerformance create(Difficulty d,Beatmap b,Mode m){try(Arena a=Arena.ofConfined()){return new GradualPerformance(unwrap(RosuNative.gradual_performance_new_with_mode(a,d.context(),b.context(),m.value),"gradual_performance_new_with_mode"));}}
        void destroy(MemorySegment c){RosuNative.gradual_performance_destroy(c);}
        public Optional<PerformanceAttributes> next(ScoreState s){try(Arena a=Arena.ofConfined()){return optionalPerformance(RosuNative.gradual_performance_next(a,context(),s.encode(a)));}}
        public Optional<PerformanceAttributes> last(ScoreState s){try(Arena a=Arena.ofConfined()){return optionalPerformance(RosuNative.gradual_performance_last(a,context(),s.encode(a)));}}
        public Optional<PerformanceAttributes> nth(ScoreState s,long n){try(Arena a=Arena.ofConfined()){return optionalPerformance(RosuNative.gradual_performance_nth(a,context(),s.encode(a),(int)n));}}
        public long length(){return Integer.toUnsignedLong(RosuNative.gradual_performance_len(context()));}
    }

    private static Optional<DifficultyAttributes> optionalDifficulty(MemorySegment s){return desu.life.raw.Option_DifficultyAttributes.variant(s)==0?Optional.of(new DifficultyAttributes(desu.life.raw.Option_DifficultyAttributes.some(s))):Optional.empty();}
    private static Optional<PerformanceAttributes> optionalPerformance(MemorySegment s){return desu.life.raw.Option_PerformanceAttributes.variant(s)==0?Optional.of(new PerformanceAttributes(desu.life.raw.Option_PerformanceAttributes.some(s))):Optional.empty();}
    public static String debug(DifficultyAttributes v){try(Arena a=Arena.ofConfined()){return consumeString(RosuNative.debug_difficulty_attributes(a,v.segment));}}
    public static String debug(PerformanceAttributes v){try(Arena a=Arena.ofConfined()){return consumeString(RosuNative.debug_performance_attributes(a,v.segment));}}
    public static String debug(ScoreState v){try(Arena a=Arena.ofConfined()){return consumeString(RosuNative.debug_score_state(a,v.encode(a)));}}
    public static double calculateAccuracy(ScoreState s,DifficultyAttributes a,OsuScoreOrigin o){try(Arena arena=Arena.ofConfined()){return RosuNative.calculate_accuacy(s.encode(arena),a.segment,o.value);}}

    private static <T> T decode(MemorySegment s,Class<T> facade,Class<?> raw){try{T v=facade.getDeclaredConstructor().newInstance();decodeInto(s,v,raw);return v;}catch(ReflectiveOperationException e){throw new IllegalStateException(e);}}
    private static void decodeInto(MemorySegment s,Object target,Class<?> raw){
        try {
            for(Field f:target.getClass().getFields()){
                if(Modifier.isStatic(f.getModifiers()))continue;
                Method getter; try{getter=raw.getMethod(f.getName(),MemorySegment.class);}catch(NoSuchMethodException ignored){continue;}
                Object value=getter.invoke(null,s);
                if(f.getType()==boolean.class && value instanceof Boolean b) f.setBoolean(target,b);
                else if(f.getType()==OptionDouble.class){MemorySegment x=(MemorySegment)value;OptionDouble o=new OptionDouble();o.variant=desu.life.raw.Option_f64.variant(x);o.some=desu.life.raw.Option_f64.some(x);f.set(target,o);}
                else if(f.getType()==OptionUint.class){MemorySegment x=(MemorySegment)value;OptionUint o=new OptionUint();o.variant=desu.life.raw.Option_u32.variant(x);o.some=desu.life.raw.Option_u32.some(x);f.set(target,o);}
                else if(value instanceof MemorySegment x){String n=f.getType().getSimpleName();Class<?> rr=Class.forName("desu.life.raw."+n);f.set(target,decode(x,f.getType(),rr));}
                else f.set(target,value);
            }
        } catch(ReflectiveOperationException e){throw new IllegalStateException(e);}
    }
    private static void setRaw(MemorySegment s,Class<?> raw,Object source){
        try {
            for(Field f:source.getClass().getFields()){
                if(Modifier.isStatic(f.getModifiers()))continue; Object value=f.get(source);
                if(f.getType()==OptionUint.class) continue;
                try{raw.getMethod(f.getName(),MemorySegment.class,f.getType()).invoke(null,s,value);}catch(NoSuchMethodException ignored){}
            }
            OptionUint o=((ScoreState)source).legacy_total_score; MemorySegment x=desu.life.raw.ScoreState.legacy_total_score(s);
            desu.life.raw.Option_u32.variant(x,o.variant);desu.life.raw.Option_u32.some(x,o.some);
        }catch(ReflectiveOperationException e){throw new IllegalStateException(e);}
    }
}
