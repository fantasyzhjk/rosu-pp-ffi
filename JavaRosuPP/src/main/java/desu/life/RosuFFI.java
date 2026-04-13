package desu.life;

import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.lang.ref.Cleaner;
import java.nio.ByteBuffer;
import java.nio.file.Files;
import java.util.Optional;

import com.sun.jna.Memory;
import com.sun.jna.Native;
import com.sun.jna.Pointer;
import com.sun.jna.Structure;
import com.sun.jna.ptr.PointerByReference;

@SuppressWarnings("unused")
public class RosuFFI {
    private static final Cleaner cleaner = Cleaner.create();

    public enum Mode {
        /// osu!standard
        Osu(0),
        /// osu!taiko
        Taiko(1),
        /// osu!catch
        Catch(2),
        /// osu!mania
        Mania(3);

        private final int value;

        Mode(int value) {
            this.value = value;
        }

        public int getValue() {
            return value;
        }

        public static Mode fromValue(int value) {
            for (Mode v : values()) {
                if (v.value == value) {
                    return v;
                }
            }
            throw new IllegalArgumentException("Unknown mode value: " + value);
        }
    }

    public enum HitResultPriority {
        BestCase(0),
        WorstCase(1);

        private final int value;

        HitResultPriority(int value) {
            this.value = value;
        }

        public int getValue() {
            return value;
        }

        public static HitResultPriority fromValue(int value) {
            for (HitResultPriority v : values()) {
                if (v.value == value) {
                    return v;
                }
            }
            throw new IllegalArgumentException("Unknown mode value: " + value);
        }
    }

    public enum OsuScoreOrigin {
        /// For scores set on osu!stable
        Stable(0),
        /// For scores set on osu!lazer with slider accuracy
        WithSliderAcc(1),
        /// For scores set on osu!lazer without slider accuracy
        WithoutSliderAcc(2);

        private final int value;

        OsuScoreOrigin(int value) {
            this.value = value;
        }

        public int getValue() {
            return value;
        }

        public static OsuScoreOrigin fromValue(int value) {
            for (OsuScoreOrigin v : values()) {
                if (v.value == value) {
                    return v;
                }
            }
            throw new IllegalArgumentException("Unknown mode value: " + value);
        }
    }

    public interface FFIError {
        int Ok = 0;
        int Null = 100;
        int Panic = 200;
        int IoError = 300;
        int Utf8Error = 400;
        int InvalidString = 500;
        int SerializeError = 600;
        int ConvertError = 700;
        int Unknown = 1000;
    }

    public static class RosuPPLib {

        // JNA 为 dll 名称
        // RosuPPLib INSTANCE = Native.load("rosu_pp_ffi", RosuPPLib.class);

        private static File extractLibrary(String libName) throws IOException {
            // 从 classpath 中读取库文件
            InputStream input = RosuFFI.class.getClassLoader().getResourceAsStream(libName);
            if (input == null) {
                throw new IllegalArgumentException("Library not found: " + libName);
            }

            // 创建临时文件
            File tempFile = File.createTempFile("native", libName.substring(libName.lastIndexOf('.')));
            tempFile.deleteOnExit();

            // 将资源写入临时文件
            Files.copy(input, tempFile.toPath(), java.nio.file.StandardCopyOption.REPLACE_EXISTING);
            input.close();
            return tempFile;
        }

