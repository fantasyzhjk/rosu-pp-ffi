import java.lang.ref.Cleaner;
import java.util.Optional;

import com.sun.jna.Library;
import com.sun.jna.Memory;
import com.sun.jna.Native;
import com.sun.jna.Pointer;
import com.sun.jna.Structure;
import com.sun.jna.ptr.PointerByReference;

public class RosuFFI {
    
    public interface HitResultPriority {
        int BestCase = 0;
        int WorstCase = 1;
    }

    public interface ModeInt {
        /// osu!standard
        int Osu = 0;
        /// osu!taiko
        int Taiko = 1;
        /// osu!catch
        int Catch = 2;
        /// osu!mania
        int Mania = 3;
    }

    public interface FFIError {
        int Ok = 0;
        int Null = 100;
        int Panic = 200;
        int ParseError = 300;
        int InvalidString = 400;
        int SerializeError = 500;
        int Unknown = 1000;
    }

    public interface RosuPPLib extends Library {

        // JNA 为 dll 名称
        RosuPPLib INSTANCE = Native.load("rosu_pp_ffi", RosuPPLib.class);

        /// Destroys the given instance.
        ///
        /// # Safety
        ///
        /// The passed parameter MUST have been created with the corresponding init function;
        /// passing any other value results in undefined behavior.
        int beatmap_attributes_destroy(PointerByReference context);

        int beatmap_attributes_new(PointerByReference context);

        void beatmap_attributes_mode(Pointer context, int mode);

        void beatmap_attributes_p_mods(Pointer context, Pointer mods);

        void beatmap_attributes_i_mods(Pointer context, long mods);

        int beatmap_attributes_s_mods(Pointer context, String str);

        void beatmap_attributes_clock_rate(Pointer context, double clock_rate);

        void beatmap_attributes_ar(Pointer context, float ar);

        void beatmap_attributes_cs(Pointer context, float cs);

        void beatmap_attributes_hp(Pointer context, float hp);

        void beatmap_attributes_od(Pointer context, float od);

        double beatmap_attributes_get_clock_rate(Pointer context);

        BeatmapAttributes.ByValue beatmap_attributes_build(Pointer context, Pointer beatmap);

        /// Destroys the given instance.
        ///
        /// # Safety
        ///
        /// The passed parameter MUST have been created with the corresponding init function;
        /// passing any other value results in undefined behavior.
        int beatmap_destroy(PointerByReference context);

        int beatmap_from_bytes(PointerByReference context, Sliceu8 data);

        int beatmap_from_path(PointerByReference context, String path);

        /// Convert a Beatmap to the specified mode
        boolean beatmap_convert(Pointer context, int mode);

        double beatmap_bpm(Pointer context);

        double beatmap_total_break_time(Pointer context);

        int beatmap_mode(Pointer context);

        boolean beatmap_is_convert(Pointer context);

        /// Destroys the given instance.
        ///
        /// # Safety
        ///
        /// The passed parameter MUST have been created with the corresponding init function;
        /// passing any other value results in undefined behavior.
        int difficulty_destroy(PointerByReference context);

        int difficulty_new(PointerByReference context);

        void difficulty_p_mods(Pointer context, Pointer mods);

        void difficulty_i_mods(Pointer context, long mods);

        int difficulty_s_mods(Pointer context, String str);

        void difficulty_passed_objects(Pointer context, long passed_objects);

        void difficulty_clock_rate(Pointer context, double clock_rate);

        void difficulty_ar(Pointer context, float ar);

        void difficulty_cs(Pointer context, float cs);

        void difficulty_hp(Pointer context, float hp);

        void difficulty_od(Pointer context, float od);

        void difficulty_hardrock_offsets(Pointer context, boolean hardrock_offsets);

        void difficulty_lazer(Pointer context, boolean lazer);

        DifficultyAttributes.ByValue difficulty_calculate(Pointer context, Pointer beatmap);

        double difficulty_get_clock_rate(Pointer context);

        /// Destroys the given instance.
        ///
        /// # Safety
        ///
        /// The passed parameter MUST have been created with the corresponding init function;
        /// passing any other value results in undefined behavior.
        int performance_destroy(PointerByReference context);

        int performance_new(PointerByReference context);

        void performance_mode(Pointer context, int mode);

        void performance_p_mods(Pointer context, Pointer mods);

        void performance_i_mods(Pointer context, long mods);

        int performance_s_mods(Pointer context, String str);

        void performance_passed_objects(Pointer context, long passed_objects);

        void performance_clock_rate(Pointer context, double clock_rate);

        void performance_ar(Pointer context, float ar);

        void performance_cs(Pointer context, float cs);

        void performance_hp(Pointer context, float hp);

        void performance_od(Pointer context, float od);

        void performance_hardrock_offsets(Pointer context, boolean hardrock_offsets);

        void performance_accuracy(Pointer context, double accuracy);

        void performance_misses(Pointer context, long misses);

        void performance_combo(Pointer context, long combo);

        void performance_hitresult_priority(Pointer context, int hitresult_priority);

        void performance_lazer(Pointer context, boolean lazer);

        void performance_slider_tick_hits(Pointer context, long slider_tick_hits);

        void performance_slider_tick_misses(Pointer context, long slider_tick_misses);

        void performance_slider_end_hits(Pointer context, long slider_end_hits);

        void performance_n300(Pointer context, long n300);

        void performance_n100(Pointer context, long n100);

        void performance_n50(Pointer context, long n50);

