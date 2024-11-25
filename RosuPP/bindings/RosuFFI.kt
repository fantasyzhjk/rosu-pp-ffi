import com.sun.jna.*
import com.sun.jna.Structure.FieldOrder
import com.sun.jna.ptr.PointerByReference
import java.lang.ref.Cleaner
import java.util.*

@Suppress("UNUSED")
object RosuFFI {
    fun debugDifficyltyAttributes(attr: RosuPPLib.DifficultyAttributes): OwnedString {
        val s = OwnedString()
        RosuPPLib.INSTANCE.debug_difficylty_attributes(attr, s.context)
        return s
    }

    fun debugPerformanceAttributes(attr: RosuPPLib.PerformanceAttributes): OwnedString {
        val s = OwnedString()
        RosuPPLib.INSTANCE.debug_performance_attributes(attr, s.context)
        return s
    }

    fun debugScoreState(attr: RosuPPLib.ScoreState): OwnedString {
        val s = OwnedString()
        RosuPPLib.INSTANCE.debug_score_state(attr, s.context)
        return s
    }

    interface HitResultPriority {
        companion object {
            const val BESTCASE: Int = 0
            const val WORSTCASE: Int = 1
        }
    }

    interface ModeInt {
        companion object {
            /** osu!standard */
            const val OSU: Int = 0

            /** osu!taiko */
            const val TAIKO: Int = 1

            /** osu!catch */
            const val CATCH: Int = 2

            /** osu!mania */
            const val MANIA: Int = 3
        }
    }

    interface FFIError {
        companion object {
            const val OK: Int = 0
            const val NULL: Int = 100
            const val PANIC: Int = 200
            const val PARSEERROR: Int = 300
            const val INVALIDSTRING: Int = 400
            const val SERIALIZEERROR: Int = 500
            const val UNKNOWN: Int = 1000
        }
    }

    @Suppress("PropertyName", "FunctionName")
    interface RosuPPLib : Library {
        /** Destroys the given instance.
         *
         * # Safety
         *
         * The passed parameter MUST have been created with the corresponding init function;
         * passing any other value results in undefined behavior. */
        fun beatmap_attributes_destroy(context: PointerByReference): Int

        fun beatmap_attributes_new(context: PointerByReference): Int

        fun beatmap_attributes_mode(context: Pointer, mode: Int)

        fun beatmap_attributes_p_mods(context: Pointer, mods: Pointer)

        fun beatmap_attributes_i_mods(context: Pointer, mods: Long)

        fun beatmap_attributes_s_mods(context: Pointer, str: String): Int

        fun beatmap_attributes_clock_rate(context: Pointer, clockRate: Double)

        fun beatmap_attributes_ar(context: Pointer, ar: Float)

        fun beatmap_attributes_cs(context: Pointer, cs: Float)

        fun beatmap_attributes_hp(context: Pointer, hp: Float)

        fun beatmap_attributes_od(context: Pointer, od: Float)

        fun beatmap_attributes_get_clock_rate(context: Pointer): Double

        fun beatmap_attributes_build(context: Pointer, beatmap: Pointer): BeatmapAttributes.ByValue

        /** Destroys the given instance.
         *
         * # Safety
         *
         * The passed parameter MUST have been created with the corresponding init function;
         * passing any other value results in undefined behavior. */
        fun beatmap_destroy(context: PointerByReference): Int

        fun beatmap_from_bytes(context: PointerByReference, data: Sliceu8): Int

        fun beatmap_from_path(context: PointerByReference, path: String): Int

        /** Convert a Beatmap to the specified mode */
        fun beatmap_convert(context: Pointer, mode: Int): Boolean

        fun beatmap_bpm(context: Pointer): Double

        fun beatmap_total_break_time(context: Pointer): Double

        fun beatmap_mode(context: Pointer): Int

        fun beatmap_is_convert(context: Pointer): Boolean

        /** Destroys the given instance.
         *
         * # Safety
         *
         * The passed parameter MUST have been created with the corresponding init function;
         * passing any other value results in undefined behavior. */
        fun difficulty_destroy(context: PointerByReference): Int

        fun difficulty_new(context: PointerByReference): Int

        fun difficulty_p_mods(context: Pointer, mods: Pointer)

        fun difficulty_i_mods(context: Pointer, mods: Long)

        fun difficulty_s_mods(context: Pointer, str: String): Int

        fun difficulty_passed_objects(context: Pointer, passedObjects: Long)

        fun difficulty_clock_rate(context: Pointer, clockRate: Double)

        fun difficulty_ar(context: Pointer, ar: Float)

        fun difficulty_cs(context: Pointer, cs: Float)

        fun difficulty_hp(context: Pointer, hp: Float)

        fun difficulty_od(context: Pointer, od: Float)

        fun difficulty_hardrock_offsets(context: Pointer, hardrockOffsets: Boolean)

        fun difficulty_lazer(context: Pointer, lazer: Boolean)

        fun difficulty_calculate(context: Pointer, beatmap: Pointer): DifficultyAttributes.ByValue

        fun difficulty_get_clock_rate(context: Pointer): Double

        /** Destroys the given instance.
         *
         * # Safety
         *
         * The passed parameter MUST have been created with the corresponding init function;
         * passing any other value results in undefined behavior. */
        fun performance_destroy(context: PointerByReference): Int

        fun performance_new(context: PointerByReference): Int

        fun performance_mode(context: Pointer, mode: Int)

        fun performance_p_mods(context: Pointer, mods: Pointer)

        fun performance_i_mods(context: Pointer, mods: Long)

        fun performance_s_mods(context: Pointer, str: String): Int

        fun performance_passed_objects(context: Pointer, passedObjects: Long)

        fun performance_clock_rate(context: Pointer, clockRate: Double)

        fun performance_ar(context: Pointer, ar: Float)

        fun performance_cs(context: Pointer, cs: Float)