        static {

            // 根据系统选择库文件
            String libName = System.getProperty("os.name").toLowerCase().contains("win") ? "native/rosu_pp_ffi.dll" : "native/librosu_pp_ffi.so";

            // 从 resources 提取库到临时文件
            try {
                File tempFile = extractLibrary(libName);
                // 加载本地库
                Native.register(tempFile.getAbsolutePath());
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        }

        /// Destroys the given instance.
        ///
        /// # Safety
        ///
        /// The passed parameter MUST have been created with the corresponding init function;
        /// passing any other value results in undefined behavior.
        public static native int beatmap_attributes_destroy(PointerByReference context);

        public static native int beatmap_attributes_new(PointerByReference context);

        public static native void beatmap_attributes_mode(Pointer context, int mode);

        public static native void beatmap_attributes_p_mods(Pointer context, Pointer mods);

        public static native void beatmap_attributes_i_mods(Pointer context, long mods);

        public static native int beatmap_attributes_s_mods(Pointer context, String str);

        public static native void beatmap_attributes_clock_rate(Pointer context, double clock_rate);

        public static native void beatmap_attributes_ar(Pointer context, float ar);

        public static native void beatmap_attributes_cs(Pointer context, float cs);

        public static native void beatmap_attributes_hp(Pointer context, float hp);

        public static native void beatmap_attributes_od(Pointer context, float od);

        public static native double beatmap_attributes_get_clock_rate(Pointer context);

        public static native BeatmapAttributes.ByValue beatmap_attributes_build(Pointer context, Pointer beatmap);

        /// Destroys the given instance.
        ///
        /// # Safety
        ///
        /// The passed parameter MUST have been created with the corresponding init function;
        /// passing any other value results in undefined behavior.
        public static native int beatmap_destroy(PointerByReference context);

        public static native int beatmap_from_bytes(PointerByReference context, Sliceu8 data);

        public static native int beatmap_from_path(PointerByReference context, String path);

        /// Convert a Beatmap to the specified mode
        public static native boolean beatmap_convert(Pointer context, int mode, Pointer mods);

        public static native double beatmap_bpm(Pointer context);

        public static native double beatmap_total_break_time(Pointer context);

        public static native int beatmap_mode(Pointer context);

        public static native boolean beatmap_is_convert(Pointer context);

        /// Destroys the given instance.
        ///
        /// # Safety
        ///
        /// The passed parameter MUST have been created with the corresponding init function;
        /// passing any other value results in undefined behavior.
        public static native int difficulty_destroy(PointerByReference context);

        public static native int difficulty_new(PointerByReference context);

        public static native void difficulty_p_mods(Pointer context, Pointer mods);

        public static native void difficulty_i_mods(Pointer context, long mods);

        public static native int difficulty_s_mods(Pointer context, String str);

        public static native void difficulty_passed_objects(Pointer context, long passed_objects);

        public static native void difficulty_clock_rate(Pointer context, double clock_rate);

        public static native void difficulty_ar(Pointer context, float ar);

        public static native void difficulty_cs(Pointer context, float cs);

        public static native void difficulty_hp(Pointer context, float hp);

        public static native void difficulty_od(Pointer context, float od);

        public static native void difficulty_hardrock_offsets(Pointer context, boolean hardrock_offsets);

        public static native void difficulty_lazer(Pointer context, boolean lazer);

        public static native DifficultyAttributes.ByValue difficulty_calculate(Pointer context, Pointer beatmap);

        public static native double difficulty_get_clock_rate(Pointer context);

        /// Destroys the given instance.
        ///
        /// # Safety
        ///
        /// The passed parameter MUST have been created with the corresponding init function;
        /// passing any other value results in undefined behavior.
        public static native int performance_destroy(PointerByReference context);

        public static native int performance_new(PointerByReference context);

        public static native void performance_mode(Pointer context, int mode);

        public static native void performance_p_mods(Pointer context, Pointer mods);

        public static native void performance_i_mods(Pointer context, long mods);

        public static native int performance_s_mods(Pointer context, String str);

        public static native void performance_passed_objects(Pointer context, long passed_objects);

        public static native void performance_clock_rate(Pointer context, double clock_rate);

        public static native void performance_ar(Pointer context, float ar);

        public static native void performance_cs(Pointer context, float cs);

        public static native void performance_hp(Pointer context, float hp);

        public static native void performance_od(Pointer context, float od);

        public static native void performance_hardrock_offsets(Pointer context, boolean hardrock_offsets);

        public static native void performance_state(Pointer context, ScoreState.ByValue accuracy);

        public static native void performance_accuracy(Pointer context, double accuracy);

        public static native void performance_misses(Pointer context, long misses);

        public static native void performance_combo(Pointer context, long combo);

        public static native void performance_hitresult_priority(Pointer context, int hitresult_priority);

        public static native void performance_lazer(Pointer context, boolean lazer);

        public static native void performance_large_tick_hits(Pointer context, long large_tick_hits);

        public static native void performance_small_tick_hits(Pointer context, long small_tick_hits);

        public static native void performance_slider_end_hits(Pointer context, long slider_end_hits);

        public static native void performance_n300(Pointer context, long n300);

        public static native void performance_n100(Pointer context, long n100);

        public static native void performance_n50(Pointer context, long n50);

        public static native void performance_n_katu(Pointer context, long n_katu);

        public static native void performance_n_geki(Pointer context, long n_geki);

        public static native ScoreState.ByValue performance_generate_state(Pointer context, Pointer beatmap);

        public static native ScoreState.ByValue performance_generate_state_from_difficulty(Pointer context, DifficultyAttributes.ByValue difficulty_attr);

        public static native PerformanceAttributes.ByValue performance_calculate(Pointer context, Pointer beatmap);

        public static native PerformanceAttributes.ByValue performance_calculate_from_difficulty(Pointer context, DifficultyAttributes.ByValue difficulty_attr);

        public static native double performance_get_clock_rate(Pointer context);

        
        /// Destroys the given instance.
        ///
        /// # Safety
        ///
        /// The passed parameter MUST have been created with the corresponding init function;
        /// passing any other value results in undefined behavior.
        public static native int gradual_difficulty_destroy(PointerByReference context);

        /// Create a [`GradualDifficulty`] for a map of any mode.
        public static native int gradual_difficulty_new(PointerByReference context, Pointer difficulty, Pointer beatmap);

        /// Create a [`GradualDifficulty`] for a [`Beatmap`] on a specific [`GameMode`].
        public static native int gradual_difficulty_new_with_mode(PointerByReference context, Pointer difficulty, Pointer beatmap, int mode);

        public static native OptionDifficultyAttributes gradual_difficulty_next(Pointer context);

        public static native OptionDifficultyAttributes gradual_difficulty_nth(Pointer context, long n);

        public static native long gradual_difficulty_len(Pointer context);

        /// Destroys the given instance.
        ///
        /// # Safety
        ///
        /// The passed parameter MUST have been created with the corresponding init function;
        /// passing any other value results in undefined behavior.
        public static native int gradual_performance_destroy(PointerByReference context);

        /// Create a [`GradualPerformance`] for a map of any mode.
        public static native int gradual_performance_new(PointerByReference context, Pointer difficulty, Pointer beatmap);

        /// Create a [`GradualPerformance`] for a [`Beatmap`] on a specific [`GameMode`].
        public static native int gradual_performance_new_with_mode(PointerByReference context, Pointer difficulty, Pointer beatmap, int mode);

        /// Process the next hit object and calculate the performance attributes
        /// for the resulting score state.
        public static native OptionPerformanceAttributes gradual_performance_next(Pointer context, ScoreState.ByValue state);

        /// Process all remaining hit objects and calculate the final performance
        /// attributes.
        public static native OptionPerformanceAttributes gradual_performance_last(Pointer context, ScoreState.ByValue state);

        /// Process everything up to the next `n`th hitobject and calculate the
        /// performance attributes for the resulting score state.
        ///
        /// Note that the count is zero-indexed, so `n=0` will process 1 object,
        /// `n=1` will process 2, and so on.
        public static native OptionPerformanceAttributes gradual_performance_nth(Pointer context, ScoreState.ByValue state, long n);

        /// Returns the amount of remaining objects.
        public static native long gradual_performance_len(Pointer context);


        /// Destroys the given instance.
        ///
        /// # Safety
        ///
        /// The passed parameter MUST have been created with the corresponding init function;
        /// passing any other value results in undefined behavior.
        public static native int string_destroy(PointerByReference context);

        public static native int string_from_c_str(PointerByReference context, String str);

        public static native int string_empty(PointerByReference context);

        public static native boolean string_is_init(Pointer context);

        public static native String string_to_cstr(Pointer context);

        /// Destroys the given instance.
        ///
        /// # Safety
        ///
        /// The passed parameter MUST have been created with the corresponding init function;
        /// passing any other value results in undefined behavior.
        public static native int mods_destroy(PointerByReference context);

        public static native int mods_new(PointerByReference context, int mode);

        public static native int mods_from_acronyms(PointerByReference context, String str, int mode);

        public static native int mods_from_bits(PointerByReference context, long bits, int mode);

        public static native int mods_from_json(PointerByReference context, String str, int mode, boolean deny_unknown_fields);

        public static native void mods_remove_unknown_mods(Pointer context);

        public static native void mods_sanitize(Pointer context);

        public static native long mods_bits(Pointer context);

        public static native long mods_len(Pointer context);

        public static native void mods_json(Pointer context, Pointer str);

        public static native boolean mods_insert_json(Pointer context, String str, boolean deny_unknown_fields);

        public static native boolean mods_insert(Pointer context, String str);

        public static native boolean mods_contains(Pointer context, String str);

        public static native void mods_clear(Pointer context);

        public static native Optionf64 mods_clock_rate(Pointer context);

        public static native void debug_difficylty_attributes(DifficultyAttributes res, Pointer str);

        public static native void debug_performance_attributes(PerformanceAttributes res, Pointer str);

        public static native void debug_score_state(ScoreState res, Pointer str);

        public static native double calculate_accuacy(ScoreState state, DifficultyAttributes difficulty, int origin);


        @Structure.FieldOrder({"data", "len"})
        public static class Sliceu8 extends Structure {
            public Pointer data;
            public long len;

            public Sliceu8(ByteBuffer data) {
                this.data = Native.getDirectBufferPointer(data);
                this.len = data.capacity();
            }

            public Sliceu8(byte[] data) {
                var mem = new Memory(data.length);
                mem.write(0, data, 0, data.length);
                this.data = mem;
                this.len = data.length;
            }

            public Sliceu8() {}

            public static class ByReference extends Sliceu8 implements Structure.ByReference {}
            public static class ByValue extends Sliceu8 implements Structure.ByValue {}
        }

        @Structure.FieldOrder({"t", "is_some"})
        public static class Optionf64 extends Structure {
            public double t;
            public byte is_some;

            public static class ByReference extends Optionf64 implements Structure.ByReference {}
            public static class ByValue extends Optionf64 implements Structure.ByValue {}

            public Optional<Double> toOptional() {
                return is_some == 1 ? Optional.of(t) : Optional.empty();
            }
        }

        @Structure.FieldOrder({"t", "is_some"})
        public static class Optionu32 extends Structure {
            public int t;
            public byte is_some;

            public static class ByReference extends Optionu32 implements Structure.ByReference {}
            public static class ByValue extends Optionu32 implements Structure.ByValue {}

            public Optional<Integer> toOptional() {
                return is_some == 1 ? Optional.of(t) : Optional.empty();
            }
        }

        @Structure.FieldOrder({"t", "is_some"})
        public static class OptionDifficultyAttributes extends Structure {
            public DifficultyAttributes t;
            public byte is_some;

            public static class ByReference extends OptionDifficultyAttributes implements Structure.ByReference {}
            public static class ByValue extends OptionDifficultyAttributes implements Structure.ByValue {}

            public Optional<DifficultyAttributes> toOptional() {
                return is_some == 1 ? Optional.of(t) : Optional.empty();
            }
        }

        @Structure.FieldOrder({"t", "is_some"})
        public static class OptionPerformanceAttributes extends Structure {
            public PerformanceAttributes t;
            public byte is_some;

            public static class ByReference extends OptionPerformanceAttributes implements Structure.ByReference {}
            public static class ByValue extends OptionPerformanceAttributes implements Structure.ByValue {}

            public Optional<PerformanceAttributes> toOptional() {
                return is_some == 1 ? Optional.of(t) : Optional.empty();
            }
        }

        @Structure.FieldOrder({ "aim", "aim_difficult_slider_count", "speed", "flashlight", "slider_factor",
            "aim_top_weighted_slider_factor", "speed_top_weighted_slider_factor",
            "speed_note_count", "aim_difficult_strain_count", "speed_difficult_strain_count",
            "nested_score_per_object", "legacy_score_base_multiplier", "maximum_legacy_combo_score",
                "ar", "great_hit_window", "ok_hit_window", "meh_hit_window", "hp",
                "n_circles", "n_sliders", "n_large_ticks", "n_spinners",
                "stars", "max_combo" })
        public static class OsuDifficultyAttributes extends Structure {
            public double aim;                           // Difficulty of the aim skill
            public double aim_difficult_slider_count;    // The number of sliders weighted by difficulty.
            public double speed;                         // Difficulty of the speed skill
            public double flashlight;                   // Difficulty of the flashlight skill
            public double slider_factor;                // Ratio of aim strain with/without sliders
            public double aim_top_weighted_slider_factor;
            public double speed_top_weighted_slider_factor;
            public double speed_note_count;             // Number of clickable objects weighted by difficulty
            public double aim_difficult_strain_count;   // Weighted sum of aim strains
            public double speed_difficult_strain_count; // Weighted sum of speed strains
            public double nested_score_per_object;
            public double legacy_score_base_multiplier;
            public double maximum_legacy_combo_score;
            public double ar;                           // Approach rate
            public double great_hit_window;             // great hit window.
            public double ok_hit_window;                // ok hit window.
            public double meh_hit_window;               // meh hit window.
            public double hp;                           // Health drain rate
            public int n_circles;                       // Number of circles (unsigned int -> int)
            public int n_sliders;                       // Number of sliders (unsigned int -> int)
            public int n_large_ticks;                  // Number of slider ticks and repeat points (unsigned int -> int)
            public int n_spinners;                      // Number of spinners (unsigned int -> int)
            public double stars;                        // Final star rating
            public int max_combo;                       // Maximum combo (unsigned int -> int)

            public static class ByReference extends OsuDifficultyAttributes implements Structure.ByReference {}
            public static class ByValue extends OsuDifficultyAttributes implements Structure.ByValue {}
        }

        @Structure.FieldOrder({ "difficulty", "pp", "pp_acc", "pp_aim",
            "pp_flashlight", "pp_speed", "effective_miss_count", "speed_deviation",
            "combo_based_estimated_miss_count", "score_based_estimated_miss_count",
            "aim_estimated_slider_breaks", "speed_estimated_slider_breaks" })
        public static class OsuPerformanceAttributes extends Structure {
            public OsuDifficultyAttributes difficulty; // Nested structure for difficulty attributes
            public double pp;                          // Final performance points
            public double pp_acc;                      // Accuracy portion of the final pp
            public double pp_aim;                      // Aim portion of the final pp
            public double pp_flashlight;               // Flashlight portion of the final pp
            public double pp_speed;                    // Speed portion of the final pp
            public double effective_miss_count;        // Misses including approximated slider breaks
            public Optionf64 speed_deviation;          // Approximated unstable-rate
            public double combo_based_estimated_miss_count;
            public Optionf64 score_based_estimated_miss_count;
            public double aim_estimated_slider_breaks;
            public double speed_estimated_slider_breaks;

            public static class ByReference extends OsuPerformanceAttributes implements Structure.ByReference {}
            public static class ByValue extends OsuPerformanceAttributes implements Structure.ByValue {}
        }

        @Structure.FieldOrder({ "stamina", "rhythm", "color", "reading",
            "great_hit_window", "ok_hit_window", "mono_stamina_factor",
            "mechanical_difficulty", "consistency_factor",
                "stars", "max_combo", "is_convert" })
        public static class TaikoDifficultyAttributes extends Structure {
            public double stamina;               // Difficulty of the stamina skill
            public double rhythm;                // Difficulty of the rhythm skill
            public double color;                 // Difficulty of the color skill
            public double reading;               // The difficulty of the reading skill.
            public double great_hit_window;      // Hit window for an n300 inclusive of mods
            public double ok_hit_window;         // Hit window for an n100 inclusive of mods
            public double mono_stamina_factor;   // Stamina difficulty ratio for mono-color streams
            public double mechanical_difficulty;
            public double consistency_factor;
            public double stars;                 // Final star rating
            public int max_combo;                // Maximum combo (unsigned int -> int)
            public boolean is_convert;           // Whether the beatmap is a convert (osu!standard)

            public static class ByReference extends TaikoDifficultyAttributes implements Structure.ByReference {}
            public static class ByValue extends TaikoDifficultyAttributes implements Structure.ByValue {}
        }

        @Structure.FieldOrder({ "difficulty", "pp", "pp_acc", "pp_difficulty",
            "estimated_unstable_rate" })
        public static class TaikoPerformanceAttributes extends Structure {
            public TaikoDifficultyAttributes difficulty;   // Difficulty attributes used for performance calculation
            public double pp;                              // Final performance points
            public double pp_acc;                          // Accuracy portion of the final pp
            public double pp_difficulty;                   // Strain portion of the final pp
            public Optionf64 estimated_unstable_rate;      // Estimated unstable rate (optional value)

            public static class ByReference extends TaikoPerformanceAttributes implements Structure.ByReference {}
            public static class ByValue extends TaikoPerformanceAttributes implements Structure.ByValue {}
        }

        @Structure.FieldOrder({ "stars", "preempt", "n_fruits", "n_droplets", "n_tiny_droplets", "is_convert" })
        public static class CatchDifficultyAttributes extends Structure {
            public double stars;        // Final star rating
            public double preempt;      // Time preempt (AR time window)
            public int n_fruits;        // Number of fruits (unsigned int -> use int in Java)
            public int n_droplets;      // Number of droplets (unsigned int -> use int in Java)
            public int n_tiny_droplets; // Number of tiny droplets (unsigned int -> use int in Java)
            public boolean is_convert;  // Whether the beatmap is a convert (bool)

            public static class ByReference extends CatchDifficultyAttributes implements Structure.ByReference {}
            public static class ByValue extends CatchDifficultyAttributes implements Structure.ByValue {}
        }

        @Structure.FieldOrder({ "difficulty", "pp" })
        public static class CatchPerformanceAttributes extends Structure {
            public CatchDifficultyAttributes difficulty; // Nested CatchDifficultyAttributes structure
            public double pp;                            // Final performance points

            public static class ByReference extends CatchPerformanceAttributes implements Structure.ByReference {}
            public static class ByValue extends CatchPerformanceAttributes implements Structure.ByValue {}
        }

        @Structure.FieldOrder({ "stars", "n_objects", "n_hold_notes", "max_combo", "is_convert" })
        public static class ManiaDifficultyAttributes extends Structure {
            public double stars;        // Final star rating
            public int n_objects;       // Number of hit objects (unsigned int -> int in Java)
            public int n_hold_notes;    // Number of hold notes (unsigned int -> int in Java)
            public int max_combo;       // Maximum achievable combo (unsigned int -> int in Java)
            public boolean is_convert;  // Whether the beatmap is a convert

            public static class ByReference extends ManiaDifficultyAttributes implements Structure.ByReference {}
            public static class ByValue extends ManiaDifficultyAttributes implements Structure.ByValue {}
        }

        @Structure.FieldOrder({ "difficulty", "pp", "pp_difficulty" })
        public static class ManiaPerformanceAttributes extends Structure {
            public ManiaDifficultyAttributes difficulty; // Nested ManiaDifficultyAttributes structure
            public double pp;                            // Final performance points
            public double pp_difficulty;                 // Difficulty portion of the final pp

            public static class ByReference extends ManiaPerformanceAttributes implements Structure.ByReference {}
            public static class ByValue extends ManiaPerformanceAttributes implements Structure.ByValue {}
        }

        @Structure.FieldOrder({ "t", "is_some" })
        public static class OptionOsuDifficultyAttributes extends Structure {
            public OsuDifficultyAttributes t;     // Element that is maybe valid
            public byte is_some;                  // 1 means element t is valid

            public static class ByReference extends OptionOsuDifficultyAttributes implements Structure.ByReference {}
            public static class ByValue extends OptionOsuDifficultyAttributes implements Structure.ByValue {}

            public Optional<OsuDifficultyAttributes> toOptional() {
                return is_some == 1 ? Optional.of(t) : Optional.empty();
            }
        }

        @Structure.FieldOrder({ "t", "is_some" })
        public static class OptionTaikoDifficultyAttributes extends Structure {
            public TaikoDifficultyAttributes t;     // Element that is maybe valid
            public byte is_some;                  // 1 means element t is valid

            public static class ByReference extends OptionTaikoDifficultyAttributes implements Structure.ByReference {}
            public static class ByValue extends OptionTaikoDifficultyAttributes implements Structure.ByValue {}

            public Optional<TaikoDifficultyAttributes> toOptional() {
                return is_some == 1 ? Optional.of(t) : Optional.empty();
            }
        }

        @Structure.FieldOrder({ "t", "is_some" })
        public static class OptionCatchDifficultyAttributes extends Structure {
            public CatchDifficultyAttributes t;     // Element that is maybe valid
            public byte is_some;                  // 1 means element t is valid

            public static class ByReference extends OptionCatchDifficultyAttributes implements Structure.ByReference {}
            public static class ByValue extends OptionCatchDifficultyAttributes implements Structure.ByValue {}

            public Optional<CatchDifficultyAttributes> toOptional() {
                return is_some == 1 ? Optional.of(t) : Optional.empty();
            }
        }

        @Structure.FieldOrder({ "t", "is_some" })
        public static class OptionManiaDifficultyAttributes extends Structure {
            public ManiaDifficultyAttributes t;     // Element that is maybe valid
            public byte is_some;                  // 1 means element t is valid

            public static class ByReference extends OptionManiaDifficultyAttributes implements Structure.ByReference {}
            public static class ByValue extends OptionManiaDifficultyAttributes implements Structure.ByValue {}

            public Optional<ManiaDifficultyAttributes> toOptional() {
                return is_some == 1 ? Optional.of(t) : Optional.empty();
            }
        }

        @Structure.FieldOrder({ "osu", "taiko", "fruit", "mania", "mode" })
        public static class DifficultyAttributes extends Structure {
            public OptionOsuDifficultyAttributes osu;   // Option for osu!difficulty attributes
            public OptionTaikoDifficultyAttributes taiko; // Option for taiko difficulty attributes
            public OptionCatchDifficultyAttributes fruit; // Option for catch difficulty attributes
            public OptionManiaDifficultyAttributes mania; // Option for mania difficulty attributes
            public int mode;                            // Mode enum (osu!, taiko, catch, mania)

            public static class ByReference extends DifficultyAttributes implements Structure.ByReference {}
            public static class ByValue extends DifficultyAttributes implements Structure.ByValue {}
        }

        @Structure.FieldOrder({ "t", "is_some" })
        public static class OptionOsuPerformanceAttributes extends Structure {
            public OsuPerformanceAttributes t;     // Element that is maybe valid
            public byte is_some;                  // 1 means element t is valid

            public static class ByReference extends OptionOsuPerformanceAttributes implements Structure.ByReference {}
            public static class ByValue extends OptionOsuPerformanceAttributes implements Structure.ByValue {}

            public Optional<OsuPerformanceAttributes> toOptional() {
                return is_some == 1 ? Optional.of(t) : Optional.empty();
            }
        }

        @Structure.FieldOrder({ "t", "is_some" })
        public static class OptionTaikoPerformanceAttributes extends Structure {
            public TaikoPerformanceAttributes t;     // Element that is maybe valid
            public byte is_some;                  // 1 means element t is valid

            public static class ByReference extends OptionTaikoPerformanceAttributes implements Structure.ByReference {}
            public static class ByValue extends OptionTaikoPerformanceAttributes implements Structure.ByValue {}

            public Optional<TaikoPerformanceAttributes> toOptional() {
                return is_some == 1 ? Optional.of(t) : Optional.empty();
            }
        }

        @Structure.FieldOrder({ "t", "is_some" })
        public static class OptionCatchPerformanceAttributes extends Structure {
            public CatchPerformanceAttributes t;     // Element that is maybe valid
            public byte is_some;                  // 1 means element t is valid

            public static class ByReference extends OptionCatchPerformanceAttributes implements Structure.ByReference {}
            public static class ByValue extends OptionCatchPerformanceAttributes implements Structure.ByValue {}

            public Optional<CatchPerformanceAttributes> toOptional() {
                return is_some == 1 ? Optional.of(t) : Optional.empty();
            }
        }

        @Structure.FieldOrder({ "t", "is_some" })
        public static class OptionManiaPerformanceAttributes extends Structure {
            public ManiaPerformanceAttributes t;     // Element that is maybe valid
            public byte is_some;                  // 1 means element t is valid

            public static class ByReference extends OptionManiaPerformanceAttributes implements Structure.ByReference {}
            public static class ByValue extends OptionManiaPerformanceAttributes implements Structure.ByValue {}

            public Optional<ManiaPerformanceAttributes> toOptional() {
                return is_some == 1 ? Optional.of(t) : Optional.empty();
            }
        }

        @Structure.FieldOrder({ "osu", "taiko", "fruit", "mania", "mode" })
        public static class PerformanceAttributes extends Structure {
            public OptionOsuPerformanceAttributes osu;   // Option for osu!difficulty attributes
            public OptionTaikoPerformanceAttributes taiko; // Option for taiko difficulty attributes
            public OptionCatchPerformanceAttributes fruit; // Option for catch difficulty attributes
            public OptionManiaPerformanceAttributes mania; // Option for mania difficulty attributes
            public int mode;                            // Mode enum (osu!, taiko, catch, mania)

            public static class ByReference extends PerformanceAttributes implements Structure.ByReference {}
            public static class ByValue extends PerformanceAttributes implements Structure.ByValue {}
        }

        @Structure.FieldOrder({ "ar", "od_perfect", "od_great", "od_good", "od_ok", "od_meh" })
        public static class HitWindows extends Structure {
            /// Hit window for approach rate i.e. `TimePreempt` in milliseconds.
            public Optionf64 ar;
            /// Hit window for overall difficulty i.e. time to hit a "Perfect" in milliseconds.
            public Optionf64 od_perfect;
            /// Hit window for overall difficulty i.e. time to hit a 300 ("Great") in milliseconds.
            public Optionf64 od_great;
            /// Hit window for overall difficulty i.e. time to hit a "Good" in milliseconds.
            public Optionf64 od_good;
            /// Hit window for overall difficulty i.e. time to hit a 100 ("Ok") in milliseconds.
            public Optionf64 od_ok;
            /// Hit window for overall difficulty i.e. time to hit a 50 ("Meh") in milliseconds.
            public Optionf64 od_meh;

            public static class ByReference extends HitWindows implements Structure.ByReference {}
            public static class ByValue extends HitWindows implements Structure.ByValue {}
        }

        @Structure.FieldOrder({ "ar", "od", "cs", "hp", "clock_rate", "hit_windows" })
        public static class BeatmapAttributes extends Structure {
            public double ar;         // Approach rate
            public double od;         // Overall difficulty
            public double cs;         // Circle size
            public double hp;         // Health drain rate
            public double clock_rate; // Clock rate with respect to mods
            public HitWindows hit_windows; // Nested hit windows structure

            public static class ByReference extends BeatmapAttributes implements Structure.ByReference {}
            public static class ByValue extends BeatmapAttributes implements Structure.ByValue {}
        }

        @Structure.FieldOrder({ "max_combo", "osu_large_tick_hits", "osu_small_tick_hits", "slider_end_hits",
            "n_geki", "n_katu", "n300", "n100", "n50", "misses", "legacy_total_score" })
        public static class ScoreState extends Structure {
            public int max_combo;            // Maximum combo (unsigned int -> int)
            /// "Large tick" hits for osu!standard.
            ///
            /// The meaning depends on the kind of score:
            /// - if set on osu!stable, this field is irrelevant and can be `0`
            /// - if set on osu!lazer *without* `CL`, this field is the amount of hit
            ///   slider ticks and repeats
            /// - if set on osu!lazer *with* `CL`, this field is the amount of hit
            ///   slider heads, ticks, and repeats
            ///
            /// Only relevant for osu!lazer.
            public int osu_large_tick_hits;
            /// "Small ticks" hits for osu!standard.
            ///
            /// These are essentially the slider end hits for lazer scores without
            /// slider accuracy.
            ///
            /// Only relevant for osu!lazer.
            public int osu_small_tick_hits;
            /// Amount of successfully hit slider ends.
            ///
            /// Only relevant for osu!standard in lazer.
            public int slider_end_hits;
            public int n_geki;               // Current gekis (unsigned int -> int)
            public int n_katu;               // Current katus (unsigned int -> int)
            public int n300;                 // Current 300s (unsigned int -> int)
            public int n100;                 // Current 100s (unsigned int -> int)
            public int n50;                  // Current 50s (unsigned int -> int)
            public int misses;               // Current misses (unsigned int -> int)
            public Optionu32 legacy_total_score;

            public static class ByReference extends ScoreState implements Structure.ByReference {}
            public static class ByValue extends ScoreState implements Structure.ByValue {}
        }
    }

