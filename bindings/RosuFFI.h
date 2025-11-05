

#ifndef rosu_pp
#define rosu_pp

#ifdef __cplusplus
extern "C" {
#endif

#include <stdint.h>
#include <stdbool.h>
#include <sys/types.h>




typedef enum ERROR
    {
    ERROR_UNKNOWN = 0,
    ERROR_NULL = 1,
    ERROR_IO = 2,
    ERROR_INVALIDSTRING = 3,
    ERROR_UTF8 = 4,
    ERROR_SERIALIZE = 5,
    ERROR_CONVERT = 6,
    } ERROR;

typedef enum HITOBJECTKIND
    {
    HITOBJECTKIND_CIRCLE = 0,
    HITOBJECTKIND_SLIDER = 1,
    HITOBJECTKIND_SPINNER = 2,
    HITOBJECTKIND_HOLD = 3,
    } HITOBJECTKIND;

typedef enum HITRESULTPRIORITY
    {
    HITRESULTPRIORITY_BESTCASE = 0,
    HITRESULTPRIORITY_WORSTCASE = 1,
    } HITRESULTPRIORITY;

typedef enum MODE
    {
    ///  osu!standard
    MODE_OSU = 0,
    ///  osu!taiko
    MODE_TAIKO = 1,
    ///  osu!catch
    MODE_CATCH = 2,
    ///  osu!mania
    MODE_MANIA = 3,
    } MODE;

///  Type to pass [`OsuScoreState::accuracy`] and specify the origin of a score.
typedef enum OSUSCOREORIGIN
    {
    ///  For scores set on osu!stable
    OSUSCOREORIGIN_STABLE = 0,
    ///  For scores set on osu!lazer with slider accuracy
    OSUSCOREORIGIN_WITHSLIDERACC = 1,
    ///  For scores set on osu!lazer without slider accuracy
    OSUSCOREORIGIN_WITHOUTSLIDERACC = 2,
    } OSUSCOREORIGIN;

typedef struct BEATMAP BEATMAP;

typedef struct BEATMAPATTRIBUTESBUILDER BEATMAPATTRIBUTESBUILDER;

typedef struct DIFFICULTY DIFFICULTY;

typedef struct GRADUALDIFFICULTY GRADUALDIFFICULTY;

typedef struct GRADUALPERFORMANCE GRADUALPERFORMANCE;

typedef struct MODS MODS;

typedef struct PERFORMANCE PERFORMANCE;

///  UTF-8 string marshalling helper.
///  A highly dangerous 'use once type' that has ownership semantics!
///  Once passed over an FFI boundary 'the other side' is meant to own
///  (and free) it. Rust handles that fine, but if in C# you put this
///  in a struct and then call Rust multiple times with that struct 
///  you'll free the same pointer multiple times, and get UB!
typedef struct UTF8STRING
    {
    uint8_t* ptr;
    uint64_t len;
    uint64_t capacity;
    } UTF8STRING;

///  The result of a difficulty calculation on an osu!catch map.
typedef struct CATCHDIFFICULTYATTRIBUTES
    {
    ///  The final star rating
    double stars;
    ///  The approach rate.
    double ar;
    ///  The amount of fruits.
    uint32_t n_fruits;
    ///  The amount of droplets.
    uint32_t n_droplets;
    ///  The amount of tiny droplets.
    uint32_t n_tiny_droplets;
    ///  Whether the [`Beatmap`] was a convert i.e. an osu!standard map.
    /// 
    ///  [`Beatmap`]: crate::model::beatmap::Beatmap
    bool is_convert;
    } CATCHDIFFICULTYATTRIBUTES;

///  The result of a difficulty calculation on an osu!mania map.
typedef struct MANIADIFFICULTYATTRIBUTES
    {
    ///  The final star rating.
    double stars;
    ///  The amount of hitobjects in the map.
    uint32_t n_objects;
    ///  The amount of hold notes in the map.
    uint32_t n_hold_notes;
    ///  The maximum achievable combo.
    uint32_t max_combo;
    ///  Whether the [`Beatmap`] was a convert i.e. an osu!standard map.
    /// 
    ///  [`Beatmap`]: crate::model::beatmap::Beatmap
    bool is_convert;
    } MANIADIFFICULTYATTRIBUTES;

///  The result of a difficulty calculation on an osu!standard map.
typedef struct OSUDIFFICULTYATTRIBUTES
    {
    ///  The difficulty of the aim skill.
    double aim;
    ///  The number of sliders weighted by difficulty.
    double aim_difficult_slider_count;
    ///  The difficulty of the speed skill.
    double speed;
    ///  The difficulty of the flashlight skill.
    double flashlight;
    ///  The ratio of the aim strain with and without considering sliders
    double slider_factor;
    ///  The number of clickable objects weighted by difficulty.
    double speed_note_count;
    ///  Weighted sum of aim strains.
    double aim_difficult_strain_count;
    ///  Weighted sum of speed strains.
    double speed_difficult_strain_count;
    ///  The approach rate.
    double ar;
    ///  The great hit window.
    double great_hit_window;
    ///  The ok hit window.
    double ok_hit_window;
    ///  The meh hit window.
    double meh_hit_window;
    ///  The overall difficulty
    double hp;
    ///  The amount of circles.
    uint32_t n_circles;
    ///  The amount of sliders.
    uint32_t n_sliders;
    ///  The amount of "large ticks".
    /// 
    ///  The meaning depends on the kind of score:
    ///  - if set on osu!stable, this value is irrelevant
    ///  - if set on osu!lazer *without* `CL`, this value is the amount of
    ///    slider ticks and repeats
    ///  - if set on osu!lazer *with* `CL`, this value is the amount of slider
    ///    heads, ticks, and repeats
    uint32_t n_large_ticks;
    ///  The amount of spinners.
    uint32_t n_spinners;
    ///  The final star rating
    double stars;
    ///  The maximum combo.
    uint32_t max_combo;
    } OSUDIFFICULTYATTRIBUTES;

typedef struct POS
    {
    ///  Position on the x-axis.
    float x;
    ///  Position on the y-axis.
    float y;
    } POS;

///  Aggregation for a score's current state.
typedef struct SCORESTATE
    {
    ///  Maximum combo that the score has had so far. **Not** the maximum
    ///  possible combo of the map so far.
    /// 
    ///  Note that for osu!catch only fruits and droplets are considered for
    ///  combo.
    /// 
    ///  Irrelevant for osu!mania.
    uint32_t max_combo;
    ///  "Large tick" hits for osu!standard.
    /// 
    ///  The meaning depends on the kind of score:
    ///  - if set on osu!stable, this field is irrelevant and can be `0`
    ///  - if set on osu!lazer *without* `CL`, this field is the amount of hit
    ///    slider ticks and repeats
    ///  - if set on osu!lazer *with* `CL`, this field is the amount of hit
    ///    slider heads, ticks, and repeats
    /// 
    ///  Only relevant for osu!lazer.
    uint32_t osu_large_tick_hits;
    ///  "Small ticks" hits for osu!standard.
    /// 
    ///  These are essentially the slider end hits for lazer scores without
    ///  slider accuracy.
    /// 
    ///  Only relevant for osu!lazer.
    uint32_t osu_small_tick_hits;
    ///  Amount of successfully hit slider ends.
    /// 
    ///  Only relevant for osu!standard in lazer.
    uint32_t slider_end_hits;
    ///  Amount of current gekis (n320 for osu!mania).
    uint32_t n_geki;
    ///  Amount of current katus (tiny droplet misses for osu!catch / n200 for
    ///  osu!mania).
    uint32_t n_katu;
    ///  Amount of current 300s (fruits for osu!catch).
    uint32_t n300;
    ///  Amount of current 100s (droplets for osu!catch).
    uint32_t n100;
    ///  Amount of current 50s (tiny droplets for osu!catch).
    uint32_t n50;
    ///  Amount of current misses (fruits + droplets for osu!catch).
    uint32_t misses;
    } SCORESTATE;

///  The result of a difficulty calculation on an osu!taiko map.
typedef struct TAIKODIFFICULTYATTRIBUTES
    {
    ///  The difficulty of the stamina skill.
    double stamina;
    ///  The difficulty of the rhythm skill.
    double rhythm;
    ///  The difficulty of the color skill.
    double color;
    ///  The difficulty of the reading skill.
    double reading;
    ///  The perceived hit window for an n300 inclusive of rate-adjusting mods (DT/HT/etc)
    double great_hit_window;
    ///  The perceived hit window for an n100 inclusive of rate-adjusting mods (DT/HT/etc)
    double ok_hit_window;
    ///  The ratio of stamina difficulty from mono-color (single color) streams to total
    ///  stamina difficulty.
    double mono_stamina_factor;
    ///  The final star rating.
    double stars;
    ///  The maximum combo.
    uint32_t max_combo;
    ///  Whether the [`Beatmap`] was a convert i.e. an osu!standard map.
    /// 
    ///  [`Beatmap`]: crate::model::beatmap::Beatmap
    bool is_convert;
    } TAIKODIFFICULTYATTRIBUTES;

/// A pointer to an array of data someone else owns which may not be modified.
typedef struct SLICEU8
    {
    /// Pointer to start of immutable data.
    const uint8_t* data;
    /// Number of elements.
    uint64_t len;
    } SLICEU8;

/// Option that contains Some(value) or None.
typedef enum OPTIONF64
    {
    /// Element if Some().
    // TODO - OMITTED DATA VARIANT - BINDINGS ARE BROKEN
    OPTIONF64_NONE = 1,
    } OPTIONF64;

/// Result that contains value or an error.
typedef enum RESULTERROR
    {
    /// Element if err is `Ok`.
    // TODO - OMITTED DATA VARIANT - BINDINGS ARE BROKEN
    /// Error value.
    // TODO - OMITTED DATA VARIANT - BINDINGS ARE BROKEN
    RESULTERROR_PANIC = 2,
    RESULTERROR_NULL = 3,
    } RESULTERROR;

typedef enum DIFFICULTYATTRIBUTES
    {
    // TODO - OMITTED DATA VARIANT - BINDINGS ARE BROKEN
    // TODO - OMITTED DATA VARIANT - BINDINGS ARE BROKEN
    // TODO - OMITTED DATA VARIANT - BINDINGS ARE BROKEN
    // TODO - OMITTED DATA VARIANT - BINDINGS ARE BROKEN
    } DIFFICULTYATTRIBUTES;

///  The result of a performance calculation on an osu!catch map.
typedef struct CATCHPERFORMANCEATTRIBUTES
    {
    ///  The difficulty attributes that were used for the performance calculation
    CATCHDIFFICULTYATTRIBUTES difficulty;
    ///  The final performance points.
    double pp;
    } CATCHPERFORMANCEATTRIBUTES;

typedef struct HITOBJECTDATA
    {
    HITOBJECTKIND kind;
    uint32_t repeats;
    OPTIONF64 expected_dist;
    double duration;
    } HITOBJECTDATA;

///  AR and OD hit windows
typedef struct HITWINDOWS
    {
    ///  Hit window for approach rate i.e. `TimePreempt` in milliseconds.
    double ar;
    ///  Hit window for overall difficulty i.e. time to hit a 300 ("Great") in milliseconds.
    double od_great;
    ///  Hit window for overall difficulty i.e. time to hit a 100 ("Ok") in milliseconds.
    /// 
    ///  `None` for osu!mania.
    OPTIONF64 od_ok;
    } HITWINDOWS;

///  The result of a performance calculation on an osu!mania map.
typedef struct MANIAPERFORMANCEATTRIBUTES
    {
    ///  The difficulty attributes that were used for the performance calculation.
    MANIADIFFICULTYATTRIBUTES difficulty;
    ///  The final performance points.
    double pp;
    ///  The difficulty portion of the final pp.
    double pp_difficulty;
    } MANIAPERFORMANCEATTRIBUTES;

///  The result of a performance calculation on an osu!standard map.
typedef struct OSUPERFORMANCEATTRIBUTES
    {
    ///  The difficulty attributes that were used for the performance calculation
    OSUDIFFICULTYATTRIBUTES difficulty;
    ///  The final performance points.
    double pp;
    ///  The accuracy portion of the final pp.
    double pp_acc;
    ///  The aim portion of the final pp.
    double pp_aim;
    ///  The flashlight portion of the final pp.
    double pp_flashlight;
    ///  The speed portion of the final pp.
    double pp_speed;
    ///  Misses including an approximated amount of slider breaks
    double effective_miss_count;
    ///  Approximated unstable-rate
    OPTIONF64 speed_deviation;
    } OSUPERFORMANCEATTRIBUTES;

///  The result of a performance calculation on an osu!taiko map.
typedef struct TAIKOPERFORMANCEATTRIBUTES
    {
    ///  The difficulty attributes that were used for the performance calculation
    TAIKODIFFICULTYATTRIBUTES difficulty;
    ///  The final performance points.
    double pp;
    ///  The accuracy portion of the final pp.
    double pp_acc;
    ///  The strain portion of the final pp.
    double pp_difficulty;
    ///  Scaled miss count based on total hits.
    double effective_miss_count;
    ///  Upper bound on the player's tap deviation.
    OPTIONF64 estimated_unstable_rate;
    } TAIKOPERFORMANCEATTRIBUTES;

/// Result that contains value or an error.
typedef enum RESULTCONSTPTRBEATMAPATTRIBUTESBUILDERERROR
    {
    /// Element if err is `Ok`.
    // TODO - OMITTED DATA VARIANT - BINDINGS ARE BROKEN
    /// Error value.
    // TODO - OMITTED DATA VARIANT - BINDINGS ARE BROKEN
    RESULTCONSTPTRBEATMAPATTRIBUTESBUILDERERROR_PANIC = 2,
    RESULTCONSTPTRBEATMAPATTRIBUTESBUILDERERROR_NULL = 3,
    } RESULTCONSTPTRBEATMAPATTRIBUTESBUILDERERROR;

/// Result that contains value or an error.
typedef enum RESULTCONSTPTRBEATMAPERROR
    {
    /// Element if err is `Ok`.
    // TODO - OMITTED DATA VARIANT - BINDINGS ARE BROKEN
    /// Error value.
    // TODO - OMITTED DATA VARIANT - BINDINGS ARE BROKEN
    RESULTCONSTPTRBEATMAPERROR_PANIC = 2,
    RESULTCONSTPTRBEATMAPERROR_NULL = 3,
    } RESULTCONSTPTRBEATMAPERROR;

/// Result that contains value or an error.
typedef enum RESULTCONSTPTRDIFFICULTYERROR
    {
    /// Element if err is `Ok`.
    // TODO - OMITTED DATA VARIANT - BINDINGS ARE BROKEN
    /// Error value.
    // TODO - OMITTED DATA VARIANT - BINDINGS ARE BROKEN
    RESULTCONSTPTRDIFFICULTYERROR_PANIC = 2,
    RESULTCONSTPTRDIFFICULTYERROR_NULL = 3,
    } RESULTCONSTPTRDIFFICULTYERROR;

/// Result that contains value or an error.
typedef enum RESULTCONSTPTRGRADUALDIFFICULTYERROR
    {
    /// Element if err is `Ok`.
    // TODO - OMITTED DATA VARIANT - BINDINGS ARE BROKEN
    /// Error value.
    // TODO - OMITTED DATA VARIANT - BINDINGS ARE BROKEN
    RESULTCONSTPTRGRADUALDIFFICULTYERROR_PANIC = 2,
    RESULTCONSTPTRGRADUALDIFFICULTYERROR_NULL = 3,
    } RESULTCONSTPTRGRADUALDIFFICULTYERROR;

/// Result that contains value or an error.
typedef enum RESULTCONSTPTRGRADUALPERFORMANCEERROR
    {
    /// Element if err is `Ok`.
    // TODO - OMITTED DATA VARIANT - BINDINGS ARE BROKEN
    /// Error value.
    // TODO - OMITTED DATA VARIANT - BINDINGS ARE BROKEN
    RESULTCONSTPTRGRADUALPERFORMANCEERROR_PANIC = 2,
    RESULTCONSTPTRGRADUALPERFORMANCEERROR_NULL = 3,
    } RESULTCONSTPTRGRADUALPERFORMANCEERROR;

/// Result that contains value or an error.
typedef enum RESULTCONSTPTRMODSERROR
    {
    /// Element if err is `Ok`.
    // TODO - OMITTED DATA VARIANT - BINDINGS ARE BROKEN
    /// Error value.
    // TODO - OMITTED DATA VARIANT - BINDINGS ARE BROKEN
    RESULTCONSTPTRMODSERROR_PANIC = 2,
    RESULTCONSTPTRMODSERROR_NULL = 3,
    } RESULTCONSTPTRMODSERROR;

/// Result that contains value or an error.
typedef enum RESULTCONSTPTRPERFORMANCEERROR
    {
    /// Element if err is `Ok`.
    // TODO - OMITTED DATA VARIANT - BINDINGS ARE BROKEN
    /// Error value.
    // TODO - OMITTED DATA VARIANT - BINDINGS ARE BROKEN
    RESULTCONSTPTRPERFORMANCEERROR_PANIC = 2,
    RESULTCONSTPTRPERFORMANCEERROR_NULL = 3,
    } RESULTCONSTPTRPERFORMANCEERROR;

typedef enum PERFORMANCEATTRIBUTES
    {
    // TODO - OMITTED DATA VARIANT - BINDINGS ARE BROKEN
    // TODO - OMITTED DATA VARIANT - BINDINGS ARE BROKEN
    // TODO - OMITTED DATA VARIANT - BINDINGS ARE BROKEN
    // TODO - OMITTED DATA VARIANT - BINDINGS ARE BROKEN
    } PERFORMANCEATTRIBUTES;

///  Summary struct for a [`Beatmap`]'s attributes.
typedef struct BEATMAPATTRIBUTES
    {
    ///  The approach rate.
    double ar;
    ///  The overall difficulty.
    double od;
    ///  The circle size.
    double cs;
    ///  The health drain rate
    double hp;
    ///  The clock rate with respect to mods.
    double clock_rate;
    ///  The hit windows for approach rate and overall difficulty.
    HITWINDOWS hit_windows;
    } BEATMAPATTRIBUTES;

typedef struct HITOBJECT
    {
    POS pos;
    double start_time;
    HITOBJECTDATA data;
    } HITOBJECT;

/// Option that contains Some(value) or None.
typedef enum OPTIONDIFFICULTYATTRIBUTES
    {
    /// Element if Some().
    // TODO - OMITTED DATA VARIANT - BINDINGS ARE BROKEN
    OPTIONDIFFICULTYATTRIBUTES_NONE = 1,
    } OPTIONDIFFICULTYATTRIBUTES;

/// Option that contains Some(value) or None.
typedef enum OPTIONPERFORMANCEATTRIBUTES
    {
    /// Element if Some().
    // TODO - OMITTED DATA VARIANT - BINDINGS ARE BROKEN
    OPTIONPERFORMANCEATTRIBUTES_NONE = 1,
    } OPTIONPERFORMANCEATTRIBUTES;

///  Vec marshalling helper.
///  A highly dangerous 'use once type' that has ownership semantics!
///  Once passed over an FFI boundary 'the other side' is meant to own
///  (and free) it. Rust handles that fine, but if in C# you put this
///  in a struct and then call Rust multiple times with that struct 
///  you'll free the same pointer multiple times, and get UB!
typedef struct VECHITOBJECT
    {
    HITOBJECT* ptr;
    uint64_t len;
    uint64_t capacity;
    } VECHITOBJECT;


///  Destroys the given instance.
/// 
///  # Safety
/// 
///  The passed parameter MUST have been created with the corresponding init function;
///  passing any other value results in undefined behavior.
RESULTCONSTPTRBEATMAPATTRIBUTESBUILDERERROR beatmap_attributes_destroy(const BEATMAPATTRIBUTESBUILDER* _CONTEXT);

RESULTCONSTPTRBEATMAPATTRIBUTESBUILDERERROR beatmap_attributes_new();

void beatmap_attributes_mode(BEATMAPATTRIBUTESBUILDER* _CONTEXT, MODE MODE);

void beatmap_attributes_p_mods(BEATMAPATTRIBUTESBUILDER* _CONTEXT, const MODS* MODS);

void beatmap_attributes_i_mods(BEATMAPATTRIBUTESBUILDER* _CONTEXT, uint32_t MODS);

RESULTERROR beatmap_attributes_s_mods(BEATMAPATTRIBUTESBUILDER* _CONTEXT, const char* STR);

void beatmap_attributes_clock_rate(BEATMAPATTRIBUTESBUILDER* _CONTEXT, double CLOCK_RATE);

void beatmap_attributes_ar(BEATMAPATTRIBUTESBUILDER* _CONTEXT, float AR);

void beatmap_attributes_cs(BEATMAPATTRIBUTESBUILDER* _CONTEXT, float CS);

void beatmap_attributes_hp(BEATMAPATTRIBUTESBUILDER* _CONTEXT, float HP);

void beatmap_attributes_od(BEATMAPATTRIBUTESBUILDER* _CONTEXT, float OD);

double beatmap_attributes_get_clock_rate(BEATMAPATTRIBUTESBUILDER* _CONTEXT);

BEATMAPATTRIBUTES beatmap_attributes_build(const BEATMAPATTRIBUTESBUILDER* _CONTEXT, const BEATMAP* BEATMAP);

///  Destroys the given instance.
/// 
///  # Safety
/// 
///  The passed parameter MUST have been created with the corresponding init function;
///  passing any other value results in undefined behavior.
RESULTCONSTPTRBEATMAPERROR beatmap_destroy(const BEATMAP* _CONTEXT);

RESULTCONSTPTRBEATMAPERROR beatmap_from_bytes(SLICEU8 DATA);

RESULTCONSTPTRBEATMAPERROR beatmap_from_path(const char* PATH);

///  Convert a Beatmap to the specified mode
bool beatmap_convert(BEATMAP* _CONTEXT, MODE MODE, const MODS* MODS);

double beatmap_bpm(BEATMAP* _CONTEXT);

double beatmap_total_break_time(BEATMAP* _CONTEXT);

int32_t beatmap_version(BEATMAP* _CONTEXT);

bool beatmap_is_convert(BEATMAP* _CONTEXT);

float beatmap_stack_leniency(BEATMAP* _CONTEXT);

MODE beatmap_mode(BEATMAP* _CONTEXT);

float beatmap_ar(BEATMAP* _CONTEXT);

float beatmap_cs(BEATMAP* _CONTEXT);

float beatmap_hp(BEATMAP* _CONTEXT);

float beatmap_od(BEATMAP* _CONTEXT);

double beatmap_slider_multiplier(BEATMAP* _CONTEXT);

double beatmap_slider_tick_rate(BEATMAP* _CONTEXT);

VECHITOBJECT beatmap_hit_objects(const BEATMAP* _CONTEXT);

///  Destroys the given instance.
/// 
///  # Safety
/// 
///  The passed parameter MUST have been created with the corresponding init function;
///  passing any other value results in undefined behavior.
RESULTCONSTPTRDIFFICULTYERROR difficulty_destroy(const DIFFICULTY* _CONTEXT);

RESULTCONSTPTRDIFFICULTYERROR difficulty_new();

void difficulty_p_mods(DIFFICULTY* _CONTEXT, const MODS* MODS);

void difficulty_i_mods(DIFFICULTY* _CONTEXT, uint32_t MODS);

RESULTERROR difficulty_s_mods(DIFFICULTY* _CONTEXT, const char* STR);

void difficulty_passed_objects(DIFFICULTY* _CONTEXT, uint32_t PASSED_OBJECTS);

void difficulty_clock_rate(DIFFICULTY* _CONTEXT, double CLOCK_RATE);

void difficulty_ar(DIFFICULTY* _CONTEXT, float AR);

void difficulty_cs(DIFFICULTY* _CONTEXT, float CS);

void difficulty_hp(DIFFICULTY* _CONTEXT, float HP);

void difficulty_od(DIFFICULTY* _CONTEXT, float OD);

void difficulty_hardrock_offsets(DIFFICULTY* _CONTEXT, bool HARDROCK_OFFSETS);

void difficulty_lazer(DIFFICULTY* _CONTEXT, bool LAZER);

DIFFICULTYATTRIBUTES difficulty_calculate(const DIFFICULTY* _CONTEXT, const BEATMAP* BEATMAP);

double difficulty_get_clock_rate(DIFFICULTY* _CONTEXT);

///  Destroys the given instance.
/// 
///  # Safety
/// 
///  The passed parameter MUST have been created with the corresponding init function;
///  passing any other value results in undefined behavior.
RESULTCONSTPTRPERFORMANCEERROR performance_destroy(const PERFORMANCE* _CONTEXT);

RESULTCONSTPTRPERFORMANCEERROR performance_new();

void performance_mode(PERFORMANCE* _CONTEXT, MODE MODE);

void performance_p_mods(PERFORMANCE* _CONTEXT, const MODS* MODS);

void performance_i_mods(PERFORMANCE* _CONTEXT, uint32_t MODS);

RESULTERROR performance_s_mods(PERFORMANCE* _CONTEXT, const char* STR);

void performance_passed_objects(PERFORMANCE* _CONTEXT, uint32_t PASSED_OBJECTS);

void performance_clock_rate(PERFORMANCE* _CONTEXT, double CLOCK_RATE);

void performance_ar(PERFORMANCE* _CONTEXT, float AR);

void performance_cs(PERFORMANCE* _CONTEXT, float CS);

void performance_hp(PERFORMANCE* _CONTEXT, float HP);

void performance_od(PERFORMANCE* _CONTEXT, float OD);

void performance_hardrock_offsets(PERFORMANCE* _CONTEXT, bool HARDROCK_OFFSETS);

void performance_state(PERFORMANCE* _CONTEXT, SCORESTATE STATE);

void performance_accuracy(PERFORMANCE* _CONTEXT, double ACCURACY);

void performance_misses(PERFORMANCE* _CONTEXT, uint32_t MISSES);

void performance_combo(PERFORMANCE* _CONTEXT, uint32_t COMBO);

void performance_hitresult_priority(PERFORMANCE* _CONTEXT, HITRESULTPRIORITY HITRESULT_PRIORITY);

void performance_lazer(PERFORMANCE* _CONTEXT, bool LAZER);

void performance_large_tick_hits(PERFORMANCE* _CONTEXT, uint32_t LARGE_TICK_HITS);

void performance_small_tick_hits(PERFORMANCE* _CONTEXT, uint32_t SMALL_TICK_HITS);

void performance_slider_end_hits(PERFORMANCE* _CONTEXT, uint32_t SLIDER_END_HITS);

void performance_n300(PERFORMANCE* _CONTEXT, uint32_t N300);

void performance_n100(PERFORMANCE* _CONTEXT, uint32_t N100);

void performance_n50(PERFORMANCE* _CONTEXT, uint32_t N50);

void performance_n_katu(PERFORMANCE* _CONTEXT, uint32_t N_KATU);

void performance_n_geki(PERFORMANCE* _CONTEXT, uint32_t N_GEKI);

SCORESTATE performance_generate_state(const PERFORMANCE* _CONTEXT, const BEATMAP* BEATMAP);

SCORESTATE performance_generate_state_from_difficulty(const PERFORMANCE* _CONTEXT, DIFFICULTYATTRIBUTES DIFFICULTY_ATTR);

PERFORMANCEATTRIBUTES performance_calculate(const PERFORMANCE* _CONTEXT, const BEATMAP* BEATMAP);

PERFORMANCEATTRIBUTES performance_calculate_from_difficulty(const PERFORMANCE* _CONTEXT, DIFFICULTYATTRIBUTES DIFFICULTY_ATTR);

double performance_get_clock_rate(PERFORMANCE* _CONTEXT);

///  Destroys the given instance.
/// 
///  # Safety
/// 
///  The passed parameter MUST have been created with the corresponding init function;
///  passing any other value results in undefined behavior.
RESULTCONSTPTRGRADUALDIFFICULTYERROR gradual_difficulty_destroy(const GRADUALDIFFICULTY* _CONTEXT);

///  Create a [`GradualDifficulty`] for a map of any mode.
RESULTCONSTPTRGRADUALDIFFICULTYERROR gradual_difficulty_new(const DIFFICULTY* DIFFICULTY, const BEATMAP* BEATMAP);

///  Create a [`GradualDifficulty`] for a [`Beatmap`] on a specific [`GameMode`].
RESULTCONSTPTRGRADUALDIFFICULTYERROR gradual_difficulty_new_with_mode(const DIFFICULTY* DIFFICULTY, const BEATMAP* BEATMAP, MODE MODE);

OPTIONDIFFICULTYATTRIBUTES gradual_difficulty_next(GRADUALDIFFICULTY* _CONTEXT);

OPTIONDIFFICULTYATTRIBUTES gradual_difficulty_nth(GRADUALDIFFICULTY* _CONTEXT, uint32_t N);

uint32_t gradual_difficulty_len(const GRADUALDIFFICULTY* _CONTEXT);

///  Destroys the given instance.
/// 
///  # Safety
/// 
///  The passed parameter MUST have been created with the corresponding init function;
///  passing any other value results in undefined behavior.
RESULTCONSTPTRGRADUALPERFORMANCEERROR gradual_performance_destroy(const GRADUALPERFORMANCE* _CONTEXT);

///  Create a [`GradualPerformance`] for a map of any mode.
RESULTCONSTPTRGRADUALPERFORMANCEERROR gradual_performance_new(const DIFFICULTY* DIFFICULTY, const BEATMAP* BEATMAP);

///  Create a [`GradualPerformance`] for a [`Beatmap`] on a specific [`GameMode`].
RESULTCONSTPTRGRADUALPERFORMANCEERROR gradual_performance_new_with_mode(const DIFFICULTY* DIFFICULTY, const BEATMAP* BEATMAP, MODE MODE);

///  Process the next hit object and calculate the performance attributes
///  for the resulting score state.
OPTIONPERFORMANCEATTRIBUTES gradual_performance_next(GRADUALPERFORMANCE* _CONTEXT, SCORESTATE STATE);

///  Process all remaining hit objects and calculate the final performance
///  attributes.
OPTIONPERFORMANCEATTRIBUTES gradual_performance_last(GRADUALPERFORMANCE* _CONTEXT, SCORESTATE STATE);

///  Process everything up to the next `n`th hitobject and calculate the
///  performance attributes for the resulting score state.
/// 
///  Note that the count is zero indexed
///  `n=1` will process 2, and so on.
OPTIONPERFORMANCEATTRIBUTES gradual_performance_nth(GRADUALPERFORMANCE* _CONTEXT, SCORESTATE STATE, uint32_t N);

///  Returns the amount of remaining objects.
uint32_t gradual_performance_len(const GRADUALPERFORMANCE* _CONTEXT);

///  Destroys the given instance.
/// 
///  # Safety
/// 
///  The passed parameter MUST have been created with the corresponding init function;
///  passing any other value results in undefined behavior.
RESULTCONSTPTRMODSERROR mods_destroy(const MODS* _CONTEXT);

RESULTCONSTPTRMODSERROR mods_new(MODE MODE);

RESULTCONSTPTRMODSERROR mods_from_acronyms(const char* STR, MODE MODE);

RESULTCONSTPTRMODSERROR mods_from_bits(uint32_t BITS, MODE MODE);

RESULTCONSTPTRMODSERROR mods_from_json(const char* STR, MODE MODE, bool DENY_UNKNOWN_FIELDS);

void mods_remove_unknown_mods(MODS* _CONTEXT);

void mods_sanitize(MODS* _CONTEXT);

uint32_t mods_bits(MODS* _CONTEXT);

uint32_t mods_len(MODS* _CONTEXT);

UTF8STRING mods_json(MODS* _CONTEXT);

bool mods_insert_json(MODS* _CONTEXT, const char* STR, bool DENY_UNKNOWN_FIELDS);

bool mods_insert(MODS* _CONTEXT, const char* STR);

bool mods_contains(MODS* _CONTEXT, const char* STR);

void mods_clear(MODS* _CONTEXT);

OPTIONF64 mods_clock_rate(MODS* _CONTEXT);

UTF8STRING debug_difficulty_attributes(const DIFFICULTYATTRIBUTES* RES);

UTF8STRING debug_performance_attributes(const PERFORMANCEATTRIBUTES* RES);

UTF8STRING debug_score_state(const SCORESTATE* RES);

double calculate_accuracy(const SCORESTATE* STATE, const DIFFICULTYATTRIBUTES* DIFFICULTY, OSUSCOREORIGIN ORIGIN);

int64_t interoptopus_string_create(const void* UTF8, uint64_t LEN, UTF8STRING* RVAL);

int64_t interoptopus_string_destroy(UTF8STRING UTF8);

int64_t interoptopus_string_clone(const UTF8STRING* UTF8, UTF8STRING* RVAL);

void interoptopus_wire_destroy(uint8_t* DATA, int32_t LEN, int32_t CAPACITY);

int64_t interoptopus_vec_create_1095792466183922639(const void* DATA, uint64_t LEN, VECHITOBJECT* RVAL);

int64_t interoptopus_vec_destroy_7642792079161229908(VECHITOBJECT IGNORED);


#ifdef __cplusplus
}
#endif

#endif /* rosu_pp */
