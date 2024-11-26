// Automatically generated by Interoptopus.

#ifndef rosu_pp
#define rosu_pp

#ifdef __cplusplus
extern "C" {
#endif

#include <stdint.h>
#include <stdbool.h>




typedef enum hitresultpriority
    {
    HITRESULTPRIORITY_BESTCASE = 0,
    HITRESULTPRIORITY_WORSTCASE = 1,
    } hitresultpriority;

typedef enum mode
    {
    /// osu!standard
    MODE_OSU = 0,
    /// osu!taiko
    MODE_TAIKO = 1,
    /// osu!catch
    MODE_CATCH = 2,
    /// osu!mania
    MODE_MANIA = 3,
    } mode;

/// Type to pass [`OsuScoreState::accuracy`] and specify the origin of a score.
typedef enum osuscoreorigin
    {
    /// For scores set on osu!stable
    OSUSCOREORIGIN_STABLE = 0,
    /// For scores set on osu!lazer with slider accuracy
    OSUSCOREORIGIN_WITHSLIDERACC = 1,
    /// For scores set on osu!lazer without slider accuracy
    OSUSCOREORIGIN_WITHOUTSLIDERACC = 2,
    } osuscoreorigin;

typedef struct beatmap beatmap;

typedef struct beatmapattributesbuilder beatmapattributesbuilder;

typedef struct difficulty difficulty;

typedef struct mods mods;

typedef struct ownedstring ownedstring;

typedef struct performance performance;

typedef enum ffierror
    {
    FFIERROR_OK = 0,
    FFIERROR_NULL = 100,
    FFIERROR_PANIC = 200,
    FFIERROR_IOERROR = 300,
    FFIERROR_UTF8ERROR = 400,
    FFIERROR_INVALIDSTRING = 500,
    FFIERROR_SERIALIZEERROR = 600,
    FFIERROR_UNKNOWN = 1000,
    } ffierror;

/// The result of a difficulty calculation on an osu!catch map.
typedef struct catchdifficultyattributes
    {
    /// The final star rating
    double stars;
    /// The approach rate.
    double ar;
    /// The amount of fruits.
    uint32_t n_fruits;
    /// The amount of droplets.
    uint32_t n_droplets;
    /// The amount of tiny droplets.
    uint32_t n_tiny_droplets;
    /// Whether the [`Beatmap`] was a convert i.e. an osu!standard map.
    ///
    /// [`Beatmap`]: crate::model::beatmap::Beatmap
    uint8_t is_convert;
    } catchdifficultyattributes;

/// The result of a difficulty calculation on an osu!mania map.
typedef struct maniadifficultyattributes
    {
    /// The final star rating.
    double stars;
    /// The perceived hit window for an n300 inclusive of rate-adjusting mods (DT/HT/etc).
    double hit_window;
    /// The amount of hitobjects in the map.
    uint32_t n_objects;
    /// The amount of hold notes in the map.
    uint32_t n_hold_notes;
    /// The maximum achievable combo.
    uint32_t max_combo;
    /// Whether the [`Beatmap`] was a convert i.e. an osu!standard map.
    ///
    /// [`Beatmap`]: crate::model::beatmap::Beatmap
    uint8_t is_convert;
    } maniadifficultyattributes;

/// The result of a difficulty calculation on an osu!standard map.
typedef struct osudifficultyattributes
    {
    /// The difficulty of the aim skill.
    double aim;
    /// The difficulty of the speed skill.
    double speed;
    /// The difficulty of the flashlight skill.
    double flashlight;
    /// The ratio of the aim strain with and without considering sliders
    double slider_factor;
    /// The number of clickable objects weighted by difficulty.
    double speed_note_count;
    /// Weighted sum of aim strains.
    double aim_difficult_strain_count;
    /// Weighted sum of speed strains.
    double speed_difficult_strain_count;
    /// The approach rate.
    double ar;
    /// The overall difficulty
    double od;
    /// The health drain rate.
    double hp;
    /// The amount of circles.
    uint32_t n_circles;
    /// The amount of sliders.
    uint32_t n_sliders;
    /// The amount of "large ticks".
    ///
    /// The meaning depends on the kind of score:
    /// - if set on osu!stable, this value is irrelevant
    /// - if set on osu!lazer *without* `CL`, this value is the amount of
    ///   slider ticks and repeats
    /// - if set on osu!lazer *with* `CL`, this value is the amount of slider
    ///   heads, ticks, and repeats
    uint32_t n_large_ticks;
    /// The amount of spinners.
    uint32_t n_spinners;
    /// The final star rating
    double stars;
    /// The maximum combo.
    uint32_t max_combo;
    } osudifficultyattributes;

/// Aggregation for a score's current state.
typedef struct scorestate
    {
    /// Maximum combo that the score has had so far. **Not** the maximum
    /// possible combo of the map so far.
    ///
    /// Note that for osu!catch only fruits and droplets are considered for
    /// combo.
    ///
    /// Irrelevant for osu!mania.
    uint32_t max_combo;
    /// "Large tick" hits for osu!standard.
    ///
    /// The meaning depends on the kind of score:
    /// - if set on osu!stable, this field is irrelevant and can be `0`
    /// - if set on osu!lazer *without* `CL`, this field is the amount of hit
    ///   slider ticks and repeats
    /// - if set on osu!lazer *with* `CL`, this field is the amount of hit
    ///   slider heads, ticks, and repeats
    uint32_t osu_large_tick_hits;
    /// Amount of successfully hit slider ends.
    ///
    /// Only relevant for osu!standard in lazer.
    uint32_t slider_end_hits;
    /// Amount of current gekis (n320 for osu!mania).
    uint32_t n_geki;
    /// Amount of current katus (tiny droplet misses for osu!catch / n200 for
    /// osu!mania).
    uint32_t n_katu;
    /// Amount of current 300s (fruits for osu!catch).
    uint32_t n300;
    /// Amount of current 100s (droplets for osu!catch).
    uint32_t n100;
    /// Amount of current 50s (tiny droplets for osu!catch).
    uint32_t n50;
    /// Amount of current misses (fruits + droplets for osu!catch).
    uint32_t misses;
    } scorestate;

/// The result of a difficulty calculation on an osu!taiko map.
typedef struct taikodifficultyattributes
    {
    /// The difficulty of the stamina skill.
    double stamina;
    /// The difficulty of the rhythm skill.
    double rhythm;
    /// The difficulty of the color skill.
    double color;
    /// The difficulty of the hardest parts of the map.
    double peak;
    /// The perceived hit window for an n300 inclusive of rate-adjusting mods (DT/HT/etc)
    double great_hit_window;
    /// The perceived hit window for an n100 inclusive of rate-adjusting mods (DT/HT/etc)
    double ok_hit_window;
    /// The ratio of stamina difficulty from mono-color (single color) streams to total
    /// stamina difficulty.
    double mono_stamina_factor;
    /// The final star rating.
    double stars;
    /// The maximum combo.
    uint32_t max_combo;
    /// Whether the [`Beatmap`] was a convert i.e. an osu!standard map.
    ///
    /// [`Beatmap`]: crate::model::beatmap::Beatmap
    uint8_t is_convert;
    } taikodifficultyattributes;

///Option type containing boolean flag and maybe valid data.
typedef struct optionf64
    {
    ///Element that is maybe valid.
    double t;
    ///Byte where `1` means element `t` is valid.
    uint8_t is_some;
    } optionf64;

/// The result of a performance calculation on an osu!catch map.
typedef struct catchperformanceattributes
    {
    /// The difficulty attributes that were used for the performance calculation
    catchdifficultyattributes difficulty;
    /// The final performance points.
    double pp;
    } catchperformanceattributes;

/// AR and OD hit windows
typedef struct hitwindows
    {
    /// Hit window for approach rate i.e. `TimePreempt` in milliseconds.
    double ar;
    /// Hit window for overall difficulty i.e. time to hit a 300 ("Great") in milliseconds.
    double od_great;
    /// Hit window for overall difficulty i.e. time to hit a 100 ("Ok") in milliseconds.
    ///
    /// `None` for osu!mania.
    optionf64 od_ok;
    } hitwindows;

/// The result of a performance calculation on an osu!mania map.
typedef struct maniaperformanceattributes
    {
    /// The difficulty attributes that were used for the performance calculation.
    maniadifficultyattributes difficulty;
    /// The final performance points.
    double pp;
    /// The difficulty portion of the final pp.
    double pp_difficulty;
    } maniaperformanceattributes;

/// The result of a performance calculation on an osu!standard map.
typedef struct osuperformanceattributes
    {
    /// The difficulty attributes that were used for the performance calculation
    osudifficultyattributes difficulty;
    /// The final performance points.
    double pp;
    /// The accuracy portion of the final pp.
    double pp_acc;
    /// The aim portion of the final pp.
    double pp_aim;
    /// The flashlight portion of the final pp.
    double pp_flashlight;
    /// The speed portion of the final pp.
    double pp_speed;
    /// Misses including an approximated amount of slider breaks
    double effective_miss_count;
    } osuperformanceattributes;

/// The result of a performance calculation on an osu!taiko map.
typedef struct taikoperformanceattributes
    {
    /// The difficulty attributes that were used for the performance calculation
    taikodifficultyattributes difficulty;
    /// The final performance points.
    double pp;
    /// The accuracy portion of the final pp.
    double pp_acc;
    /// The strain portion of the final pp.
    double pp_difficulty;
    /// Scaled miss count based on total hits.
    double effective_miss_count;
    /// Upper bound on the player's tap deviation.
    optionf64 estimated_unstable_rate;
    } taikoperformanceattributes;

///A pointer to an array of data someone else owns which may not be modified.
typedef struct sliceu8
    {
    ///Pointer to start of immutable data.
    const uint8_t* data;
    ///Number of elements.
    uint64_t len;
    } sliceu8;

///Option type containing boolean flag and maybe valid data.
typedef struct optioncatchdifficultyattributes
    {
    ///Element that is maybe valid.
    catchdifficultyattributes t;
    ///Byte where `1` means element `t` is valid.
    uint8_t is_some;
    } optioncatchdifficultyattributes;

///Option type containing boolean flag and maybe valid data.
typedef struct optionmaniadifficultyattributes
    {
    ///Element that is maybe valid.
    maniadifficultyattributes t;
    ///Byte where `1` means element `t` is valid.
    uint8_t is_some;
    } optionmaniadifficultyattributes;

///Option type containing boolean flag and maybe valid data.
typedef struct optionosudifficultyattributes
    {
    ///Element that is maybe valid.
    osudifficultyattributes t;
    ///Byte where `1` means element `t` is valid.
    uint8_t is_some;
    } optionosudifficultyattributes;

///Option type containing boolean flag and maybe valid data.
typedef struct optiontaikodifficultyattributes
    {
    ///Element that is maybe valid.
    taikodifficultyattributes t;
    ///Byte where `1` means element `t` is valid.
    uint8_t is_some;
    } optiontaikodifficultyattributes;

/// Summary struct for a [`Beatmap`]'s attributes.
typedef struct beatmapattributes
    {
    /// The approach rate.
    double ar;
    /// The overall difficulty.
    double od;
    /// The circle size.
    double cs;
    /// The health drain rate
    double hp;
    /// The clock rate with respect to mods.
    double clock_rate;
    /// The hit windows for approach rate and overall difficulty.
    hitwindows hit_windows;
    } beatmapattributes;

typedef struct difficultyattributes
    {
    optionosudifficultyattributes osu;
    optiontaikodifficultyattributes taiko;
    optioncatchdifficultyattributes fruit;
    optionmaniadifficultyattributes mania;
    mode mode;
    } difficultyattributes;

///Option type containing boolean flag and maybe valid data.
typedef struct optioncatchperformanceattributes
    {
    ///Element that is maybe valid.
    catchperformanceattributes t;
    ///Byte where `1` means element `t` is valid.
    uint8_t is_some;
    } optioncatchperformanceattributes;

///Option type containing boolean flag and maybe valid data.
typedef struct optionmaniaperformanceattributes
    {
    ///Element that is maybe valid.
    maniaperformanceattributes t;
    ///Byte where `1` means element `t` is valid.
    uint8_t is_some;
    } optionmaniaperformanceattributes;

///Option type containing boolean flag and maybe valid data.
typedef struct optionosuperformanceattributes
    {
    ///Element that is maybe valid.
    osuperformanceattributes t;
    ///Byte where `1` means element `t` is valid.
    uint8_t is_some;
    } optionosuperformanceattributes;

///Option type containing boolean flag and maybe valid data.
typedef struct optiontaikoperformanceattributes
    {
    ///Element that is maybe valid.
    taikoperformanceattributes t;
    ///Byte where `1` means element `t` is valid.
    uint8_t is_some;
    } optiontaikoperformanceattributes;

typedef struct performanceattributes
    {
    optionosuperformanceattributes osu;
    optiontaikoperformanceattributes taiko;
    optioncatchperformanceattributes fruit;
    optionmaniaperformanceattributes mania;
    mode mode;
    } performanceattributes;


/// Destroys the given instance.
///
/// # Safety
///
/// The passed parameter MUST have been created with the corresponding init function;
/// passing any other value results in undefined behavior.
ffierror beatmap_attributes_destroy(beatmapattributesbuilder** context);

ffierror beatmap_attributes_new(beatmapattributesbuilder** context);

void beatmap_attributes_mode(beatmapattributesbuilder* context, mode mode);

void beatmap_attributes_p_mods(beatmapattributesbuilder* context, const mods* mods);

void beatmap_attributes_i_mods(beatmapattributesbuilder* context, uint32_t mods);

ffierror beatmap_attributes_s_mods(beatmapattributesbuilder* context, const char* str);

void beatmap_attributes_clock_rate(beatmapattributesbuilder* context, double clock_rate);

void beatmap_attributes_ar(beatmapattributesbuilder* context, float ar);

void beatmap_attributes_cs(beatmapattributesbuilder* context, float cs);

void beatmap_attributes_hp(beatmapattributesbuilder* context, float hp);

void beatmap_attributes_od(beatmapattributesbuilder* context, float od);

double beatmap_attributes_get_clock_rate(beatmapattributesbuilder* context);

beatmapattributes beatmap_attributes_build(const beatmapattributesbuilder* context, const beatmap* beatmap);

/// Destroys the given instance.
///
/// # Safety
///
/// The passed parameter MUST have been created with the corresponding init function;
/// passing any other value results in undefined behavior.
ffierror beatmap_destroy(beatmap** context);

ffierror beatmap_from_bytes(beatmap** context, sliceu8 data);

ffierror beatmap_from_path(beatmap** context, const char* path);

/// Convert a Beatmap to the specified mode
uint8_t beatmap_convert(beatmap* context, mode mode, const mods* mods);

double beatmap_bpm(beatmap* context);

double beatmap_total_break_time(beatmap* context);

mode beatmap_mode(beatmap* context);

uint8_t beatmap_is_convert(beatmap* context);

/// Destroys the given instance.
///
/// # Safety
///
/// The passed parameter MUST have been created with the corresponding init function;
/// passing any other value results in undefined behavior.
ffierror difficulty_destroy(difficulty** context);

ffierror difficulty_new(difficulty** context);

void difficulty_p_mods(difficulty* context, const mods* mods);

void difficulty_i_mods(difficulty* context, uint32_t mods);

ffierror difficulty_s_mods(difficulty* context, const char* str);

void difficulty_passed_objects(difficulty* context, uint32_t passed_objects);

void difficulty_clock_rate(difficulty* context, double clock_rate);

void difficulty_ar(difficulty* context, float ar);

void difficulty_cs(difficulty* context, float cs);

void difficulty_hp(difficulty* context, float hp);

void difficulty_od(difficulty* context, float od);

void difficulty_hardrock_offsets(difficulty* context, uint8_t hardrock_offsets);

void difficulty_lazer(difficulty* context, uint8_t lazer);

difficultyattributes difficulty_calculate(const difficulty* context, const beatmap* beatmap);

double difficulty_get_clock_rate(difficulty* context);

/// Destroys the given instance.
///
/// # Safety
///
/// The passed parameter MUST have been created with the corresponding init function;
/// passing any other value results in undefined behavior.
ffierror performance_destroy(performance** context);

ffierror performance_new(performance** context);

void performance_mode(performance* context, mode mode);

void performance_p_mods(performance* context, const mods* mods);

void performance_i_mods(performance* context, uint32_t mods);

ffierror performance_s_mods(performance* context, const char* str);

void performance_passed_objects(performance* context, uint32_t passed_objects);

void performance_clock_rate(performance* context, double clock_rate);

void performance_ar(performance* context, float ar);

void performance_cs(performance* context, float cs);

void performance_hp(performance* context, float hp);

void performance_od(performance* context, float od);

void performance_hardrock_offsets(performance* context, uint8_t hardrock_offsets);

void performance_accuracy(performance* context, double accuracy);

void performance_misses(performance* context, uint32_t misses);

void performance_combo(performance* context, uint32_t combo);

void performance_hitresult_priority(performance* context, hitresultpriority hitresult_priority);

void performance_lazer(performance* context, uint8_t lazer);

void performance_slider_tick_hits(performance* context, uint32_t slider_tick_hits);

void performance_slider_end_hits(performance* context, uint32_t slider_end_hits);

void performance_n300(performance* context, uint32_t n300);

void performance_n100(performance* context, uint32_t n100);

void performance_n50(performance* context, uint32_t n50);

void performance_n_katu(performance* context, uint32_t n_katu);

void performance_n_geki(performance* context, uint32_t n_geki);

scorestate performance_generate_state(const performance* context, const beatmap* beatmap);

scorestate performance_generate_state_from_difficulty(const performance* context, difficultyattributes difficulty_attr);

performanceattributes performance_calculate(const performance* context, const beatmap* beatmap);

performanceattributes performance_calculate_from_difficulty(const performance* context, difficultyattributes difficulty_attr);

double performance_get_clock_rate(performance* context);

/// Destroys the given instance.
///
/// # Safety
///
/// The passed parameter MUST have been created with the corresponding init function;
/// passing any other value results in undefined behavior.
ffierror string_destroy(ownedstring** context);

ffierror string_from_c_str(ownedstring** context, const char* str);

ffierror string_empty(ownedstring** context);

uint8_t string_is_init(const ownedstring* context);

const char* string_to_cstr(const ownedstring* context);

/// Destroys the given instance.
///
/// # Safety
///
/// The passed parameter MUST have been created with the corresponding init function;
/// passing any other value results in undefined behavior.
ffierror mods_destroy(mods** context);

ffierror mods_new(mods** context, mode mode);

ffierror mods_from_acronyms(mods** context, const char* str, mode mode);

ffierror mods_from_bits(mods** context, uint32_t bits, mode mode);

ffierror mods_from_json(mods** context, const char* str, mode mode);

ffierror mods_from_json_sanitize(mods** context, const char* str, mode mode);

void mods_remove_incompatible_mods(mods* context);

uint32_t mods_bits(mods* context);

uint32_t mods_len(mods* context);

void mods_json(mods* context, ownedstring* str);

uint8_t mods_insert_json(mods* context, const char* str);

uint8_t mods_insert(mods* context, const char* str);

uint8_t mods_contains(mods* context, const char* str);

void mods_clear(mods* context);

optionf64 mods_clock_rate(mods* context);

void debug_difficylty_attributes(const difficultyattributes* res, ownedstring* str);

void debug_performance_attributes(const performanceattributes* res, ownedstring* str);

void debug_score_state(const scorestate* res, ownedstring* str);

double calculate_accuacy(const scorestate* state, const difficultyattributes* difficulty, osuscoreorigin origin);


#ifdef __cplusplus
}
#endif

#endif /* rosu_pp */