    public static class Beatmap implements AutoCloseable {
        private final PointerByReference _context;  // The context of the Beatmap

        // Load the Beatmap from bytes
        public Beatmap(byte[] data) throws FFIException {
            _context = new PointerByReference();  // Initialize _context to a valid Pointer
            ByteBuffer buffer = ByteBuffer.allocateDirect(data.length);
            buffer.put(data);
            buffer.flip();
            var sliceu8 = new RosuPPLib.Sliceu8(buffer);
            int rval = RosuPPLib.beatmap_from_bytes(_context, sliceu8);
            if (rval != FFIError.Ok) {
                throw new FFIException("Error loading beatmap from bytes", rval);
            }
        }

        public Beatmap(RosuPPLib.Sliceu8 data) throws FFIException {
            _context = new PointerByReference();  // Initialize _context to a valid Pointer
            int rval = RosuPPLib.beatmap_from_bytes(_context, data);
            if (rval != FFIError.Ok) {
                throw new FFIException("Error loading beatmap from bytes", rval);
            }
        }


        // Load the Beatmap from a file path
        public Beatmap(String path) throws FFIException {
            _context = new PointerByReference();  // Initialize _context to a valid Pointer
            int rval = RosuPPLib.beatmap_from_path(_context, path);
            if (rval != FFIError.Ok) {
                throw new FFIException("Error loading beatmap from path", rval);
            }
        }