        fun performance_hp(context: Pointer, hp: Float)

        fun performance_od(context: Pointer, od: Float)

        fun performance_hardrock_offsets(context: Pointer, hardrockOffsets: Boolean)

        fun performance_accuracy(context: Pointer, accuracy: Double)

        fun performance_misses(context: Pointer, misses: Long)

        fun performance_combo(context: Pointer, combo: Long)

        fun performance_hitresult_priority(context: Pointer, hitresultPriority: Int)

        fun performance_lazer(context: Pointer, lazer: Boolean)

        fun performance_slider_tick_hits(context: Pointer, sliderTickHits: Long)

        fun performance_slider_tick_misses(context: Pointer, sliderTickMisses: Long)

        fun performance_slider_end_hits(context: Pointer, sliderEndHits: Long)

        fun performance_n300(context: Pointer, n300: Long)

        fun performance_n100(context: Pointer, n100: Long)

        fun performance_n50(context: Pointer, n50: Long)

        fun performance_n_katu(context: Pointer, nKatu: Long)

        fun performance_n_geki(context: Pointer, nGeki: Long)

        fun performance_generate_state(context: Pointer, beatmap: Pointer): ScoreState.ByValue

        fun performance_calculate(context: Pointer, beatmap: Pointer): PerformanceAttributes.ByValue

        fun performance_calculate_from_difficulty(context: Pointer, difficultyAttr: DifficultyAttributes.ByValue): PerformanceAttributes.ByValue

        fun performance_get_clock_rate(context: Pointer): Double

        /** Destroys the given instance.
         *
         * # Safety
         *
         * The passed parameter MUST have been created with the corresponding init function;
         * passing any other value results in undefined behavior. */
        fun string_destroy(context: PointerByReference): Int

        fun string_from_c_str(context: PointerByReference, str: String): Int

        fun string_empty(context: PointerByReference): Int

        fun string_is_init(context: Pointer): Boolean

        fun string_to_cstr(context: Pointer): String

        /** Destroys the given instance.
         *
         * # Safety
         *
         * The passed parameter MUST have been created with the corresponding init function;
         * passing any other value results in undefined behavior. */
        fun mods_destroy(context: PointerByReference): Int

        fun mods_new(context: PointerByReference, mode: Int): Int

        fun mods_from_acronyms(context: PointerByReference, str: String, mode: Int): Int

        fun mods_from_bits(context: PointerByReference, bits: Long, mode: Int): Int

        fun mods_from_json(context: PointerByReference, str: String, mode: Int): Int

        fun mods_from_json_sanitize(context: PointerByReference, str: String, mode: Int): Int

        fun mods_remove_incompatible_mods(context: Pointer)

        fun mods_bits(context: Pointer): Long

        fun mods_len(context: Pointer): Long

        fun mods_json(context: Pointer, str: Pointer)

        fun mods_insert_json(context: Pointer, str: String): Boolean

        fun mods_insert(context: Pointer, str: String): Boolean

        fun mods_contains(context: Pointer, str: String): Boolean

        fun mods_clear(context: Pointer)

        fun mods_clock_rate(context: Pointer): Optionf64

        /** Destroys the given instance.
         *
         * # Safety
         *
         * The passed parameter MUST have been created with the corresponding init function;
         * passing any other value results in undefined behavior. */
        fun mods_intermode_destroy(context: PointerByReference): Int

        fun mods_intermode_from_acronyms(context: PointerByReference, str: String): Int

        fun mods_intermode_from_bits(context: PointerByReference, bits: Long): Int

        fun mods_intermode_bits(context: Pointer): Long

        fun mods_intermode_len(context: Pointer): Long

        fun mods_intermode_contains(context: Pointer, str: String): Boolean

        fun mods_intermode_intersects(context: Pointer, str: String): Boolean

        fun mods_intermode_legacy_clock_rate(context: Pointer): Double

        fun debug_difficylty_attributes(res: DifficultyAttributes, str: Pointer)

        fun debug_performance_attributes(res: PerformanceAttributes, str: Pointer)

        fun debug_score_state(res: ScoreState, str: Pointer)

        fun calculate_accuacy(state: ScoreState, difficulty: DifficultyAttributes): Double

        @FieldOrder("data", "len")
        open class Sliceu8 : Structure {
            @JvmField var data: Pointer? = null
            @JvmField var len: Long = 0

            constructor(data: ByteArray) {
                val mem = Memory(data.size.toLong())
                mem.write(0, data, 0, data.size)
                this.data = mem
                this.len = data.size.toLong()
            }

            constructor()

            class ByReference : Sliceu8(), Structure.ByReference
            class ByValue : Sliceu8(), Structure.ByValue
        }

        @FieldOrder("t", "is_some")
        open class Optionf64 : Structure() {

            @JvmField var t: Double = 0.0
            @JvmField var is_some: Byte = 0

            class ByReference : Optionf64(), Structure.ByReference
            class ByValue : Optionf64(), Structure.ByValue

            fun toOptional(): Optional<Double> {
                return if (is_some.toInt() == 1) Optional.of(t) else Optional.empty()
            }
        }