        void performance_n_katu(Pointer context, long n_katu);

        void performance_n_geki(Pointer context, long n_geki);

        ScoreState.ByValue performance_generate_state(Pointer context, Pointer beatmap);

        PerformanceAttributes.ByValue performance_calculate(Pointer context, Pointer beatmap);

        PerformanceAttributes.ByValue performance_calculate_from_difficulty(Pointer context, DifficultyAttributes.ByValue difficulty_attr);

        double performance_get_clock_rate(Pointer context);

        /// Destroys the given instance.
        ///
        /// # Safety
        ///
        /// The passed parameter MUST have been created with the corresponding init function;
        /// passing any other value results in undefined behavior.
        int string_destroy(PointerByReference context);

        int string_from_c_str(PointerByReference context, String str);

        int string_empty(PointerByReference context);

        boolean string_is_init(Pointer context);

        String string_to_cstr(Pointer context);

        /// Destroys the given instance.
        ///
        /// # Safety
        ///
        /// The passed parameter MUST have been created with the corresponding init function;
        /// passing any other value results in undefined behavior.
        int mods_destroy(PointerByReference context);

        int mods_new(PointerByReference context, int mode);

        int mods_from_acronyms(PointerByReference context, String str, int mode);

        int mods_from_bits(PointerByReference context, long bits, int mode);

        int mods_from_json(PointerByReference context, String str, int mode);

        int mods_from_json_sanitize(PointerByReference context, String str, int mode);

        void mods_remove_incompatible_mods(Pointer context);

        long mods_bits(Pointer context);

        long mods_len(Pointer context);

        void mods_json(Pointer context, Pointer str);

        boolean mods_insert_json(Pointer context, String str);

        boolean mods_insert(Pointer context, String str);

        boolean mods_contains(Pointer context, String str);

        void mods_clear(Pointer context);

        Optionf64 mods_clock_rate(Pointer context);

        /// Destroys the given instance.
        ///
        /// # Safety
        ///
        /// The passed parameter MUST have been created with the corresponding init function;
        /// passing any other value results in undefined behavior.
        int mods_intermode_destroy(PointerByReference context);

        int mods_intermode_from_acronyms(PointerByReference context, String str);

        int mods_intermode_from_bits(PointerByReference context, long bits);

        long mods_intermode_bits(Pointer context);

        long mods_intermode_len(Pointer context);

        boolean mods_intermode_contains(Pointer context, String str);

        boolean mods_intermode_intersects(Pointer context, String str);

        double mods_intermode_legacy_clock_rate(Pointer context);

        void debug_difficylty_attributes(DifficultyAttributes res, Pointer str);

        void debug_performance_attributes(PerformanceAttributes res, Pointer str);

        void debug_score_state(ScoreState res, Pointer str);

        double calculate_accuacy(ScoreState state, DifficultyAttributes difficulty);

        @Structure.FieldOrder({"data", "len"})
        public static class Sliceu8 extends Structure {
            public Pointer data;
            public long len;