        // Convert the Beatmap to the specified mode
        public boolean convert(Mode mode, Mods mods) {
            return RosuPPLib.beatmap_convert(getContext(), mode.getValue(), mods.getContext());
        }

        // Convert the Beatmap to the specified mode
        public boolean convert(Mode mode) throws FFIException {
            var mods = Mods.New(mode);
            return RosuPPLib.beatmap_convert(getContext(), mode.getValue(), mods.getContext());
        }

        // Get the BPM of the Beatmap
        public double bpm() {
            return RosuPPLib.beatmap_bpm(getContext());
        }

        // Get the total break time of the Beatmap
        public double totalBreakTime() {
            return RosuPPLib.beatmap_total_break_time(getContext());
        }

        // Get the mode of the Beatmap
        public Mode mode() {
            return Mode.fromValue(RosuPPLib.beatmap_mode(getContext()));
        }

        // Check if the Beatmap is a converted map
        public boolean isConvert() {
            return RosuPPLib.beatmap_is_convert(getContext());
        }

        // Getter for the context
        public Pointer getContext() {
            return _context.getValue();
        }

        // Dispose method (releases the resources)
        @Override
        public void close() throws FFIException {
            int rval = RosuPPLib.beatmap_destroy(_context);
            if (rval != 0) {
                throw new FFIException("Error destroying beatmap", rval);
            }
        }
    }