        @FieldOrder(
            "aim",
            "speed",
            "flashlight",
            "slider_factor",
            "speed_note_count",
            "aim_difficult_strain_count",
            "speed_difficult_strain_count",
            "ar",
            "od",
            "hp",
            "n_circles",
            "n_sliders",
            "n_slider_ticks",
            "n_spinners",
            "stars",
            "max_combo"
        )
        open class OsuDifficultyAttributes : Structure() {
            @JvmField var aim: Double = 0.0 // Difficulty of the aim skill
            @JvmField var speed: Double = 0.0 // Difficulty of the speed skill
            @JvmField var flashlight: Double = 0.0 // Difficulty of the flashlight skill
            @JvmField var slider_factor: Double = 0.0 // Ratio of aim strain with/without sliders
            @JvmField var speed_note_count: Double = 0.0 // Number of clickable objects weighted by difficulty
            @JvmField var aim_difficult_strain_count: Double = 0.0 // Weighted sum of aim strains
            @JvmField var speed_difficult_strain_count: Double = 0.0 // Weighted sum of speed strains
            @JvmField var ar: Double = 0.0 // Approach rate
            @JvmField var od: Double = 0.0 // Overall difficulty
            @JvmField var hp: Double = 0.0 // Health drain rate
            @JvmField var n_circles: Int = 0 // Number of circles (unsigned int -> int)
            @JvmField var n_sliders: Int = 0 // Number of sliders (unsigned int -> int)
            @JvmField var n_slider_ticks: Int = 0 // Number of slider ticks and repeat points (unsigned int -> int)
            @JvmField var n_spinners: Int = 0 // Number of spinners (unsigned int -> int)
            @JvmField var stars: Double = 0.0 // Final star rating
            @JvmField var max_combo: Int = 0 // Maximum combo (unsigned int -> int)

            class ByReference : OsuDifficultyAttributes(), Structure.ByReference
            class ByValue : OsuDifficultyAttributes(), Structure.ByValue
        }

        @FieldOrder(
            "difficulty", "pp", "pp_acc", "pp_aim", "pp_flashlight", "pp_speed", "effective_miss_count"
        )
        open class OsuPerformanceAttributes() : Structure() {
            @JvmField var difficulty: OsuDifficultyAttributes? = null // Nested structure for difficulty attributes
            @JvmField var pp: Double = 0.0 // Final performance points
            @JvmField var pp_acc: Double = 0.0 // Accuracy portion of the final pp
            @JvmField var pp_aim: Double = 0.0 // Aim portion of the final pp
            @JvmField var pp_flashlight: Double = 0.0 // Flashlight portion of the final pp
            @JvmField var pp_speed: Double = 0.0 // Speed portion of the final pp
            @JvmField var effective_miss_count: Double = 0.0 // Misses including approximated slider breaks

            class ByReference : OsuPerformanceAttributes(), Structure.ByReference
            class ByValue : OsuPerformanceAttributes(), Structure.ByValue
        }

        @FieldOrder(
            "stamina",
            "rhythm",
            "color",
            "peak",
            "great_hit_window",
            "ok_hit_window",
            "mono_stamina_factor",
            "stars",
            "max_combo",
            "is_convert"
        )
        open class TaikoDifficultyAttributes : Structure() {
            @JvmField var stamina: Double = 0.0 // Difficulty of the stamina skill
            @JvmField var rhythm: Double = 0.0 // Difficulty of the rhythm skill
            @JvmField var color: Double = 0.0 // Difficulty of the color skill
            @JvmField var peak: Double = 0.0 // Difficulty of the hardest parts of the map
            @JvmField var great_hit_window: Double = 0.0 // Hit window for an n300 inclusive of mods
            @JvmField var ok_hit_window: Double = 0.0 // Hit window for an n100 inclusive of mods
            @JvmField var mono_stamina_factor: Double = 0.0 // Stamina difficulty ratio for mono-color streams
            @JvmField var stars: Double = 0.0 // Final star rating
            @JvmField var max_combo: Int = 0 // Maximum combo (unsigned int -> int)
            @JvmField var is_convert: Boolean = false // Whether the beatmap is a convert (osu!standard)

            class ByReference : TaikoDifficultyAttributes(), Structure.ByReference
            class ByValue : TaikoDifficultyAttributes(), Structure.ByValue
        }

        @FieldOrder(
            "difficulty", "pp", "pp_acc", "pp_difficulty", "effective_miss_count", "estimated_unstable_rate"
        )
        open class TaikoPerformanceAttributes : Structure() {
            @JvmField var difficulty: TaikoDifficultyAttributes? = null // Difficulty attributes used for performance calculation
            @JvmField var pp: Double = 0.0 // Final performance points
            @JvmField var pp_acc: Double = 0.0 // Accuracy portion of the final pp
            @JvmField var pp_difficulty: Double = 0.0 // Strain portion of the final pp
            @JvmField var effective_miss_count: Double = 0.0 // Scaled miss count based on total hits
            @JvmField var estimated_unstable_rate: Optionf64? = null // Estimated unstable rate (optional value)

            class ByReference : TaikoPerformanceAttributes(), Structure.ByReference
            class ByValue : TaikoPerformanceAttributes(), Structure.ByValue
        }

        @FieldOrder("stars", "ar", "n_fruits", "n_droplets", "n_tiny_droplets", "is_convert")
        open class CatchDifficultyAttributes : Structure() {
            @JvmField var stars: Double = 0.0 // Final star rating
            @JvmField var ar: Double = 0.0 // Approach rate
            @JvmField var n_fruits: Int = 0 // Number of fruits (unsigned int -> use int in Java)
            @JvmField var n_droplets: Int = 0 // Number of droplets (unsigned int -> use int in Java)
            @JvmField var n_tiny_droplets: Int = 0 // Number of tiny droplets (unsigned int -> use int in Java)
            @JvmField var is_convert: Boolean = false // Whether the beatmap is a convert (bool)

            class ByReference : CatchDifficultyAttributes(), Structure.ByReference
            class ByValue : CatchDifficultyAttributes(), Structure.ByValue
        }

        @FieldOrder("difficulty", "pp")
        open class CatchPerformanceAttributes : Structure() {
            @JvmField var difficulty: CatchDifficultyAttributes? = null // Nested CatchDifficultyAttributes structure
            @JvmField var pp: Double = 0.0 // Final performance points

            class ByReference : CatchPerformanceAttributes(), Structure.ByReference
            class ByValue : CatchPerformanceAttributes(), Structure.ByValue
        }

