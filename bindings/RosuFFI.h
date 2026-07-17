/* Automatically generated from rosu_pp_ffi::ffi_inventory(). */
#ifndef ROSU_PP_FFI_H
#define ROSU_PP_FFI_H
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#ifdef __cplusplus
extern "C" {
#endif

typedef struct ResultPtrFFIError ResultPtrFFIError;
typedef struct String String;
typedef struct Option_bool Option_bool;
typedef struct OsuPerformanceAttributes OsuPerformanceAttributes;
typedef struct Pos Pos;
typedef struct Option_TooSuspicious Option_TooSuspicious;
typedef struct LegacyBeatmap LegacyBeatmap;
typedef struct ManiaPerformanceAttributes ManiaPerformanceAttributes;
typedef struct ExpectedDistance ExpectedDistance;
typedef struct HitObject HitObject;
typedef struct GradualDifficulty GradualDifficulty;
typedef struct ScoreState ScoreState;
typedef struct PerformanceAttributes PerformanceAttributes;
typedef struct ManiaDifficultyAttributes ManiaDifficultyAttributes;
typedef struct Difficulty Difficulty;
typedef struct LegacyPerformance LegacyPerformance;
typedef struct DurationData DurationData;
typedef struct Slice_u8 Slice_u8;
typedef struct Option_PerformanceAttributes Option_PerformanceAttributes;
typedef struct LegacyDifficultyAttributes LegacyDifficultyAttributes;
typedef struct Option_DifficultyAttributes Option_DifficultyAttributes;
typedef struct Performance Performance;
typedef struct CatchDifficultyAttributes CatchDifficultyAttributes;
typedef struct CatchPerformanceAttributes CatchPerformanceAttributes;
typedef struct Option_LegacyDifficultyAttributes Option_LegacyDifficultyAttributes;
typedef struct BeatmapAttributesBuilder BeatmapAttributesBuilder;
typedef struct Option_f64 Option_f64;
typedef struct LegacyDifficulty LegacyDifficulty;
typedef struct HitWindows HitWindows;
typedef struct LegacyPerformanceAttributes LegacyPerformanceAttributes;
typedef struct SliderData SliderData;
typedef struct DifficultyAttributes DifficultyAttributes;
typedef struct BeatmapAttributes BeatmapAttributes;
typedef struct Mods Mods;
typedef struct TaikoDifficultyAttributes TaikoDifficultyAttributes;
typedef struct Wire_Vec_HitObject Wire_Vec_HitObject;
typedef struct GradualPerformance GradualPerformance;
typedef struct TaikoPerformanceAttributes TaikoPerformanceAttributes;
typedef struct HitObjectData HitObjectData;
typedef struct Beatmap Beatmap;
typedef struct Slice_Mode Slice_Mode;
typedef struct OsuDifficultyAttributes OsuDifficultyAttributes;
typedef struct Option_u32 Option_u32;

typedef enum LegacyVersion {
    LEGACYVERSION_V2022 = 0,
    LEGACYVERSION_V2014_5 = 1,
    LEGACYVERSION_V2014_7 = 2,
    LEGACYVERSION_V2015_2 = 3,
    LEGACYVERSION_V2015_4 = 4,
    LEGACYVERSION_V2018 = 5,
    LEGACYVERSION_V2019 = 6,
    LEGACYVERSION_V2021_1 = 7,
    LEGACYVERSION_V2021_7 = 8,
    LEGACYVERSION_V2021_11 = 9,
    LEGACYVERSION_V2024 = 11,
    LEGACYVERSION_V2025_3 = 12,
    LEGACYVERSION_VPPV1 = 13,
    LEGACYVERSION_V2020 = 14,
    LEGACYVERSION_V2025_10 = 24,
} LegacyVersion;

struct ResultPtrFFIError { uint32_t variant; union { void *ok; uint32_t err; } payload; };

struct String { uint8_t *ptr; uintptr_t len; uintptr_t capacity; };

struct Option_bool { uint32_t variant; bool some; };

struct Pos {
    float x;
    float y;
};

typedef enum TooSuspicious {
    TOOSUSPICIOUS_DENSITY = 0,
    TOOSUSPICIOUS_LENGTH = 1,
    TOOSUSPICIOUS_OBJECTCOUNT = 2,
    TOOSUSPICIOUS_REDFLAG = 3,
    TOOSUSPICIOUS_SLIDERPOSITIONS = 4,
    TOOSUSPICIOUS_SLIDERREPEATS = 5,
} TooSuspicious;

struct ExpectedDistance {
    uint32_t variant;
    union {
        double some;
    } payload;
};

struct ManiaDifficultyAttributes {
    double stars;
    uint32_t n_objects;
    uint32_t n_hold_notes;
    uint32_t max_combo;
    bool is_convert;
};

struct DurationData {
    double duration;
};

struct Slice_u8 { const uint8_t *data; uintptr_t len; };

typedef enum FFIError {
    FFIERROR_OK = 0,
    FFIERROR_NULL = 100,
    FFIERROR_PANIC = 200,
    FFIERROR_IOERROR = 300,
    FFIERROR_SERIALIZEERROR = 600,
    FFIERROR_CONVERTERROR = 700,
    FFIERROR_UNKNOWN = 1000,
} FFIError;

typedef enum HitResultPriority {
    HITRESULTPRIORITY_BESTCASE = 0,
    HITRESULTPRIORITY_WORSTCASE = 1,
} HitResultPriority;

struct CatchDifficultyAttributes {
    double stars;
    double preempt;
    uint32_t n_fruits;
    uint32_t n_droplets;
    uint32_t n_tiny_droplets;
    bool is_convert;
};

struct CatchPerformanceAttributes {
    CatchDifficultyAttributes difficulty;
    double pp;
};

struct Option_f64 { uint32_t variant; double some; };

struct HitWindows {
    Option_f64 ar;
    Option_f64 od_perfect;
    Option_f64 od_great;
    Option_f64 od_good;
    Option_f64 od_ok;
    Option_f64 od_meh;
};

typedef enum OsuScoreOrigin {
    OSUSCOREORIGIN_STABLE = 0,
    OSUSCOREORIGIN_WITHSLIDERACC = 1,
    OSUSCOREORIGIN_WITHOUTSLIDERACC = 2,
} OsuScoreOrigin;

struct SliderData {
    uint32_t repeats;
    ExpectedDistance expected_dist;
};

typedef uint64_t Version;

struct BeatmapAttributes {
    double ar;
    double od;
    float cs;
    float hp;
    double clock_rate;
    HitWindows hit_windows;
};

struct TaikoDifficultyAttributes {
    double stamina;
    double rhythm;
    double color;
    double reading;
    double great_hit_window;
    double ok_hit_window;
    double mono_stamina_factor;
    double mechanical_difficulty;
    double consistency_factor;
    double stars;
    uint32_t max_combo;
    bool is_convert;
};

struct Wire_Vec_HitObject { uint8_t *data; uint32_t len; uint32_t capacity; };

typedef enum Mode {
    MODE_OSU = 0,
    MODE_TAIKO = 1,
    MODE_CATCH = 2,
    MODE_MANIA = 3,
} Mode;

struct TaikoPerformanceAttributes {
    TaikoDifficultyAttributes difficulty;
    double pp;
    double pp_acc;
    double pp_difficulty;
    Option_f64 estimated_unstable_rate;
};

struct HitObjectData {
    uint32_t variant;
    union {
        SliderData slider;
        DurationData spinner;
        DurationData hold;
    } payload;
};

struct Slice_Mode { const Mode *data; uintptr_t len; };

struct OsuDifficultyAttributes {
    double aim;
    double aim_difficult_slider_count;
    double speed;
    double flashlight;
    double reading;
    double slider_factor;
    double aim_top_weighted_slider_factor;
    double speed_top_weighted_slider_factor;
    double speed_note_count;
    double aim_difficult_strain_count;
    double speed_difficult_strain_count;
    double reading_difficult_note_count;
    double nested_score_per_object;
    double legacy_score_base_multiplier;
    double maximum_legacy_combo_score;
    double ar;
    double great_hit_window;
    double ok_hit_window;
    double meh_hit_window;
    double hp;
    uint32_t n_circles;
    uint32_t n_sliders;
    uint32_t n_large_ticks;
    uint32_t n_spinners;
    double stars;
    uint32_t max_combo;
};

struct Option_u32 { uint32_t variant; uint32_t some; };

struct OsuPerformanceAttributes {
    OsuDifficultyAttributes difficulty;
    double pp;
    double pp_acc;
    double pp_aim;
    double pp_flashlight;
    double pp_reading;
    double pp_speed;
    double effective_miss_count;
    Option_f64 speed_deviation;
    double combo_based_estimated_miss_count;
    Option_f64 score_based_estimated_miss_count;
    double aim_estimated_slider_breaks;
    double speed_estimated_slider_breaks;
};

struct Option_TooSuspicious { uint32_t variant; TooSuspicious some; };

struct ManiaPerformanceAttributes {
    ManiaDifficultyAttributes difficulty;
    double pp;
    double pp_difficulty;
};

struct HitObject {
    Pos pos;
    double start_time;
    HitObjectData data;
};

struct ScoreState {
    uint32_t max_combo;
    uint32_t osu_large_tick_hits;
    uint32_t osu_small_tick_hits;
    uint32_t slider_end_hits;
    uint32_t n_geki;
    uint32_t n_katu;
    uint32_t n300;
    uint32_t n100;
    uint32_t n50;
    uint32_t misses;
    Option_u32 legacy_total_score;
};

struct PerformanceAttributes {
    uint32_t variant;
    union {
        OsuPerformanceAttributes osu;
        TaikoPerformanceAttributes taiko;
        CatchPerformanceAttributes catch_;
        ManiaPerformanceAttributes mania;
    } payload;
};

struct Option_PerformanceAttributes { uint32_t variant; PerformanceAttributes some; };

struct LegacyDifficultyAttributes {
    LegacyVersion version;
    Mode mode;
    double stars;
    uint32_t max_combo;
    Option_f64 aim;
    Option_f64 aim_difficult_slider_count;
    Option_f64 speed;
    Option_f64 flashlight;
    Option_f64 slider_factor;
    Option_f64 aim_top_weighted_slider_factor;
    Option_f64 speed_top_weighted_slider_factor;
    Option_f64 speed_note_count;
    Option_f64 aim_difficult_strain_count;
    Option_f64 speed_difficult_strain_count;
    Option_f64 nested_score_per_object;
    Option_f64 legacy_score_base_multiplier;
    Option_f64 maximum_legacy_combo_score;
    Option_f64 stamina;
    Option_f64 rhythm;
    Option_f64 color;
    Option_f64 reading;
    Option_f64 peak;
    Option_f64 mechanical_difficulty;
    Option_f64 consistency_factor;
    Option_f64 ar;
    Option_f64 od;
    Option_f64 hp;
    Option_f64 hit_window;
    Option_f64 great_hit_window;
    Option_f64 ok_hit_window;
    Option_f64 meh_hit_window;
    Option_f64 preempt;
    Option_f64 mono_stamina_factor;
    Option_u32 n_circles;
    Option_u32 n_sliders;
    Option_u32 n_large_ticks;
    Option_u32 n_spinners;
    Option_u32 n_fruits;
    Option_u32 n_droplets;
    Option_u32 n_tiny_droplets;
    Option_u32 n_objects;
    Option_u32 n_hold_notes;
    Option_bool is_convert;
};

struct Option_LegacyDifficultyAttributes { uint32_t variant; LegacyDifficultyAttributes some; };

struct LegacyPerformanceAttributes {
    LegacyDifficultyAttributes difficulty;
    double pp;
    Option_f64 pp_acc;
    Option_f64 pp_aim;
    Option_f64 pp_speed;
    Option_f64 pp_flashlight;
    Option_f64 pp_difficulty;
    Option_f64 effective_miss_count;
    Option_f64 estimated_unstable_rate;
    Option_f64 speed_deviation;
    Option_f64 combo_based_estimated_miss_count;
    Option_f64 score_based_estimated_miss_count;
    Option_f64 aim_estimated_slider_breaks;
    Option_f64 speed_estimated_slider_breaks;
};

struct DifficultyAttributes {
    uint32_t variant;
    union {
        OsuDifficultyAttributes osu;
        TaikoDifficultyAttributes taiko;
        CatchDifficultyAttributes catch_;
        ManiaDifficultyAttributes mania;
    } payload;
};

struct Option_DifficultyAttributes { uint32_t variant; DifficultyAttributes some; };

void mods_sanitize(Mods * instance);
ResultPtrFFIError performance_create(void);
Option_f64 mods_clock_rate(Mods * instance);
void performance_n_katu(Performance * instance, uint32_t n_katu);
void performance_n50(Performance * instance, uint32_t n50);
ResultPtrFFIError mods_from_json(String str, Mode mode, bool deny_unknown_fields);
ResultPtrFFIError legacy_difficulty_create(void);
ResultPtrFFIError difficulty_create(void);
void beatmap_attributes_builder_mode(BeatmapAttributesBuilder * instance, Mode mode);
ResultPtrFFIError gradual_difficulty_create(const Difficulty * difficulty, const Beatmap * beatmap);
void legacy_performance_large_tick_hits(LegacyPerformance * instance, uint32_t large_tick_hits);
Option_LegacyDifficultyAttributes legacy_difficulty_calculate(LegacyDifficulty * instance, const LegacyBeatmap * beatmap, LegacyVersion version);
uint32_t mods_len(Mods * instance);
void difficulty_s_mods(Difficulty * instance, String str);
bool mods_insert_json(Mods * instance, String str, bool deny_unknown_fields);
void legacy_performance_combo(LegacyPerformance * instance, uint32_t combo);
void beatmap_attributes_builder_s_mods(BeatmapAttributesBuilder * instance, String str);
double beatmap_bpm(Beatmap * instance);
ResultPtrFFIError legacy_performance_create(void);
void performance_p_mods(Performance * instance, const Mods * mods);
Option_PerformanceAttributes gradual_performance_nth(GradualPerformance * instance, ScoreState state, uint32_t n);
void beatmap_attributes_builder_p_mods(BeatmapAttributesBuilder * instance, const Mods * mods);
void performance_clock_rate(Performance * instance, double clock_rate);
void beatmap_destroy(const Beatmap * instance);
Wire_Vec_HitObject beatmap_hit_objects(const Beatmap * instance);
void legacy_performance_i_mods(LegacyPerformance * instance, uint32_t mods);
void performance_small_tick_hits(Performance * instance, uint32_t small_tick_hits);
BeatmapAttributes beatmap_attributes_builder_build(const BeatmapAttributesBuilder * instance, const Beatmap * beatmap);
void performance_mode(Performance * instance, Mode mode);
Version __api_guard(void);
ResultPtrFFIError gradual_performance_create(const Difficulty * difficulty, const Beatmap * beatmap);
void legacy_performance_n50(LegacyPerformance * instance, uint32_t n50);
void legacy_performance_p_mods(LegacyPerformance * instance, const Mods * mods);
void performance_state(Performance * instance, ScoreState state);
void interoptopus_wire_destroy_78044(uint8_t * data, int32_t len, int32_t capacity);
Slice_Mode legacy_version_supported_modes(LegacyVersion version);
void legacy_performance_slider_end_hits(LegacyPerformance * instance, uint32_t slider_end_hits);
void performance_hp(Performance * instance, float hp);
void legacy_performance_lazer(LegacyPerformance * instance, bool lazer);
String debug_score_state(const ScoreState * res);
void difficulty_p_mods(Difficulty * instance, const Mods * mods);
void beatmap_attributes_builder_hp(BeatmapAttributesBuilder * instance, float hp);
LegacyVersion legacy_difficulty_version(const LegacyDifficulty * instance);
void beatmap_attributes_builder_cs(BeatmapAttributesBuilder * instance, float cs);
void difficulty_ar(Difficulty * instance, float ar);
void performance_n100(Performance * instance, uint32_t n100);
float beatmap_od(Beatmap * instance);
void difficulty_i_mods(Difficulty * instance, uint32_t mods);
void mods_clear(Mods * instance);
void difficulty_cs(Difficulty * instance, float cs);
Option_f64 beatmap_hit_object_end_time(const Beatmap * instance, uint32_t index);
Option_PerformanceAttributes gradual_performance_last(GradualPerformance * instance, ScoreState state);
Option_DifficultyAttributes gradual_difficulty_next(GradualDifficulty * instance);
uint32_t gradual_performance_len(const GradualPerformance * instance);
void beatmap_attributes_builder_i_mods(BeatmapAttributesBuilder * instance, uint32_t mods);
void gradual_difficulty_destroy(const GradualDifficulty * instance);
void gradual_performance_destroy(const GradualPerformance * instance);
void legacy_performance_destroy(const LegacyPerformance * instance);
float beatmap_ar(Beatmap * instance);
void legacy_performance_n_katu(LegacyPerformance * instance, uint32_t n_katu);
double calculate_accuacy(const ScoreState * state, const DifficultyAttributes * difficulty, OsuScoreOrigin origin);
void legacy_performance_score(LegacyPerformance * instance, uint32_t score);
Mode legacy_difficulty_mode(const LegacyDifficulty * instance);
void performance_accuracy(Performance * instance, double accuracy);
void performance_misses(Performance * instance, uint32_t misses);
double beatmap_slider_tick_rate(Beatmap * instance);
double legacy_difficulty_stars(const LegacyDifficulty * instance);
uint32_t legacy_difficulty_max_combo(const LegacyDifficulty * instance);
void legacy_performance_small_tick_hits(LegacyPerformance * instance, uint32_t small_tick_hits);
bool beatmap_is_convert(Beatmap * instance);
ResultPtrFFIError gradual_performance_new_with_mode(const Difficulty * difficulty, const Beatmap * beatmap, Mode mode);
void legacy_performance_n300(LegacyPerformance * instance, uint32_t n300);
uint32_t mods_bits(Mods * instance);
void legacy_difficulty_destroy(const LegacyDifficulty * instance);
float beatmap_stack_leniency(Beatmap * instance);
ResultPtrFFIError beatmap_attributes_builder_create(void);
void beatmap_attributes_builder_ar(BeatmapAttributesBuilder * instance, float ar);
void legacy_difficulty_set_mode(LegacyDifficulty * instance, Mode mode);
void performance_combo(Performance * instance, uint32_t combo);
void legacy_performance_accuracy(LegacyPerformance * instance, double accuracy);
PerformanceAttributes performance_calculate_from_difficulty(const Performance * instance, DifficultyAttributes difficulty_attr);
void legacy_performance_misses(LegacyPerformance * instance, uint32_t misses);
void mods_destroy(const Mods * instance);
void legacy_difficulty_clock_rate(LegacyDifficulty * instance, double clock_rate);
void mods_insert(Mods * instance, String str);
String mods_json(const Mods * instance);
float beatmap_hp(Beatmap * instance);
void difficulty_od(Difficulty * instance, float od);
ResultPtrFFIError beatmap_from_bytes(Slice_u8 data);
void performance_passed_objects(Performance * instance, uint32_t passed_objects);
Option_TooSuspicious beatmap_check_suspicious(Beatmap * instance);
void performance_n_geki(Performance * instance, uint32_t n_geki);
void difficulty_passed_objects(Difficulty * instance, uint32_t passed_objects);
void difficulty_lazer(Difficulty * instance, bool lazer);
ResultPtrFFIError gradual_difficulty_new_with_mode(const Difficulty * difficulty, const Beatmap * beatmap, Mode mode);
void legacy_performance_n_geki(LegacyPerformance * instance, uint32_t n_geki);
void performance_i_mods(Performance * instance, uint32_t mods);
void legacy_difficulty_passed_objects(LegacyDifficulty * instance, uint32_t passed_objects);
void performance_destroy(const Performance * instance);
void performance_hitresult_priority(Performance * instance, HitResultPriority hitresult_priority);
void legacy_difficulty_mods(LegacyDifficulty * instance, uint32_t mods);
Option_DifficultyAttributes gradual_difficulty_nth(GradualDifficulty * instance, uint32_t n);
ResultPtrFFIError legacy_performance_calculate(const LegacyPerformance * instance, const LegacyBeatmap * beatmap, const LegacyDifficulty * difficulty);
void performance_hardrock_offsets(Performance * instance, bool hardrock_offsets);
void performance_cs(Performance * instance, float cs);
Mode beatmap_mode(Beatmap * instance);
void legacy_beatmap_destroy(const LegacyBeatmap * instance);
ResultPtrFFIError mods_from_bits(uint32_t bits, Mode mode);
Option_PerformanceAttributes gradual_performance_next(GradualPerformance * instance, ScoreState state);
uint8_t * interoptopus_wire_create_75623(int32_t size, int32_t * out_len, int32_t * out_capacity);
ResultPtrFFIError mods_create(Mode mode);
int32_t beatmap_version(Beatmap * instance);
void performance_od(Performance * instance, float od);
int64_t interoptopus_string_clone(const String * utf8, String * rval);
double beatmap_total_break_time(Beatmap * instance);
int64_t interoptopus_string_create(const void * utf8, uint64_t len, String * rval);
void beatmap_attributes_builder_destroy(const BeatmapAttributesBuilder * instance);
DifficultyAttributes difficulty_calculate(const Difficulty * instance, const Beatmap * beatmap);
String debug_performance_attributes(const PerformanceAttributes * res);
void performance_large_tick_hits(Performance * instance, uint32_t large_tick_hits);
double difficulty_get_clock_rate(Difficulty * instance);
void beatmap_attributes_builder_clock_rate(BeatmapAttributesBuilder * instance, double clock_rate);
float beatmap_cs(Beatmap * instance);
ResultPtrFFIError legacy_beatmap_from_bytes(Slice_u8 data);
double beatmap_slider_multiplier(Beatmap * instance);
void legacy_performance_n100(LegacyPerformance * instance, uint32_t n100);
bool beatmap_convert(Beatmap * instance, Mode mode, const Mods * mods);
int64_t interoptopus_string_destroy(String utf8);
ScoreState performance_generate_state_from_difficulty(const Performance * instance, DifficultyAttributes difficulty_attr);
void performance_n300(Performance * instance, uint32_t n300);
void performance_ar(Performance * instance, float ar);
void performance_slider_end_hits(Performance * instance, uint32_t slider_end_hits);
void beatmap_attributes_builder_od(BeatmapAttributesBuilder * instance, float od);
ScoreState performance_generate_state(const Performance * instance, const Beatmap * beatmap);
double beatmap_attributes_builder_get_clock_rate(BeatmapAttributesBuilder * instance);
void mods_remove_unknown_mods(Mods * instance);
PerformanceAttributes performance_calculate(const Performance * instance, const Beatmap * beatmap);
void difficulty_destroy(const Difficulty * instance);
void difficulty_hp(Difficulty * instance, float hp);
void performance_legacy_total_score(Performance * instance, uint32_t legacy_total_score);
void difficulty_hardrock_offsets(Difficulty * instance, bool hardrock_offsets);
void legacy_performance_s_mods(LegacyPerformance * instance, String str);
void performance_s_mods(Performance * instance, String str);
String debug_difficulty_attributes(const DifficultyAttributes * res);
void legacy_performance_legacy_total_score(LegacyPerformance * instance, uint32_t legacy_total_score);
bool mods_contains(const Mods * instance, String str);
void difficulty_clock_rate(Difficulty * instance, double clock_rate);
uint32_t gradual_difficulty_len(const GradualDifficulty * instance);
ResultPtrFFIError beatmap_from_path(String path);
double performance_get_clock_rate(Performance * instance);
ResultPtrFFIError mods_from_acronyms(String str, Mode mode);
void performance_lazer(Performance * instance, bool lazer);

#ifdef __cplusplus
}
#endif
#endif