    public static class BeatmapAttributesBuilder implements AutoCloseable {
        private final PointerByReference _context; // Context for BeatmapAttributesBuilder

        public BeatmapAttributesBuilder() throws FFIException {
            _context = new PointerByReference();
            int rval = RosuPPLib.beatmap_attributes_new(_context);
            if (rval != FFIError.Ok) {
                throw new FFIException("Error creating BeatmapAttributesBuilder", rval);
            }
        }

        // Method to dispose of the builder
        @Override
        public void close() throws FFIException {
            int rval = RosuPPLib.beatmap_attributes_destroy(_context);
            if (rval != FFIError.Ok) {
                throw new FFIException("Error destroying BeatmapAttributesBuilder", rval);
            }
        }

        // Method to set the mode
        public void setMode(Mode mode) {
            RosuPPLib.beatmap_attributes_mode(getContext(), mode.getValue());
        }

        // Method to set mods (using IntPtr)
        public void setMods(Mods mods) {
            RosuPPLib.beatmap_attributes_p_mods(getContext(), mods.getContext());
        }

        // Method to set mods (using uint)
        public void setMods(int mods) {
            RosuPPLib.beatmap_attributes_i_mods(getContext(), mods);
        }

        // Method to set mods (using string)
        public void setMods(String str) throws FFIException {
            int rval = RosuPPLib.beatmap_attributes_s_mods(getContext(), str);
            if (rval != FFIError.Ok) {
                throw new FFIException("Error setting string mods", rval);
            }
        }