        @FieldOrder("stars", "hit_window", "n_objects", "n_hold_notes", "max_combo", "is_convert")
        open class ManiaDifficultyAttributes : Structure() {
            @JvmField var stars: Double = 0.0 // Final star rating
            @JvmField var hit_window: Double = 0.0 // Perceived hit window for n300 inclusive of rate-adjusting mods
            @JvmField var n_objects: Int = 0 // Number of hit objects (unsigned int -> int in Java)
            @JvmField var n_hold_notes: Int = 0 // Number of hold notes (unsigned int -> int in Java)
            @JvmField var max_combo: Int = 0 // Maximum achievable combo (unsigned int -> int in Java)
            @JvmField var is_convert: Boolean = false // Whether the beatmap is a convert (boolean with I1 marshalling)

            class ByReference : ManiaDifficultyAttributes(), Structure.ByReference
            class ByValue : ManiaDifficultyAttributes(), Structure.ByValue
        }

        @FieldOrder("difficulty", "pp", "pp_difficulty")
        open class ManiaPerformanceAttributes : Structure() {
            @JvmField var difficulty: ManiaDifficultyAttributes? = null // Nested ManiaDifficultyAttributes structure
            @JvmField var pp: Double = 0.0 // Final performance points
            @JvmField var pp_difficulty: Double = 0.0 // Difficulty portion of the final pp

            class ByReference : ManiaPerformanceAttributes(), Structure.ByReference
            class ByValue : ManiaPerformanceAttributes(), Structure.ByValue
        }

        @FieldOrder("t", "is_some")
        open class OptionOsuDifficultyAttributes : Structure() {
            @JvmField var t: OsuDifficultyAttributes? = null // Element that is maybe valid
            @JvmField var is_some: Byte = 0 // 1 means element t is valid

            class ByReference : OptionOsuDifficultyAttributes(), Structure.ByReference
            class ByValue : OptionOsuDifficultyAttributes(), Structure.ByValue

            fun toOptional(): Optional<OsuDifficultyAttributes> {
                return if (is_some.toInt() == 1) Optional.of(t!!) else Optional.empty()
            }
        }

        @FieldOrder("t", "is_some")
        open class OptionTaikoDifficultyAttributes : Structure() {
            @JvmField var t: TaikoDifficultyAttributes? = null // Element that is maybe valid
            @JvmField var is_some: Byte = 0 // 1 means element t is valid

            class ByReference : OptionTaikoDifficultyAttributes(), Structure.ByReference
            class ByValue : OptionTaikoDifficultyAttributes(), Structure.ByValue

            fun toOptional(): Optional<TaikoDifficultyAttributes> {
                return if (is_some.toInt() == 1) Optional.of(t!!) else Optional.empty()
            }
        }

        @FieldOrder("t", "is_some")
        open class OptionCatchDifficultyAttributes : Structure() {
            @JvmField var t: CatchDifficultyAttributes? = null // Element that is maybe valid
            @JvmField var is_some: Byte = 0 // 1 means element t is valid

            class ByReference : OptionCatchDifficultyAttributes(), Structure.ByReference
            class ByValue : OptionCatchDifficultyAttributes(), Structure.ByValue

            fun toOptional(): Optional<CatchDifficultyAttributes> {
                return if (is_some.toInt() == 1) Optional.of(t!!) else Optional.empty()
            }
        }

        @FieldOrder("t", "is_some")
        open class OptionManiaDifficultyAttributes : Structure() {
            @JvmField var t: ManiaDifficultyAttributes? = null // Element that is maybe valid
            @JvmField var is_some: Byte = 0 // 1 means element t is valid

            class ByReference : OptionManiaDifficultyAttributes(), Structure.ByReference
            class ByValue : OptionManiaDifficultyAttributes(), Structure.ByValue

            fun toOptional(): Optional<ManiaDifficultyAttributes> {
                return if (is_some.toInt() == 1) Optional.of(t!!) else Optional.empty()
            }
        }

        @FieldOrder("osu", "taiko", "fruit", "mania", "mode")
        open class DifficultyAttributes : Structure() {
            @JvmField var osu: OptionOsuDifficultyAttributes? = null // Option for osu!difficulty attributes
            @JvmField var taiko: OptionTaikoDifficultyAttributes? = null // Option for taiko difficulty attributes
            @JvmField var fruit: OptionCatchDifficultyAttributes? = null // Option for catch difficulty attributes
            @JvmField var mania: OptionManiaDifficultyAttributes? = null // Option for mania difficulty attributes
            @JvmField var mode: Int = 0 // Mode enum (osu!, taiko, catch, mania)

            class ByReference : DifficultyAttributes(), Structure.ByReference
            class ByValue : DifficultyAttributes(), Structure.ByValue
        }

        @FieldOrder("t", "is_some")
        open class OptionOsuPerformanceAttributes : Structure() {
            @JvmField var t: OsuPerformanceAttributes? = null // Element that is maybe valid
            @JvmField var is_some: Byte = 0 // 1 means element t is valid

            class ByReference : OptionOsuPerformanceAttributes(), Structure.ByReference
            class ByValue : OptionOsuPerformanceAttributes(), Structure.ByValue

            fun toOptional(): Optional<OsuPerformanceAttributes> {
                return if (is_some.toInt() == 1) Optional.of(t!!) else Optional.empty()
            }
        }

        @FieldOrder("t", "is_some")
        open class OptionTaikoPerformanceAttributes : Structure() {
            @JvmField var t: TaikoPerformanceAttributes? = null // Element that is maybe valid
            @JvmField var is_some: Byte = 0 // 1 means element t is valid

            class ByReference : OptionTaikoPerformanceAttributes(), Structure.ByReference
            class ByValue : OptionTaikoPerformanceAttributes(), Structure.ByValue

            fun toOptional(): Optional<TaikoPerformanceAttributes> {
                return if (is_some.toInt() == 1) Optional.of(t!!) else Optional.empty()
            }
        }