            public Sliceu8(byte[] data) {
                this.data = new Memory(data.length);
                this.data.write(0, data, 0, data.length);
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

        @Structure.FieldOrder({ "aim", "speed", "flashlight", "slider_factor",
                    "speed_note_count", "aim_difficult_strain_count", "speed_difficult_strain_count",
                    "ar", "od", "hp",
                    "n_circles", "n_sliders", "n_slider_ticks", "n_spinners",
                    "stars", "max_combo" })
        public class OsuDifficultyAttributes extends Structure {
            public double aim;                           // Difficulty of the aim skill
            public double speed;                         // Difficulty of the speed skill
            public double flashlight;                   // Difficulty of the flashlight skill
            public double slider_factor;                // Ratio of aim strain with/without sliders
            public double speed_note_count;             // Number of clickable objects weighted by difficulty
            public double aim_difficult_strain_count;   // Weighted sum of aim strains
            public double speed_difficult_strain_count; // Weighted sum of speed strains
            public double ar;                           // Approach rate
            public double od;                           // Overall difficulty
            public double hp;                           // Health drain rate
            public int n_circles;                       // Number of circles (unsigned int -> int)
            public int n_sliders;                       // Number of sliders (unsigned int -> int)
            public int n_slider_ticks;                  // Number of slider ticks and repeat points (unsigned int -> int)
            public int n_spinners;                      // Number of spinners (unsigned int -> int)
            public double stars;                        // Final star rating
            public int max_combo;                       // Maximum combo (unsigned int -> int)
        
            public static class ByReference extends OsuDifficultyAttributes implements Structure.ByReference {}
            public static class ByValue extends OsuDifficultyAttributes implements Structure.ByValue {}
        }

        @Structure.FieldOrder({ "difficulty", "pp", "pp_acc", "pp_aim",
                    "pp_flashlight", "pp_speed", "effective_miss_count" })
        public class OsuPerformanceAttributes extends Structure {
            public OsuDifficultyAttributes difficulty; // Nested structure for difficulty attributes
            public double pp;                          // Final performance points
            public double pp_acc;                      // Accuracy portion of the final pp
            public double pp_aim;                      // Aim portion of the final pp
            public double pp_flashlight;               // Flashlight portion of the final pp
            public double pp_speed;                    // Speed portion of the final pp
            public double effective_miss_count;        // Misses including approximated slider breaks
        
            public static class ByReference extends OsuPerformanceAttributes implements Structure.ByReference {}
            public static class ByValue extends OsuPerformanceAttributes implements Structure.ByValue {}
        }

        @Structure.FieldOrder({ "stamina", "rhythm", "color", "peak", 
                    "great_hit_window", "ok_hit_window", "mono_stamina_factor", 
                    "stars", "max_combo", "is_convert" })
        public class TaikoDifficultyAttributes extends Structure {
            public double stamina;               // Difficulty of the stamina skill
            public double rhythm;                // Difficulty of the rhythm skill
            public double color;                 // Difficulty of the color skill
            public double peak;                  // Difficulty of the hardest parts of the map
            public double great_hit_window;      // Hit window for an n300 inclusive of mods
            public double ok_hit_window;         // Hit window for an n100 inclusive of mods
            public double mono_stamina_factor;   // Stamina difficulty ratio for mono-color streams
            public double stars;                 // Final star rating
            public int max_combo;                // Maximum combo (unsigned int -> int)
            public boolean is_convert;           // Whether the beatmap is a convert (osu!standard)
        
            public static class ByReference extends TaikoDifficultyAttributes implements Structure.ByReference {}
            public static class ByValue extends TaikoDifficultyAttributes implements Structure.ByValue {}
        }

        @Structure.FieldOrder({ "difficulty", "pp", "pp_acc", "pp_difficulty", 
                    "effective_miss_count", "estimated_unstable_rate" })
        public class TaikoPerformanceAttributes extends Structure {
            public TaikoDifficultyAttributes difficulty;   // Difficulty attributes used for performance calculation
            public double pp;                              // Final performance points
            public double pp_acc;                          // Accuracy portion of the final pp
            public double pp_difficulty;                   // Strain portion of the final pp
            public double effective_miss_count;            // Scaled miss count based on total hits
            public Optionf64 estimated_unstable_rate;      // Estimated unstable rate (optional value)
        
            public static class ByReference extends TaikoPerformanceAttributes implements Structure.ByReference {}
            public static class ByValue extends TaikoPerformanceAttributes implements Structure.ByValue {}
        }

        @Structure.FieldOrder({ "stars", "ar", "n_fruits", "n_droplets", "n_tiny_droplets", "is_convert" })
        public class CatchDifficultyAttributes extends Structure {
            public double stars;        // Final star rating
            public double ar;           // Approach rate
            public int n_fruits;        // Number of fruits (unsigned int -> use int in Java)
            public int n_droplets;      // Number of droplets (unsigned int -> use int in Java)
            public int n_tiny_droplets; // Number of tiny droplets (unsigned int -> use int in Java)
            public boolean is_convert;  // Whether the beatmap is a convert (bool)
        
            public static class ByReference extends CatchDifficultyAttributes implements Structure.ByReference {}
            public static class ByValue extends CatchDifficultyAttributes implements Structure.ByValue {}
        }

        @Structure.FieldOrder({ "difficulty", "pp" })
        public class CatchPerformanceAttributes extends Structure {
            public CatchDifficultyAttributes difficulty; // Nested CatchDifficultyAttributes structure
            public double pp;                            // Final performance points
        
            public static class ByReference extends CatchPerformanceAttributes implements Structure.ByReference {}
            public static class ByValue extends CatchPerformanceAttributes implements Structure.ByValue {}
        }
        
        @Structure.FieldOrder({ "stars", "hit_window", "n_objects", "n_hold_notes", "max_combo", "is_convert" })
        public class ManiaDifficultyAttributes extends Structure {
            public double stars;        // Final star rating
            public double hit_window;   // Perceived hit window for n300 inclusive of rate-adjusting mods
            public int n_objects;       // Number of hit objects (unsigned int -> int in Java)
            public int n_hold_notes;    // Number of hold notes (unsigned int -> int in Java)
            public int max_combo;       // Maximum achievable combo (unsigned int -> int in Java)
            public boolean is_convert;  // Whether the beatmap is a convert (boolean with I1 marshalling)
        
            public static class ByReference extends ManiaDifficultyAttributes implements Structure.ByReference {}
            public static class ByValue extends ManiaDifficultyAttributes implements Structure.ByValue {}
        }

        @Structure.FieldOrder({ "difficulty", "pp", "pp_difficulty" })
        public class ManiaPerformanceAttributes extends Structure {
            public ManiaDifficultyAttributes difficulty; // Nested ManiaDifficultyAttributes structure
            public double pp;                            // Final performance points
            public double pp_difficulty;                 // Difficulty portion of the final pp
        
            public static class ByReference extends ManiaPerformanceAttributes implements Structure.ByReference {}
            public static class ByValue extends ManiaPerformanceAttributes implements Structure.ByValue {}
        }

        @Structure.FieldOrder({ "t", "is_some" })
        public class OptionOsuDifficultyAttributes extends Structure {
            public OsuDifficultyAttributes t;     // Element that is maybe valid
            public byte is_some;                  // 1 means element t is valid
        
            public static class ByReference extends OptionOsuDifficultyAttributes implements Structure.ByReference {}
            public static class ByValue extends OptionOsuDifficultyAttributes implements Structure.ByValue {}
        
            public Optional<OsuDifficultyAttributes> toOptional() {
                return is_some == 1 ? Optional.of(t) : Optional.empty();
            }
        }

        @Structure.FieldOrder({ "t", "is_some" })
        public class OptionTaikoDifficultyAttributes extends Structure {
            public TaikoDifficultyAttributes t;     // Element that is maybe valid
            public byte is_some;                  // 1 means element t is valid

            public static class ByReference extends OptionTaikoDifficultyAttributes implements Structure.ByReference {}
            public static class ByValue extends OptionTaikoDifficultyAttributes implements Structure.ByValue {}
        
            public Optional<TaikoDifficultyAttributes> toOptional() {
                return is_some == 1 ? Optional.of(t) : Optional.empty();
            }
        }

        @Structure.FieldOrder({ "t", "is_some" })
        public class OptionCatchDifficultyAttributes extends Structure {
            public CatchDifficultyAttributes t;     // Element that is maybe valid
            public byte is_some;                  // 1 means element t is valid
        
            public static class ByReference extends OptionCatchDifficultyAttributes implements Structure.ByReference {}
            public static class ByValue extends OptionCatchDifficultyAttributes implements Structure.ByValue {}
        
            public Optional<CatchDifficultyAttributes> toOptional() {
                return is_some == 1 ? Optional.of(t) : Optional.empty();
            }
        }

        @Structure.FieldOrder({ "t", "is_some" })
        public class OptionManiaDifficultyAttributes extends Structure {
            public ManiaDifficultyAttributes t;     // Element that is maybe valid
            public byte is_some;                  // 1 means element t is valid
        
            public static class ByReference extends OptionManiaDifficultyAttributes implements Structure.ByReference {}
            public static class ByValue extends OptionManiaDifficultyAttributes implements Structure.ByValue {}
        
            public Optional<ManiaDifficultyAttributes> toOptional() {
                return is_some == 1 ? Optional.of(t) : Optional.empty();
            }
        }

        @Structure.FieldOrder({ "osu", "taiko", "fruit", "mania", "mode" })
        public class DifficultyAttributes extends Structure {
            public OptionOsuDifficultyAttributes osu;   // Option for osu!difficulty attributes
            public OptionTaikoDifficultyAttributes taiko; // Option for taiko difficulty attributes
            public OptionCatchDifficultyAttributes fruit; // Option for catch difficulty attributes
            public OptionManiaDifficultyAttributes mania; // Option for mania difficulty attributes
            public int mode;                            // Mode enum (osu!, taiko, catch, mania)
        
            public static class ByReference extends DifficultyAttributes implements Structure.ByReference {}
            public static class ByValue extends DifficultyAttributes implements Structure.ByValue {}
        }

        @Structure.FieldOrder({ "t", "is_some" })
        public class OptionOsuPerformanceAttributes extends Structure {
            public OsuPerformanceAttributes t;     // Element that is maybe valid
            public byte is_some;                  // 1 means element t is valid
        
            public static class ByReference extends OptionOsuPerformanceAttributes implements Structure.ByReference {}
            public static class ByValue extends OptionOsuPerformanceAttributes implements Structure.ByValue {}
        
            public Optional<OsuPerformanceAttributes> toOptional() {
                return is_some == 1 ? Optional.of(t) : Optional.empty();
            }
        }

        @Structure.FieldOrder({ "t", "is_some" })
        public class OptionTaikoPerformanceAttributes extends Structure {
            public TaikoPerformanceAttributes t;     // Element that is maybe valid
            public byte is_some;                  // 1 means element t is valid
        
            public static class ByReference extends OptionTaikoPerformanceAttributes implements Structure.ByReference {}
            public static class ByValue extends OptionTaikoPerformanceAttributes implements Structure.ByValue {}
        
            public Optional<TaikoPerformanceAttributes> toOptional() {
                return is_some == 1 ? Optional.of(t) : Optional.empty();
            }
        }

        @Structure.FieldOrder({ "t", "is_some" })
        public class OptionCatchPerformanceAttributes extends Structure {
            public CatchPerformanceAttributes t;     // Element that is maybe valid
            public byte is_some;                  // 1 means element t is valid
        
            public static class ByReference extends OptionCatchPerformanceAttributes implements Structure.ByReference {}
            public static class ByValue extends OptionCatchPerformanceAttributes implements Structure.ByValue {}
        
            public Optional<CatchPerformanceAttributes> toOptional() {
                return is_some == 1 ? Optional.of(t) : Optional.empty();
            }
        }

        @Structure.FieldOrder({ "t", "is_some" })
        public class OptionManiaPerformanceAttributes extends Structure {
            public ManiaPerformanceAttributes t;     // Element that is maybe valid
            public byte is_some;                  // 1 means element t is valid
        
            public static class ByReference extends OptionManiaPerformanceAttributes implements Structure.ByReference {}
            public static class ByValue extends OptionManiaPerformanceAttributes implements Structure.ByValue {}
        
            public Optional<ManiaPerformanceAttributes> toOptional() {
                return is_some == 1 ? Optional.of(t) : Optional.empty();
            }
        }

        @Structure.FieldOrder({ "osu", "taiko", "fruit", "mania", "mode" })
        public class PerformanceAttributes extends Structure {
            public OptionOsuPerformanceAttributes osu;   // Option for osu!difficulty attributes
            public OptionTaikoPerformanceAttributes taiko; // Option for taiko difficulty attributes
            public OptionCatchPerformanceAttributes fruit; // Option for catch difficulty attributes
            public OptionManiaPerformanceAttributes mania; // Option for mania difficulty attributes
            public int mode;                            // Mode enum (osu!, taiko, catch, mania)
        
            public static class ByReference extends PerformanceAttributes implements Structure.ByReference {}
            public static class ByValue extends PerformanceAttributes implements Structure.ByValue {}
        }

        @Structure.FieldOrder({ "ar", "od_great", "od_ok" })
        public static class HitWindows extends Structure {
            /// Hit window for approach rate i.e. `TimePreempt` in milliseconds.
            public double ar;
            /// Hit window for overall difficulty i.e. time to hit a 300 ("Great") in milliseconds.
            public double od_great;
            /// Hit window for overall difficulty i.e. time to hit a 100 ("Ok") in milliseconds.
            ///
            /// `None` for osu!mania.
            public Optionf64 od_ok;

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

        @Structure.FieldOrder({ "max_combo", "slider_tick_hits", "slider_tick_misses", "slider_end_hits",
                    "n_geki", "n_katu", "n300", "n100", "n50", "misses" })
        public class ScoreState extends Structure {
            public int max_combo;            // Maximum combo (unsigned int -> int)
            public int slider_tick_hits;     // Hits on slider ticks (unsigned int -> int)
            public int slider_tick_misses;   // Misses on slider ticks (unsigned int -> int)
            public int slider_end_hits;      // Hits on slider ends (unsigned int -> int)
            public int n_geki;               // Current gekis (unsigned int -> int)
            public int n_katu;               // Current katus (unsigned int -> int)
            public int n300;                 // Current 300s (unsigned int -> int)
            public int n100;                 // Current 100s (unsigned int -> int)
            public int n50;                  // Current 50s (unsigned int -> int)
            public int misses;               // Current misses (unsigned int -> int)
        
            public static class ByReference extends ScoreState implements Structure.ByReference {}
            public static class ByValue extends ScoreState implements Structure.ByValue {}
        }
    }

    public static class Beatmap implements AutoCloseable {
        private PointerByReference _context;  // The context of the Beatmap

        // Load the Beatmap from bytes
        public Beatmap(byte[] data) {
            _context = new PointerByReference();  // Initialize _context to a valid Pointer
            var sliceu8 = new RosuPPLib.Sliceu8(data);
            int rval = RosuPPLib.INSTANCE.beatmap_from_bytes(_context, sliceu8);
            if (rval != FFIError.Ok) {
                throw new RuntimeException("Error loading beatmap from bytes");
            }
        }
        
        public Beatmap(RosuPPLib.Sliceu8 data) {
            _context = new PointerByReference();  // Initialize _context to a valid Pointer
            int rval = RosuPPLib.INSTANCE.beatmap_from_bytes(_context, data);
            if (rval != FFIError.Ok) {
                throw new RuntimeException("Error loading beatmap from bytes");
            }
        }
        

        // Load the Beatmap from a file path
        public Beatmap(String path) {
            _context = new PointerByReference();  // Initialize _context to a valid Pointer
            int rval = RosuPPLib.INSTANCE.beatmap_from_path(_context, path);
            if (rval != FFIError.Ok) {
                throw new RuntimeException("Error loading beatmap from path");
            }
        }

        // Convert the Beatmap to the specified mode
        public boolean convert(Mode mode) {
            return RosuPPLib.INSTANCE.beatmap_convert(getContext(), mode.getValue());
        }

        // Get the BPM of the Beatmap
        public double bpm() {
            return RosuPPLib.INSTANCE.beatmap_bpm(getContext());
        }

        // Get the total break time of the Beatmap
        public double totalBreakTime() {
            return RosuPPLib.INSTANCE.beatmap_total_break_time(getContext());
        }

        // Get the mode of the Beatmap
        public Mode mode() {
            return Mode.fromValue(RosuPPLib.INSTANCE.beatmap_mode(getContext()));
        }

        // Check if the Beatmap is a converted map
        public boolean isConvert() {
            return RosuPPLib.INSTANCE.beatmap_is_convert(getContext());
        }

        // Getter for the context
        public Pointer getContext() {
            return _context.getValue();
        }

        // Dispose method (releases the resources)
        @Override
        public void close() {
            int rval = RosuPPLib.INSTANCE.beatmap_destroy(_context);
            if (rval != 0) {
                throw new RuntimeException("Error destroying beatmap");
            }
        }
    }

    public static class BeatmapAttributesBuilder implements AutoCloseable {
        private PointerByReference _context; // Context for BeatmapAttributesBuilder
    
        public BeatmapAttributesBuilder() {
            _context = new PointerByReference();
            int rval = RosuPPLib.INSTANCE.beatmap_attributes_new(_context);
            if (rval != FFIError.Ok) {
                throw new RuntimeException("Error creating BeatmapAttributesBuilder");
            }
        }
    
        // Method to dispose of the builder
        @Override
        public void close() {
            int rval = RosuPPLib.INSTANCE.beatmap_attributes_destroy(_context);
            if (rval != FFIError.Ok) {
                throw new RuntimeException("Error destroying BeatmapAttributesBuilder");
            }
        }
    
        // Method to set the mode
        public void setMode(Mode mode) {
            RosuPPLib.INSTANCE.beatmap_attributes_mode(getContext(), mode.getValue());
        }
    
        // Method to set mods (using IntPtr)
        public void setMods(Mods mods) {
            RosuPPLib.INSTANCE.beatmap_attributes_p_mods(getContext(), mods.getContext());
        }
    
        // Method to set mods (using uint)
        public void setMods(int mods) {
            RosuPPLib.INSTANCE.beatmap_attributes_i_mods(getContext(), mods);
        }
    
        // Method to set mods (using string)
        public void setMods(String str) {
            int rval = RosuPPLib.INSTANCE.beatmap_attributes_s_mods(getContext(), str);
            if (rval != FFIError.Ok) {
                throw new RuntimeException("Error setting string mods");
            }
        }
    
        // Method to set clock rate
        public void setClockRate(double clockRate) {
            RosuPPLib.INSTANCE.beatmap_attributes_clock_rate(getContext(), clockRate);
        }
    
        // Method to set AR (approach rate)
        public void setAr(float ar) {
            RosuPPLib.INSTANCE.beatmap_attributes_ar(getContext(), ar);
        }
    
        // Method to set CS (circle size)
        public void setCs(float cs) {
            RosuPPLib.INSTANCE.beatmap_attributes_cs(getContext(), cs);
        }
    
        // Method to set HP (health drain rate)
        public void setHp(float hp) {
            RosuPPLib.INSTANCE.beatmap_attributes_hp(getContext(), hp);
        }
    
        // Method to set OD (overall difficulty)
        public void setOd(float od) {
            RosuPPLib.INSTANCE.beatmap_attributes_od(getContext(), od);
        }
    
        // Method to get the clock rate
        public double getClockRate() {
            return RosuPPLib.INSTANCE.beatmap_attributes_get_clock_rate(getContext());
        }
    
        // Method to build BeatmapAttributes
        public RosuPPLib.BeatmapAttributes build(Beatmap beatmap) {
            return RosuPPLib.INSTANCE.beatmap_attributes_build(getContext(), beatmap.getContext());
        }
    
        // Getter for the context
        public Pointer getContext() {
            return _context.getValue();
        }
    }

    public static class Difficulty implements AutoCloseable {
        private PointerByReference _context;
    
        public Difficulty() {
            _context = new PointerByReference();
            int rval = RosuPPLib.INSTANCE.difficulty_new(_context);
            if (rval != 0) {
                throw new RuntimeException("Error creating Difficulty");
            }
        }
    
        // Method to dispose of the Difficulty
        @Override
        public void close() {
            int rval = RosuPPLib.INSTANCE.difficulty_destroy(_context);
            if (rval != 0) {
                throw new RuntimeException("Error destroying Difficulty");
            }
        }
    
        // Method to set p_mods (using Pointer)
        public void setMods(Mods mods) {
            RosuPPLib.INSTANCE.difficulty_p_mods(getContext(), mods.getContext());
        }
    
        // Method to set i_mods (using uint)
        public void setMods(int mods) {
            RosuPPLib.INSTANCE.difficulty_i_mods(getContext(), mods);
        }
    
        // Method to set s_mods (using string)
        public void setMods(String str) {
            int rval = RosuPPLib.INSTANCE.difficulty_s_mods(getContext(), str);
            if (rval != 0) {
                throw new RuntimeException("Error setting string mods");
            }
        }
    
        // Method to set passed objects (using uint)
        public void setPassedObjects(int passedObjects) {
            RosuPPLib.INSTANCE.difficulty_passed_objects(getContext(), passedObjects);
        }
    
        // Method to set clock rate
        public void setClockRate(double clockRate) {
            RosuPPLib.INSTANCE.difficulty_clock_rate(getContext(), clockRate);
        }
    
        // Method to set AR (approach rate)
        public void setAr(float ar) {
            RosuPPLib.INSTANCE.difficulty_ar(getContext(), ar);
        }
    
        // Method to set CS (circle size)
        public void setCs(float cs) {
            RosuPPLib.INSTANCE.difficulty_cs(getContext(), cs);
        }
    
        // Method to set HP (health drain)
        public void setHp(float hp) {
            RosuPPLib.INSTANCE.difficulty_hp(getContext(), hp);
        }
    
        // Method to set OD (overall difficulty)
        public void setOd(float od) {
            RosuPPLib.INSTANCE.difficulty_od(getContext(), od);
        }
    
        // Method to set hardrock offsets
        public void setHardrockOffsets(boolean hardrockOffsets) {
            RosuPPLib.INSTANCE.difficulty_hardrock_offsets(getContext(), hardrockOffsets);
        }
    
        // Method to set lazer
        public void setLazer(boolean lazer) {
            RosuPPLib.INSTANCE.difficulty_lazer(getContext(), lazer);
        }
    
        // Method to calculate DifficultyAttributes from beatmap
        public RosuPPLib.DifficultyAttributes calculate(Beatmap beatmap) {
            return RosuPPLib.INSTANCE.difficulty_calculate(getContext(), beatmap.getContext());
        }
    
        // Method to get clock rate
        public double getClockRate() {
            return RosuPPLib.INSTANCE.difficulty_get_clock_rate(getContext());
        }
    
        // Getter for context
        public Pointer getContext() {
            return _context.getValue();
        }
    }
    
    public static class Performance implements AutoCloseable {
        private PointerByReference _context;
    
        public Performance() {
            _context = new PointerByReference();
            int rval = RosuPPLib.INSTANCE.performance_new(_context);
            if (rval != 0) {
                throw new RuntimeException("Error creating Performance");
            }
        }
    
        // Method to dispose of the Performance
        @Override
        public void close() {
            int rval = RosuPPLib.INSTANCE.performance_destroy(_context);
            if (rval != 0) {
                throw new RuntimeException("Error destroying Performance");
            }
        }
    
        // Method to set mode
        public void setMode(Mode mode) {
            RosuPPLib.INSTANCE.performance_mode(getContext(), mode.getValue());
        }
    
        // Method to set p_mods (using Pointer)
        public void setMods(Mods mods) {
            RosuPPLib.INSTANCE.performance_p_mods(getContext(), mods.getContext());
        }
    
        // Method to set i_mods (using uint)
        public void setMods(int mods) {
            RosuPPLib.INSTANCE.performance_i_mods(getContext(), mods);
        }
    
        // Method to set s_mods (using string)
        public void setMods(String str) {
            int rval = RosuPPLib.INSTANCE.performance_s_mods(getContext(), str);
            if (rval != 0) {
                throw new RuntimeException("Error setting string mods");
            }
        }
    
        // Method to set passed objects (using uint)
        public void setPassedObjects(int passedObjects) {
            RosuPPLib.INSTANCE.performance_passed_objects(getContext(), passedObjects);
        }
    
        // Method to set clock rate
        public void setClockRate(double clockRate) {
            RosuPPLib.INSTANCE.performance_clock_rate(getContext(), clockRate);
        }
    
        // Method to set AR (approach rate)
        public void setAr(float ar) {
            RosuPPLib.INSTANCE.performance_ar(getContext(), ar);
        }
    
        // Method to set CS (circle size)
        public void setCs(float cs) {
            RosuPPLib.INSTANCE.performance_cs(getContext(), cs);
        }
    
        // Method to set HP (health drain)
        public void setHp(float hp) {
            RosuPPLib.INSTANCE.performance_hp(getContext(), hp);
        }
    
        // Method to set OD (overall difficulty)
        public void setOd(float od) {
            RosuPPLib.INSTANCE.performance_od(getContext(), od);
        }
    
        // Method to set hardrock offsets
        public void setHardrockOffsets(boolean hardrockOffsets) {
            RosuPPLib.INSTANCE.performance_hardrock_offsets(getContext(), hardrockOffsets);
        }

        // Method to set hardrock offsets
        public void setHitResultPriority(int hitresult_priority) {
            RosuPPLib.INSTANCE.performance_hitresult_priority(getContext(), hitresult_priority);
        }

        public void setAccuracy(double accuracy) {
            RosuPPLib.INSTANCE.performance_accuracy(getContext(), accuracy);
        }

        public void setMisses(long misses) {
            RosuPPLib.INSTANCE.performance_misses(getContext(), misses);
        }

        public void setSliderTickHits(long sliderTickHits) {
            RosuPPLib.INSTANCE.performance_slider_tick_hits(getContext(), sliderTickHits);
        }
        
        public void setSliderTickMisses(long sliderTickMisses) {
            RosuPPLib.INSTANCE.performance_slider_tick_misses(getContext(), sliderTickMisses);
        }
        
        public void setSliderEndHits(long sliderEndHits) {
            RosuPPLib.INSTANCE.performance_slider_end_hits(getContext(), sliderEndHits);
        }
        
        public void setN300(long n300) {
            RosuPPLib.INSTANCE.performance_n300(getContext(), n300);
        }
        
        public void setN100(long n100) {
            RosuPPLib.INSTANCE.performance_n100(getContext(), n100);
        }
        
        public void setN50(long n50) {
            RosuPPLib.INSTANCE.performance_n50(getContext(), n50);
        }
        
        public void setNKatu(long nKatu) {
            RosuPPLib.INSTANCE.performance_n_katu(getContext(), nKatu);
        }
        
        public void setNGeki(long nGeki) {
            RosuPPLib.INSTANCE.performance_n_geki(getContext(), nGeki);
        }

        // Method to set lazer
        public void setLazer(boolean lazer) {
            RosuPPLib.INSTANCE.performance_lazer(getContext(), lazer);
        }

        public RosuPPLib.ScoreState GenerateState(Beatmap beatmap) {
            return RosuPPLib.INSTANCE.performance_generate_state(getContext(), beatmap.getContext());
        }
    
        // Method to calculate PerformanceAttributes from beatmap
        public RosuPPLib.PerformanceAttributes calculate(Beatmap beatmap) {
            return RosuPPLib.INSTANCE.performance_calculate(getContext(), beatmap.getContext());
        }
    
        // Method to calculate PerformanceAttributes from DifficultyAttributes
        public RosuPPLib.PerformanceAttributes calculateFromDifficulty(RosuPPLib.DifficultyAttributes difficultyAttributes) {
            return RosuPPLib.INSTANCE.performance_calculate_from_difficulty(getContext(), (RosuPPLib.DifficultyAttributes.ByValue)difficultyAttributes);
        }
    
        // Method to get clock rate
        public double getClockRate() {
            return RosuPPLib.INSTANCE.performance_get_clock_rate(getContext());
        }
    
        // Getter for context
        public Pointer getContext() {
            return _context.getValue();
        }
    }

    public static class Mods {
        private static final Cleaner cleaner = Cleaner.create();
        @SuppressWarnings("unused")
        private final Cleaner.Cleanable cleanable;

        private PointerByReference _context; // Context for BeatmapAttributesBuilder

        private Mods() {
            _context = new PointerByReference();
            this.cleanable = cleaner.register(this, cleanAction(_context));
        }

        private static Runnable cleanAction(final PointerByReference context) {
            return () -> {
                int rval = RosuPPLib.INSTANCE.mods_destroy(context);
                if (rval != FFIError.Ok) {
                    throw new RuntimeException("Error destroying Mods");
                }
            };
        }
    
        /// new
        public static Mods New(Mode mode) {
            var m = new Mods();
            int rval = RosuPPLib.INSTANCE.mods_new(m._context, mode.getValue());
            if (rval != FFIError.Ok) {
                throw new RuntimeException("Error creating Mods");
            }
            return m;
        }

        /// from acronyms
        public static Mods FromAcronyms(String mods, Mode mode) {
            var m = new Mods();
            int rval = RosuPPLib.INSTANCE.mods_from_acronyms(m._context, mods, mode.getValue());
            if (rval != FFIError.Ok) {
                throw new RuntimeException("Error creating Mods");
            }
            return m;
        }

        /// from bits
        public static Mods FromBits(long mods, Mode mode) {
            var m = new Mods();
            int rval = RosuPPLib.INSTANCE.mods_from_bits(m._context, mods, mode.getValue());
            if (rval != FFIError.Ok) {
                throw new RuntimeException("Error creating Mods");
            }
            return m;
        }
    
        /// from json
        public static Mods FromJson(String mods, Mode mode) {
            var m = new Mods();
            int rval = RosuPPLib.INSTANCE.mods_from_json(m._context, mods, mode.getValue());
            if (rval != FFIError.Ok) {
                throw new RuntimeException("Error creating Mods");
            }
            return m;
        }

        /// from json sanitize
        public static Mods FromJsonSanitize(String mods, Mode mode) {
            var m = new Mods();
            int rval = RosuPPLib.INSTANCE.mods_from_json_sanitize(m._context, mods, mode.getValue());
            if (rval != FFIError.Ok) {
                throw new RuntimeException("Error creating Mods");
            }
            return m;
        }

        public void RemoveIncompatibleMods() {
            RosuPPLib.INSTANCE.mods_remove_incompatible_mods(getContext());
        } 
        
        public long getBits() {
            return RosuPPLib.INSTANCE.mods_bits(getContext());
        } 

        public long getLength() {
            return RosuPPLib.INSTANCE.mods_len(getContext());
        }

        public OwnedString toJson() {
            var s = new OwnedString();
            RosuPPLib.INSTANCE.mods_json(getContext(), s.getContext());
            return s;
        }

        public boolean InsertJson(String mod) {
            return RosuPPLib.INSTANCE.mods_insert_json(getContext(), mod);
        }

        public boolean Insert(String mod) {
            return RosuPPLib.INSTANCE.mods_insert(getContext(), mod);
        }

        public boolean Contains(String mod) {
            return RosuPPLib.INSTANCE.mods_contains(getContext(), mod);
        }

        public void Clear() {
            RosuPPLib.INSTANCE.mods_clear(getContext());
        }

        public RosuPPLib.Optionf64 getClockRate() {
            return RosuPPLib.INSTANCE.mods_clock_rate(getContext());
        }

        // Getter for the context
        public Pointer getContext() {
            return _context.getValue();
        }
    }
    

    public static class OwnedString {
        private static final Cleaner cleaner = Cleaner.create();
        @SuppressWarnings("unused")
        private final Cleaner.Cleanable cleanable;

        private PointerByReference _context; // Context for BeatmapAttributesBuilder
    
        public OwnedString() {
            _context = new PointerByReference();
            int rval = RosuPPLib.INSTANCE.string_empty(_context);
            if (rval != FFIError.Ok) {
                throw new RuntimeException("Error creating OwnedString");
            }
            this.cleanable = cleaner.register(this, cleanAction(_context));
        }

        public OwnedString(String str) {
            _context = new PointerByReference();
            int rval = RosuPPLib.INSTANCE.string_from_c_str(_context, str);
            if (rval != FFIError.Ok) {
                throw new RuntimeException("Error creating OwnedString");
            }
            this.cleanable = cleaner.register(this, cleanAction(_context));
        }

        private static Runnable cleanAction(final PointerByReference context) {
            return () -> {
                int rval = RosuPPLib.INSTANCE.string_destroy(context);
                if (rval != FFIError.Ok) {
                    throw new RuntimeException("Error destroying Mods");
                }
            };
        }
    
        public String toCstr() {
            return RosuPPLib.INSTANCE.string_to_cstr(getContext());
        } 
        
        public boolean isInit() {
            return RosuPPLib.INSTANCE.string_is_init(getContext());
        } 
        
        public String toString() {
            return isInit() ? toCstr() : null;
        } 

        // Getter for the context
        public Pointer getContext() {
            return _context.getValue();
        }
    }

    public static OwnedString DebugDifficyltyAttributes(RosuPPLib.DifficultyAttributes attr) {
        if (attr == null) return null;
        var s = new OwnedString();
        RosuPPLib.INSTANCE.debug_difficylty_attributes(attr, s.getContext());
        return s;
    }

    public static OwnedString DebugPerformanceAttributes(RosuPPLib.PerformanceAttributes attr) {
        if (attr == null) return null;
        var s = new OwnedString();
        RosuPPLib.INSTANCE.debug_performance_attributes(attr, s.getContext());
        return s;
    }

    public static OwnedString DebugScoreState(RosuPPLib.ScoreState attr) {
        if (attr == null) return null;
        var s = new OwnedString();
        RosuPPLib.INSTANCE.debug_score_state(attr, s.getContext());
        return s;
    }

    public enum Mode {
        OSU(0),
        TAIKO(1),
        CATCH(2),
        MANIA(3);
    
        private final int value;
    
        Mode(int value) {
            this.value = value;
        }
    
        public int getValue() {
            return value;
        }
    
        public static Mode fromValue(int value) {
            for (Mode mode : values()) {
                if (mode.value == value) {
                    return mode;
                }
            }
            throw new IllegalArgumentException("Unknown mode value: " + value);
        }
    }
}