        // Method to set clock rate
        public void setClockRate(double clockRate) {
            RosuPPLib.beatmap_attributes_clock_rate(getContext(), clockRate);
        }

        // Method to set AR (approach rate)
        public void setAr(float ar) {
            RosuPPLib.beatmap_attributes_ar(getContext(), ar);
        }

        // Method to set CS (circle size)
        public void setCs(float cs) {
            RosuPPLib.beatmap_attributes_cs(getContext(), cs);
        }

        // Method to set HP (health drain rate)
        public void setHp(float hp) {
            RosuPPLib.beatmap_attributes_hp(getContext(), hp);
        }

        // Method to set OD (overall difficulty)
        public void setOd(float od) {
            RosuPPLib.beatmap_attributes_od(getContext(), od);
        }

        // Method to get the clock rate
        public double getClockRate() {
            return RosuPPLib.beatmap_attributes_get_clock_rate(getContext());
        }

        // Method to build BeatmapAttributes
        public RosuPPLib.BeatmapAttributes build(Beatmap beatmap) {
            return RosuPPLib.beatmap_attributes_build(getContext(), beatmap.getContext());
        }

        // Getter for the context
        public Pointer getContext() {
            return _context.getValue();
        }
    }

    public static class Difficulty implements AutoCloseable {
        private final PointerByReference _context;

        public Difficulty() throws FFIException {
            _context = new PointerByReference();
            int rval = RosuPPLib.difficulty_new(_context);
            if (rval != 0) {
                throw new FFIException("Error creating Difficulty", rval);
            }
        }

        // Method to dispose of the Difficulty
        @Override
        public void close() throws FFIException {
            int rval = RosuPPLib.difficulty_destroy(_context);
            if (rval != 0) {
                throw new FFIException("Error destroying Difficulty", rval);
            }
        }

        // Method to set p_mods (using Pointer)
        public void setMods(Mods mods) {
            RosuPPLib.difficulty_p_mods(getContext(), mods.getContext());
        }

        // Method to set i_mods (using uint)
        public void setMods(int mods) {
            RosuPPLib.difficulty_i_mods(getContext(), mods);
        }

        // Method to set s_mods (using string)
        public void setMods(String str) throws FFIException {
            int rval = RosuPPLib.difficulty_s_mods(getContext(), str);
            if (rval != 0) {
                throw new FFIException("Error setting string mods", rval);
            }
        }

        // Method to set passed objects (using uint)
        public void setPassedObjects(int passedObjects) {
            RosuPPLib.difficulty_passed_objects(getContext(), passedObjects);
        }

        // Method to set clock rate
        public void setClockRate(double clockRate) {
            RosuPPLib.difficulty_clock_rate(getContext(), clockRate);
        }

        // Method to set AR (approach rate)
        public void setAr(float ar) {
            RosuPPLib.difficulty_ar(getContext(), ar);
        }

        // Method to set CS (circle size)
        public void setCs(float cs) {
            RosuPPLib.difficulty_cs(getContext(), cs);
        }

        // Method to set HP (health drain)
        public void setHp(float hp) {
            RosuPPLib.difficulty_hp(getContext(), hp);
        }

        // Method to set OD (overall difficulty)
        public void setOd(float od) {
            RosuPPLib.difficulty_od(getContext(), od);
        }

        // Method to set hardrock offsets
        public void setHardrockOffsets(boolean hardrockOffsets) {
            RosuPPLib.difficulty_hardrock_offsets(getContext(), hardrockOffsets);
        }

        // Method to set lazer
        public void setLazer(boolean lazer) {
            RosuPPLib.difficulty_lazer(getContext(), lazer);
        }

        // Method to calculate DifficultyAttributes from beatmap
        public RosuPPLib.DifficultyAttributes calculate(Beatmap beatmap) {
            return RosuPPLib.difficulty_calculate(getContext(), beatmap.getContext());
        }

        // Method to get clock rate
        public double getClockRate() {
            return RosuPPLib.difficulty_get_clock_rate(getContext());
        }

        // Getter for context
        public Pointer getContext() {
            return _context.getValue();
        }
    }

    public static class Performance implements AutoCloseable {
        private final PointerByReference _context;

        public Performance() throws FFIException {
            _context = new PointerByReference();
            int rval = RosuPPLib.performance_new(_context);
            if (rval != 0) {
                throw new FFIException("Error creating Performance", rval);
            }
        }

        // Method to dispose of the Performance
        @Override
        public void close() throws FFIException {
            int rval = RosuPPLib.performance_destroy(_context);
            if (rval != 0) {
                throw new FFIException("Error destroying Performance", rval);
            }
        }

        // Method to set mode
        public void setMode(Mode mode) {
            RosuPPLib.performance_mode(getContext(), mode.getValue());
        }

        // Method to set p_mods (using Pointer)
        public void setMods(Mods mods) {
            RosuPPLib.performance_p_mods(getContext(), mods.getContext());
        }

        // Method to set i_mods (using uint)
        public void setMods(int mods) {
            RosuPPLib.performance_i_mods(getContext(), mods);
        }

        // Method to set s_mods (using string)
        public void setMods(String str) throws FFIException {
            int rval = RosuPPLib.performance_s_mods(getContext(), str);
            if (rval != 0) {
                throw new FFIException("Error setting string mods", rval);
            }
        }

        // Method to set passed objects (using uint)
        public void setPassedObjects(int passedObjects) {
            RosuPPLib.performance_passed_objects(getContext(), passedObjects);
        }

        // Method to set clock rate
        public void setClockRate(double clockRate) {
            RosuPPLib.performance_clock_rate(getContext(), clockRate);
        }