        @FieldOrder("t", "is_some")
        open class OptionCatchPerformanceAttributes : Structure() {
            @JvmField var t: CatchPerformanceAttributes? = null // Element that is maybe valid
            @JvmField var is_some: Byte = 0 // 1 means element t is valid

            class ByReference : OptionCatchPerformanceAttributes(), Structure.ByReference
            class ByValue : OptionCatchPerformanceAttributes(), Structure.ByValue

            fun toOptional(): Optional<CatchPerformanceAttributes> {
                return if (is_some.toInt() == 1) Optional.of(t!!) else Optional.empty()
            }
        }

        @FieldOrder("t", "is_some")
        open class OptionManiaPerformanceAttributes : Structure() {
            @JvmField var t: ManiaPerformanceAttributes? = null // Element that is maybe valid
            @JvmField var is_some: Byte = 0 // 1 means element t is valid

            class ByReference : OptionManiaPerformanceAttributes(), Structure.ByReference
            class ByValue : OptionManiaPerformanceAttributes(), Structure.ByValue

            fun toOptional(): Optional<ManiaPerformanceAttributes> {
                return if (is_some.toInt() == 1) Optional.of(t!!) else Optional.empty()
            }
        }

        @FieldOrder("osu", "taiko", "fruit", "mania", "mode")
        open class PerformanceAttributes : Structure() {
            @JvmField var osu: OptionOsuPerformanceAttributes? = null // Option for osu!difficulty attributes
            @JvmField var taiko: OptionTaikoPerformanceAttributes? = null // Option for taiko difficulty attributes
            @JvmField var fruit: OptionCatchPerformanceAttributes? = null // Option for catch difficulty attributes
            @JvmField var mania: OptionManiaPerformanceAttributes? = null // Option for mania difficulty attributes
            @JvmField var mode: Int = 0 // Mode enum (osu!, taiko, catch, mania)

            class ByReference : PerformanceAttributes(), Structure.ByReference
            class ByValue : PerformanceAttributes(), Structure.ByValue
        }

        @FieldOrder("ar", "od_great", "od_ok")
        open class HitWindows : Structure() {
            /** Hit window for approach rate i.e. `TimePreempt` in milliseconds. */
            @JvmField var ar: Double = 0.0

            /** Hit window for overall difficulty i.e. time to hit a 300 ("Great") in milliseconds. */
            @JvmField var od_great: Double = 0.0

            /** Hit window for overall difficulty i.e. time to hit a 100 ("Ok") in milliseconds.
             *
             * `None` for osu!mania. */
            @JvmField var od_ok: Optionf64? = null

            class ByReference : HitWindows(), Structure.ByReference
            class ByValue : HitWindows(), Structure.ByValue
        }

        @FieldOrder("ar", "od", "cs", "hp", "clock_rate", "hit_windows")
        open class BeatmapAttributes : Structure() {
            @JvmField var ar: Double = 0.0 // Approach rate
            @JvmField var od: Double = 0.0 // Overall difficulty
            @JvmField var cs: Double = 0.0 // Circle size
            @JvmField var hp: Double = 0.0 // Health drain rate
            @JvmField var clock_rate: Double = 0.0 // Clock rate with respect to mods
            @JvmField var hit_windows: HitWindows? = null // Nested hit windows structure

            class ByReference : BeatmapAttributes(), Structure.ByReference
            class ByValue : BeatmapAttributes(), Structure.ByValue
        }

        @FieldOrder(
            "max_combo",
            "slider_tick_hits",
            "slider_tick_misses",
            "slider_end_hits",
            "n_geki",
            "n_katu",
            "n300",
            "n100",
            "n50",
            "misses"
        )
        open class ScoreState : Structure() {
            @JvmField var max_combo: Int = 0 // Maximum combo (unsigned int -> int)
            @JvmField var slider_tick_hits: Int = 0 // Hits on slider ticks (unsigned int -> int)
            @JvmField var slider_tick_misses: Int = 0 // Misses on slider ticks (unsigned int -> int)
            @JvmField var slider_end_hits: Int = 0 // Hits on slider ends (unsigned int -> int)
            @JvmField var n_geki: Int = 0 // Current gekis (unsigned int -> int)
            @JvmField var n_katu: Int = 0 // Current katus (unsigned int -> int)
            @JvmField var n300: Int = 0 // Current 300s (unsigned int -> int)
            @JvmField var n100: Int = 0 // Current 100s (unsigned int -> int)
            @JvmField var n50: Int = 0 // Current 50s (unsigned int -> int)
            @JvmField var misses: Int = 0 // Current misses (unsigned int -> int)

            class ByReference : ScoreState(), Structure.ByReference
            class ByValue : ScoreState(), Structure.ByValue
        }

        companion object {
            // JNA 为 dll 名称
            val INSTANCE: RosuPPLib = Native.load("rosu_pp_ffi", RosuPPLib::class.java)
        }
    }

    class Beatmap : AutoCloseable {
        private val _context: PointerByReference // The context of the Beatmap

        // Load the Beatmap from bytes
        constructor(data: ByteArray) {
            _context = PointerByReference() // Initialize _context to a valid Pointer
            val sliceu8 = RosuPPLib.Sliceu8(data)
            val rval = RosuPPLib.INSTANCE.beatmap_from_bytes(_context, sliceu8)
            if (rval != FFIError.OK) {
                throw RuntimeException("Error loading beatmap from bytes")
            }
        }

        constructor(data: RosuPPLib.Sliceu8) {
            _context = PointerByReference() // Initialize _context to a valid Pointer
            val rval = RosuPPLib.INSTANCE.beatmap_from_bytes(_context, data)
            if (rval != FFIError.OK) {
                throw RuntimeException("Error loading beatmap from bytes")
            }
        }


        // Load the Beatmap from a file path
        constructor(path: String) {
            _context = PointerByReference() // Initialize _context to a valid Pointer
            val rval = RosuPPLib.INSTANCE.beatmap_from_path(_context, path)
            if (rval != FFIError.OK) {
                throw RuntimeException("Error loading beatmap from path")
            }
        }