        // Method to set AR (approach rate)
        public void setAr(float ar) {
            RosuPPLib.performance_ar(getContext(), ar);
        }

        // Method to set CS (circle size)
        public void setCs(float cs) {
            RosuPPLib.performance_cs(getContext(), cs);
        }

        // Method to set HP (health drain)
        public void setHp(float hp) {
            RosuPPLib.performance_hp(getContext(), hp);
        }

        // Method to set OD (overall difficulty)
        public void setOd(float od) {
            RosuPPLib.performance_od(getContext(), od);
        }

        // Method to set hardrock offsets
        public void setHardrockOffsets(boolean hardrockOffsets) {
            RosuPPLib.performance_hardrock_offsets(getContext(), hardrockOffsets);
        }

        // Method to set hardrock offsets
        public void setHitResultPriority(HitResultPriority hitresult_priority) {
            RosuPPLib.performance_hitresult_priority(getContext(), hitresult_priority.value);
        }

        public void setCombo(long combo) {
            RosuPPLib.performance_combo(getContext(), combo);
        }

        public void setState(RosuPPLib.ScoreState state) {
            RosuPPLib.performance_state(getContext(), (RosuPPLib.ScoreState.ByValue)state);
        }

        public void setAccuracy(double accuracy) {
            RosuPPLib.performance_accuracy(getContext(), accuracy);
        }

        public void setMisses(long misses) {
            RosuPPLib.performance_misses(getContext(), misses);
        }

        public void setLargeTickHits(long largeTickHits) {
            RosuPPLib.performance_large_tick_hits(getContext(), largeTickHits);
        }

        public void setSmallTickHits(long smallTickHits) {
            RosuPPLib.performance_small_tick_hits(getContext(), smallTickHits);
        }


        public void setSliderEndHits(long sliderEndHits) {
            RosuPPLib.performance_slider_end_hits(getContext(), sliderEndHits);
        }

        public void setN300(long n300) {
            RosuPPLib.performance_n300(getContext(), n300);
        }

        public void setN100(long n100) {
            RosuPPLib.performance_n100(getContext(), n100);
        }

        public void setN50(long n50) {
            RosuPPLib.performance_n50(getContext(), n50);
        }

        public void setNKatu(long nKatu) {
            RosuPPLib.performance_n_katu(getContext(), nKatu);
        }

        public void setNGeki(long nGeki) {
            RosuPPLib.performance_n_geki(getContext(), nGeki);
        }

        // Method to set lazer
        public void setLazer(boolean lazer) {
            RosuPPLib.performance_lazer(getContext(), lazer);
        }

        public RosuPPLib.ScoreState generateState(Beatmap beatmap) {
            return RosuPPLib.performance_generate_state(getContext(), beatmap.getContext());
        }

        public RosuPPLib.ScoreState generateStateFromDifficulty(RosuPPLib.DifficultyAttributes difficultyAttributes) {
            return RosuPPLib.performance_generate_state_from_difficulty(getContext(), (RosuPPLib.DifficultyAttributes.ByValue)difficultyAttributes);
        }

        // Method to calculate PerformanceAttributes from beatmap
        public RosuPPLib.PerformanceAttributes calculate(Beatmap beatmap) {
            return RosuPPLib.performance_calculate(getContext(), beatmap.getContext());
        }

        // Method to calculate PerformanceAttributes from DifficultyAttributes
        public RosuPPLib.PerformanceAttributes calculateFromDifficulty(RosuPPLib.DifficultyAttributes difficultyAttributes) {
            return RosuPPLib.performance_calculate_from_difficulty(getContext(), (RosuPPLib.DifficultyAttributes.ByValue)difficultyAttributes);
        }

        // Method to get clock rate
        public double getClockRate() {
            return RosuPPLib.performance_get_clock_rate(getContext());
        }

        // Getter for context
        public Pointer getContext() {
            return _context.getValue();
        }
    }

    public static class GradualDifficulty {
        @SuppressWarnings("unused")
        protected final Cleaner.Cleanable cleanable;
        private final PointerByReference _context; // Context for BeatmapAttributesBuilder

        private GradualDifficulty() {
            _context = new PointerByReference();
            this.cleanable = cleaner.register(this, cleanAction(_context));
        }

        private static Runnable cleanAction(final PointerByReference context) {
            return () -> {
                int rval = RosuPPLib.gradual_difficulty_destroy(context);
                if (rval != FFIError.Ok) {
                    try {
                        throw new FFIException("Error destroying GradualDifficulty", rval);
                    } catch (FFIException e) {
                        throw new RuntimeException(e);
                    }
                }
            };
        }

        /// Create a [`GradualDifficulty`] for a map of any mode.
        public static GradualDifficulty New(Difficulty difficulty, Beatmap beatmap) throws FFIException {
            var m = new GradualDifficulty();
            int rval = RosuPPLib.gradual_difficulty_new(m._context, difficulty.getContext(), beatmap.getContext());
            if (rval != FFIError.Ok) {
                throw new FFIException("Error creating GradualDifficulty", rval);
            }
            return m;
        }

        /// Create a [`GradualDifficulty`] for a [`Beatmap`] on a specific [`GameMode`].
        public static GradualDifficulty NewWithMode(Difficulty difficulty, Beatmap beatmap, Mode mode) throws FFIException {
            var m = new GradualDifficulty();
            int rval = RosuPPLib.gradual_difficulty_new_with_mode(m._context, difficulty.getContext(), beatmap.getContext(), mode.getValue());
            if (rval != FFIError.Ok) {
                throw new FFIException("Error creating GradualDifficulty", rval);
            }
            return m;
        }

        public RosuPPLib.OptionDifficultyAttributes Next() {
            return RosuPPLib.gradual_difficulty_next(getContext());
        }

        public RosuPPLib.OptionDifficultyAttributes Nth(long n) {
            return RosuPPLib.gradual_difficulty_nth(getContext(), n);
        }

        public long Len() {
            return RosuPPLib.gradual_difficulty_len(getContext());
        }

        // Getter for the context
        public Pointer getContext() {
            return _context.getValue();
        }
    }

    public static class GradualPerformance {
        @SuppressWarnings("unused")
        protected final Cleaner.Cleanable cleanable;
        private final PointerByReference _context; // Context for BeatmapAttributesBuilder

        private GradualPerformance() {
            _context = new PointerByReference();
            this.cleanable = cleaner.register(this, cleanAction(_context));
        }

        private static Runnable cleanAction(final PointerByReference context) {
            return () -> {
                int rval = RosuPPLib.gradual_performance_destroy(context);
                if (rval != FFIError.Ok) {
                    try {
                        throw new FFIException("Error destroying GradualPerformance", rval);
                    } catch (FFIException e) {
                        throw new RuntimeException(e);
                    }
                }
            };
        }

        /// Create a [`GradualDifficulty`] for a map of any mode.
        public static GradualPerformance New(Difficulty difficulty, Beatmap beatmap) throws FFIException {
            var m = new GradualPerformance();
            int rval = RosuPPLib.gradual_performance_new(m._context, difficulty.getContext(), beatmap.getContext());
            if (rval != FFIError.Ok) {
                throw new FFIException("Error creating GradualPerformance", rval);
            }
            return m;
        }