        // Convert the Beatmap to the specified mode
        fun convert(mode: Mode): Boolean {
            return RosuPPLib.INSTANCE.beatmap_convert(context, mode.value)
        }

        // Get the BPM of the Beatmap
        fun bpm(): Double {
            return RosuPPLib.INSTANCE.beatmap_bpm(context)
        }

        // Get the total break time of the Beatmap
        fun totalBreakTime(): Double {
            return RosuPPLib.INSTANCE.beatmap_total_break_time(context)
        }

        // Get the mode of the Beatmap
        fun mode(): Mode {
            return Mode.fromValue(RosuPPLib.INSTANCE.beatmap_mode(context))
        }

        val isConvert: Boolean
            // Check if the Beatmap is a converted map
            get() = RosuPPLib.INSTANCE.beatmap_is_convert(context)

        val context: Pointer
            // Getter for the context
            get() = _context.value

        // Dispose method (releases the resources)
        override fun close() {
            val rval = RosuPPLib.INSTANCE.beatmap_destroy(_context)
            if (rval != 0) {
                throw RuntimeException("Error destroying beatmap")
            }
        }
    }

    class BeatmapAttributesBuilder : AutoCloseable {
        private val _context = PointerByReference() // Context for BeatmapAttributesBuilder

        init {
            val rval = RosuPPLib.INSTANCE.beatmap_attributes_new(_context)
            if (rval != FFIError.OK) {
                throw RuntimeException("Error creating BeatmapAttributesBuilder")
            }
        }

        // Method to dispose of the builder
        override fun close() {
            val rval = RosuPPLib.INSTANCE.beatmap_attributes_destroy(_context)
            if (rval != FFIError.OK) {
                throw RuntimeException("Error destroying BeatmapAttributesBuilder")
            }
        }

        // Method to set the mode
        fun setMode(mode: Mode) {
            RosuPPLib.INSTANCE.beatmap_attributes_mode(context, mode.value)
        }

        // Method to set mods (using IntPtr)
        fun setMods(mods: Mods) {
            RosuPPLib.INSTANCE.beatmap_attributes_p_mods(context, mods.context)
        }

        // Method to set mods (using uint)
        fun setMods(mods: Int) {
            RosuPPLib.INSTANCE.beatmap_attributes_i_mods(context, mods.toLong())
        }

        // Method to set mods (using string)
        fun setMods(str: String) {
            val rval = RosuPPLib.INSTANCE.beatmap_attributes_s_mods(context, str)
            if (rval != FFIError.OK) {
                throw RuntimeException("Error setting string mods")
            }
        }

        // Method to set AR (approach rate)
        fun setAr(ar: Float) {
            RosuPPLib.INSTANCE.beatmap_attributes_ar(context, ar)
        }

        // Method to set CS (circle size)
        fun setCs(cs: Float) {
            RosuPPLib.INSTANCE.beatmap_attributes_cs(context, cs)
        }

        // Method to set HP (health drain rate)
        fun setHp(hp: Float) {
            RosuPPLib.INSTANCE.beatmap_attributes_hp(context, hp)
        }

        // Method to set OD (overall difficulty)
        fun setOd(od: Float) {
            RosuPPLib.INSTANCE.beatmap_attributes_od(context, od)
        }

        // Method to set clock rate
        fun setClockRate(clockRate: Double) {
            RosuPPLib.INSTANCE.beatmap_attributes_clock_rate(context, clockRate)
        }

        val clockRate: Double
            // Method to get clock rate
            get() = RosuPPLib.INSTANCE.beatmap_attributes_get_clock_rate(context)

        // Method to build BeatmapAttributes
        fun build(beatmap: Beatmap): RosuPPLib.BeatmapAttributes {
            return RosuPPLib.INSTANCE.beatmap_attributes_build(context, beatmap.context)
        }

        @Suppress("MemberVisibilityCanBePrivate")
        val context: Pointer
            // Getter for the context
            get() = _context.value
    }

    class Difficulty : AutoCloseable {
        private val _context = PointerByReference()

        init {
            val rval = RosuPPLib.INSTANCE.difficulty_new(_context)
            if (rval != 0) {
                throw RuntimeException("Error creating Difficulty")
            }
        }

        // Method to dispose of the Difficulty
        override fun close() {
            val rval = RosuPPLib.INSTANCE.difficulty_destroy(_context)
            if (rval != 0) {
                throw RuntimeException("Error destroying Difficulty")
            }
        }

        // Method to set p_mods (using Pointer)
        fun setMods(mods: Mods) {
            RosuPPLib.INSTANCE.difficulty_p_mods(context, mods.context)
        }

        // Method to set i_mods (using uint)
        fun setMods(mods: Int) {
            RosuPPLib.INSTANCE.difficulty_i_mods(context, mods.toLong())
        }

        // Method to set s_mods (using string)
        fun setMods(str: String) {
            val rval = RosuPPLib.INSTANCE.difficulty_s_mods(context, str)
            if (rval != 0) {
                throw RuntimeException("Error setting string mods")
            }
        }

        // Method to set passed objects (using uint)
        fun setPassedObjects(passedObjects: Int) {
            RosuPPLib.INSTANCE.difficulty_passed_objects(context, passedObjects.toLong())
        }

        // Method to set AR (approach rate)
        fun setAr(ar: Float) {
            RosuPPLib.INSTANCE.difficulty_ar(context, ar)
        }

        // Method to set CS (circle size)
        fun setCs(cs: Float) {
            RosuPPLib.INSTANCE.difficulty_cs(context, cs)
        }

        // Method to set HP (health drain)
        fun setHp(hp: Float) {
            RosuPPLib.INSTANCE.difficulty_hp(context, hp)
        }

        // Method to set OD (overall difficulty)
        fun setOd(od: Float) {
            RosuPPLib.INSTANCE.difficulty_od(context, od)
        }

        // Method to set hardrock offsets
        fun setHardrockOffsets(hardrockOffsets: Boolean) {
            RosuPPLib.INSTANCE.difficulty_hardrock_offsets(context, hardrockOffsets)
        }

        // Method to set lazer
        fun setLazer(lazer: Boolean) {
            RosuPPLib.INSTANCE.difficulty_lazer(context, lazer)
        }

        // Method to calculate DifficultyAttributes from beatmap
        fun calculate(beatmap: Beatmap): RosuPPLib.DifficultyAttributes {
            return RosuPPLib.INSTANCE.difficulty_calculate(context, beatmap.context)
        }

        // Method to set clock rate
        fun setClockRate(clockRate: Double) {
            RosuPPLib.INSTANCE.difficulty_clock_rate(context, clockRate)
        }

        val clockRate: Double
            // Method to get clock rate
            get() = RosuPPLib.INSTANCE.difficulty_get_clock_rate(context)

        @Suppress("MemberVisibilityCanBePrivate")
        val context: Pointer
            // Getter for context
            get() = _context.value
    }

    class Performance : AutoCloseable {
        private val _context = PointerByReference()

        init {
            val rval = RosuPPLib.INSTANCE.performance_new(_context)
            if (rval != 0) {
                throw RuntimeException("Error creating Performance")
            }
        }

        // Method to dispose of the Performance
        override fun close() {
            val rval = RosuPPLib.INSTANCE.performance_destroy(_context)
            if (rval != 0) {
                throw RuntimeException("Error destroying Performance")
            }
        }

        // Method to set mode
        fun setMode(mode: Mode) {
            RosuPPLib.INSTANCE.performance_mode(context, mode.value)
        }

        // Method to set p_mods (using Pointer)
        fun setMods(mods: Mods) {
            RosuPPLib.INSTANCE.performance_p_mods(context, mods.context)
        }

        // Method to set i_mods (using uint)
        fun setMods(mods: Int) {
            RosuPPLib.INSTANCE.performance_i_mods(context, mods.toLong())
        }

        // Method to set s_mods (using string)
        fun setMods(str: String) {
            val rval = RosuPPLib.INSTANCE.performance_s_mods(context, str)
            if (rval != 0) {
                throw RuntimeException("Error setting string mods")
            }
        }

        // Method to set passed objects (using uint)
        fun setPassedObjects(passedObjects: Int) {
            RosuPPLib.INSTANCE.performance_passed_objects(context, passedObjects.toLong())
        }

        // Method to set AR (approach rate)
        fun setAr(ar: Float) {
            RosuPPLib.INSTANCE.performance_ar(context, ar)
        }

        // Method to set CS (circle size)
        fun setCs(cs: Float) {
            RosuPPLib.INSTANCE.performance_cs(context, cs)
        }

        // Method to set HP (health drain)
        fun setHp(hp: Float) {
            RosuPPLib.INSTANCE.performance_hp(context, hp)
        }

        // Method to set OD (overall difficulty)
        fun setOd(od: Float) {
            RosuPPLib.INSTANCE.performance_od(context, od)
        }

        // Method to set hardrock offsets
        fun setHardrockOffsets(hardrockOffsets: Boolean) {
            RosuPPLib.INSTANCE.performance_hardrock_offsets(context, hardrockOffsets)
        }

        // Method to set hardrock offsets
        fun setHitResultPriority(hitresultPriority: Int) {
            RosuPPLib.INSTANCE.performance_hitresult_priority(context, hitresultPriority)
        }

        fun setCombo(combo: Long) {
            RosuPPLib.INSTANCE.performance_combo(context, combo)
        }

        fun setAccuracy(accuracy: Double) {
            RosuPPLib.INSTANCE.performance_accuracy(context, accuracy)
        }

        fun setMisses(misses: Long) {
            RosuPPLib.INSTANCE.performance_misses(context, misses)
        }

        fun setSliderTickHits(sliderTickHits: Long) {
            RosuPPLib.INSTANCE.performance_slider_tick_hits(context, sliderTickHits)
        }

        fun setSliderTickMisses(sliderTickMisses: Long) {
            RosuPPLib.INSTANCE.performance_slider_tick_misses(context, sliderTickMisses)
        }

        fun setSliderEndHits(sliderEndHits: Long) {
            RosuPPLib.INSTANCE.performance_slider_end_hits(context, sliderEndHits)
        }

        fun setN300(n300: Long) {
            RosuPPLib.INSTANCE.performance_n300(context, n300)
        }

        fun setN100(n100: Long) {
            RosuPPLib.INSTANCE.performance_n100(context, n100)
        }

        fun setN50(n50: Long) {
            RosuPPLib.INSTANCE.performance_n50(context, n50)
        }

        fun setNKatu(nKatu: Long) {
            RosuPPLib.INSTANCE.performance_n_katu(context, nKatu)
        }

        fun setNGeki(nGeki: Long) {
            RosuPPLib.INSTANCE.performance_n_geki(context, nGeki)
        }

        // Method to set lazer
        fun setLazer(lazer: Boolean) {
            RosuPPLib.INSTANCE.performance_lazer(context, lazer)
        }

        fun generateState(beatmap: Beatmap): RosuPPLib.ScoreState {
            return RosuPPLib.INSTANCE.performance_generate_state(context, beatmap.context)
        }

        // Method to calculate PerformanceAttributes from beatmap
        fun calculate(beatmap: Beatmap): RosuPPLib.PerformanceAttributes {
            return RosuPPLib.INSTANCE.performance_calculate(context, beatmap.context)
        }

        // Method to calculate PerformanceAttributes from DifficultyAttributes
        fun calculateFromDifficulty(difficultyAttributes: RosuPPLib.DifficultyAttributes): RosuPPLib.PerformanceAttributes {
            return RosuPPLib.INSTANCE.performance_calculate_from_difficulty(context, difficultyAttributes as RosuPPLib.DifficultyAttributes.ByValue)
        }