        /// Create a [`GradualDifficulty`] for a [`Beatmap`] on a specific [`GameMode`].
        public static GradualPerformance NewWithMode(Difficulty difficulty, Beatmap beatmap, Mode mode) throws FFIException {
            var m = new GradualPerformance();
            int rval = RosuPPLib.gradual_performance_new_with_mode(m._context, difficulty.getContext(), beatmap.getContext(), mode.getValue());
            if (rval != FFIError.Ok) {
                throw new FFIException("Error creating GradualPerformance", rval);
            }
            return m;
        }

        public RosuPPLib.OptionPerformanceAttributes Next(RosuPPLib.ScoreState state) {
            return RosuPPLib.gradual_performance_next(getContext(), (RosuPPLib.ScoreState.ByValue)state);
        }

        public RosuPPLib.OptionPerformanceAttributes Last(RosuPPLib.ScoreState state) {
            return RosuPPLib.gradual_performance_last(getContext(), (RosuPPLib.ScoreState.ByValue)state);
        }

        public RosuPPLib.OptionPerformanceAttributes Nth(long n, RosuPPLib.ScoreState state) {
            return RosuPPLib.gradual_performance_nth(getContext(), (RosuPPLib.ScoreState.ByValue)state, n);
        }

        public long Len() {
            return RosuPPLib.gradual_performance_len(getContext());
        }

        // Getter for the context
        public Pointer getContext() {
            return _context.getValue();
        }
    }

    public static class Mods {
        @SuppressWarnings("unused")
        protected final Cleaner.Cleanable cleanable;
        private final PointerByReference _context; // Context for BeatmapAttributesBuilder

        private Mods() {
            _context = new PointerByReference();
            this.cleanable = cleaner.register(this, cleanAction(_context));
        }

        private static Runnable cleanAction(final PointerByReference context) {
            return () -> {
                int rval = RosuPPLib.mods_destroy(context);
                if (rval != FFIError.Ok) {
                    try {
                        throw new FFIException("Error destroying Mods", rval);
                    } catch (FFIException e) {
                        throw new RuntimeException(e);
                    }
                }
            };
        }

        /// new
        public static Mods New(Mode mode) throws FFIException {
            var m = new Mods();
            int rval = RosuPPLib.mods_new(m._context, mode.getValue());
            if (rval != FFIError.Ok) {
                throw new FFIException("Error creating Mods", rval);
            }
            return m;
        }

        /// from acronyms
        public static Mods fromAcronyms(String mods, Mode mode) throws FFIException {
            var m = new Mods();
            int rval = RosuPPLib.mods_from_acronyms(m._context, mods, mode.getValue());
            if (rval != FFIError.Ok) {
                throw new FFIException("Error creating Mods", rval);
            }
            return m;
        }

        /// from bits
        public static Mods fromBits(long mods, Mode mode) throws FFIException {
            var m = new Mods();
            int rval = RosuPPLib.mods_from_bits(m._context, mods, mode.getValue());
            if (rval != FFIError.Ok) {
                throw new FFIException("Error creating Mods", rval);
            }
            return m;
        }

        /// from json
        public static Mods fromJson(String mods, Mode mode, boolean deny_unknown_fields) throws FFIException {
            var m = new Mods();
            int rval = RosuPPLib.mods_from_json(m._context, mods, mode.getValue(), deny_unknown_fields);
            if (rval != FFIError.Ok) {
                throw new FFIException("Error creating Mods", rval);
            }
            return m;
        }

        public void removeUnknownMods() {
            RosuPPLib.mods_remove_unknown_mods(getContext());
        }

        public void sanitize() {
            RosuPPLib.mods_sanitize(getContext());
        }

        public long getBits() {
            return RosuPPLib.mods_bits(getContext());
        }

        public long getLength() {
            return RosuPPLib.mods_len(getContext());
        }

        public OwnedString toJson() throws FFIException {
            var s = new OwnedString();
            RosuPPLib.mods_json(getContext(), s.getContext());
            return s;
        }

        public boolean insertJson(String mod, boolean deny_unknown_fields) {
            return RosuPPLib.mods_insert_json(getContext(), mod, deny_unknown_fields);
        }

        public boolean insert(String mod) {
            return RosuPPLib.mods_insert(getContext(), mod);
        }

        public boolean contains(String mod) {
            return RosuPPLib.mods_contains(getContext(), mod);
        }

        public void clear() {
            RosuPPLib.mods_clear(getContext());
        }

        public RosuPPLib.Optionf64 getClockRate() {
            return RosuPPLib.mods_clock_rate(getContext());
        }

        // Getter for the context
        public Pointer getContext() {
            return _context.getValue();
        }
    }


    public static class OwnedString {

        @SuppressWarnings("unused")
        private final Cleaner.Cleanable cleanable;
        private final PointerByReference _context; // Context for BeatmapAttributesBuilder

        public OwnedString() throws FFIException {
            _context = new PointerByReference();
            int rval = RosuPPLib.string_empty(_context);
            if (rval != FFIError.Ok) {
                throw new FFIException("Error creating OwnedString", rval);
            }
            this.cleanable = cleaner.register(this, cleanAction(_context));
        }

        public OwnedString(String str) throws FFIException {
            _context = new PointerByReference();
            int rval = RosuPPLib.string_from_c_str(_context, str);
            if (rval != FFIError.Ok) {
                throw new FFIException("Error creating OwnedString", rval);
            }
            this.cleanable = cleaner.register(this, cleanAction(_context));
        }

        private static Runnable cleanAction(final PointerByReference context) {
            return () -> {
                int rval = RosuPPLib.string_destroy(context);
                if (rval != FFIError.Ok) {
                    try {
                        throw new FFIException("Error destroying Mods", rval);
                    } catch (FFIException e) {
                        throw new RuntimeException(e);
                    }
                }
            };
        }

        public String toCstr() {
            return RosuPPLib.string_to_cstr(getContext());
        }

        public boolean isInit() {
            return RosuPPLib.string_is_init(getContext());
        }

        public String toString() {
            return isInit() ? toCstr() : null;
        }

        // Getter for the context
        public Pointer getContext() {
            return _context.getValue();
        }
    }

    public static OwnedString debugDifficyltyAttributes(RosuPPLib.DifficultyAttributes attr) throws FFIException {
        var s = new OwnedString();
        RosuPPLib.debug_difficylty_attributes(attr, s.getContext());
        return s;
    }

    public static OwnedString debugPerformanceAttributes(RosuPPLib.PerformanceAttributes attr) throws FFIException {
        var s = new OwnedString();
        RosuPPLib.debug_performance_attributes(attr, s.getContext());
        return s;
    }

    public static OwnedString debugScoreState(RosuPPLib.ScoreState attr) throws FFIException {
        var s = new OwnedString();
        RosuPPLib.debug_score_state(attr, s.getContext());
        return s;
    }

    public static double calculateAccuacy(RosuPPLib.ScoreState state, RosuPPLib.DifficultyAttributes attr, OsuScoreOrigin origin) {
        return RosuPPLib.calculate_accuacy(state, attr, origin.value);
    }

    public static class FFIException extends Exception {
        public int code;
        public FFIException(String message, int code) {
            super(message + ", code: " + code);
            this.code = code;
        }
    }
}