        // Method to set clock rate
        fun setClockRate(clockRate: Double) {
            RosuPPLib.INSTANCE.performance_clock_rate(context, clockRate)
        }

        val clockRate: Double
            // Method to get clock rate
            get() = RosuPPLib.INSTANCE.performance_get_clock_rate(context)

        @Suppress("MemberVisibilityCanBePrivate")
        val context: Pointer
            // Getter for context
            get() = _context.value
    }

    class Mods private constructor() {
        @Suppress("unused")
        private val cleanable: Cleaner.Cleanable

        private val _context = PointerByReference() // Context for BeatmapAttributesBuilder

        init {
            this.cleanable = cleaner.register(this, cleanAction(_context))
        }

        fun removeIncompatibleMods() {
            RosuPPLib.INSTANCE.mods_remove_incompatible_mods(context)
        }

        val bits: Long
            get() = RosuPPLib.INSTANCE.mods_bits(context)

        val length: Long
            get() = RosuPPLib.INSTANCE.mods_len(context)

        fun toJson(): OwnedString {
            val s = OwnedString()
            RosuPPLib.INSTANCE.mods_json(context, s.context)
            return s
        }

        fun insertJson(mod: String): Boolean {
            return RosuPPLib.INSTANCE.mods_insert_json(context, mod)
        }

        fun insert(mod: String): Boolean {
            return RosuPPLib.INSTANCE.mods_insert(context, mod)
        }

        fun contains(mod: String): Boolean {
            return RosuPPLib.INSTANCE.mods_contains(context, mod)
        }

        fun clear() {
            RosuPPLib.INSTANCE.mods_clear(context)
        }

        val clockRate: RosuPPLib.Optionf64
            get() = RosuPPLib.INSTANCE.mods_clock_rate(context)

        val context: Pointer
            // Getter for the context
            get() = _context.value

        companion object {
            private val cleaner: Cleaner = Cleaner.create()
            private fun cleanAction(context: PointerByReference): Runnable {
                return Runnable {
                    val rval = RosuPPLib.INSTANCE.mods_destroy(context)
                    if (rval != FFIError.OK) {
                        throw RuntimeException("Error destroying Mods")
                    }
                }
            }

            /** new */
            fun new(mode: Mode): Mods {
                val m = Mods()
                val rval = RosuPPLib.INSTANCE.mods_new(m._context, mode.value)
                if (rval != FFIError.OK) {
                    throw RuntimeException("Error creating Mods")
                }
                return m
            }

            /** from acronyms */
            fun fromAcronyms(mods: String, mode: Mode): Mods {
                val m = Mods()
                val rval = RosuPPLib.INSTANCE.mods_from_acronyms(m._context, mods, mode.value)
                if (rval != FFIError.OK) {
                    throw RuntimeException("Error creating Mods")
                }
                return m
            }

            /** from bits */
            fun fromBits(mods: Long, mode: Mode): Mods {
                val m = Mods()
                val rval = RosuPPLib.INSTANCE.mods_from_bits(m._context, mods, mode.value)
                if (rval != FFIError.OK) {
                    throw RuntimeException("Error creating Mods")
                }
                return m
            }

            /** from json */
            fun fromJson(mods: String, mode: Mode): Mods {
                val m = Mods()
                val rval = RosuPPLib.INSTANCE.mods_from_json(m._context, mods, mode.value)
                if (rval != FFIError.OK) {
                    throw RuntimeException("Error creating Mods")
                }
                return m
            }

            /** from json sanitize */
            fun fromJsonSanitize(mods: String, mode: Mode): Mods {
                val m = Mods()
                val rval = RosuPPLib.INSTANCE.mods_from_json_sanitize(m._context, mods, mode.value)
                if (rval != FFIError.OK) {
                    throw RuntimeException("Error creating Mods")
                }
                return m
            }
        }
    }


    class OwnedString {
        @Suppress("unused")
        private val cleanable: Cleaner.Cleanable

        private val _context: PointerByReference // Context for BeatmapAttributesBuilder

        constructor() {
            _context = PointerByReference()
            val rval = RosuPPLib.INSTANCE.string_empty(_context)
            if (rval != FFIError.OK) {
                throw RuntimeException("Error creating OwnedString")
            }
            this.cleanable = cleaner.register(this, cleanAction(_context))
        }

        constructor(str: String) {
            _context = PointerByReference()
            val rval = RosuPPLib.INSTANCE.string_from_c_str(_context, str)
            if (rval != FFIError.OK) {
                throw RuntimeException("Error creating OwnedString")
            }
            this.cleanable = cleaner.register(this, cleanAction(_context))
        }

        @Suppress("MemberVisibilityCanBePrivate")
        fun toCstr(): String {
            return RosuPPLib.INSTANCE.string_to_cstr(context)
        }

        @Suppress("MemberVisibilityCanBePrivate")
        val isInit: Boolean
            get() = RosuPPLib.INSTANCE.string_is_init(context)

        override fun toString(): String {
            return if (isInit) toCstr() else ""
        }

        val context: Pointer
            // Getter for the context
            get() = _context.value

        companion object {
            private val cleaner: Cleaner = Cleaner.create()
            private fun cleanAction(context: PointerByReference): Runnable {
                return Runnable {
                    val rval = RosuPPLib.INSTANCE.string_destroy(context)
                    if (rval != FFIError.OK) {
                        throw RuntimeException("Error destroying Mods")
                    }
                }
            }
        }
    }

    enum class Mode(val value: Int) {
        OSU(0),
        TAIKO(1),
        CATCH(2),
        MANIA(3);

        companion object {
            fun fromValue(value: Int): Mode {
                for (mode in entries) {
                    if (mode.value == value) {
                        return mode
                    }
                }
                throw IllegalArgumentException("Unknown mode value: $value")
            }
        }
    }
}