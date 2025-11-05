from __future__ import annotations
import ctypes
import typing

T = typing.TypeVar("T")
c_lib = None

def init_lib(path):
    """Initializes the native library. Must be called at least once before anything else."""
    global c_lib
    c_lib = ctypes.cdll.LoadLibrary(path)
    c_lib.beatmap_ar.argtypes = [ctypes.c_void_p]
    c_lib.beatmap_attributes_ar.argtypes = [ctypes.c_void_p, ctypes.c_float]
    c_lib.beatmap_attributes_build.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
    c_lib.beatmap_attributes_clock_rate.argtypes = [ctypes.c_void_p, ctypes.c_double]
    c_lib.beatmap_attributes_cs.argtypes = [ctypes.c_void_p, ctypes.c_float]
    c_lib.beatmap_attributes_destroy.argtypes = [ctypes.c_void_p]
    c_lib.beatmap_attributes_get_clock_rate.argtypes = [ctypes.c_void_p]
    c_lib.beatmap_attributes_hp.argtypes = [ctypes.c_void_p, ctypes.c_float]
    c_lib.beatmap_attributes_i_mods.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
    c_lib.beatmap_attributes_mode.argtypes = [ctypes.c_void_p, ctypes.c_int]
    c_lib.beatmap_attributes_new.argtypes = []
    c_lib.beatmap_attributes_od.argtypes = [ctypes.c_void_p, ctypes.c_float]
    c_lib.beatmap_attributes_p_mods.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
    c_lib.beatmap_attributes_s_mods.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_char)]
    c_lib.beatmap_bpm.argtypes = [ctypes.c_void_p]
    c_lib.beatmap_convert.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]
    c_lib.beatmap_cs.argtypes = [ctypes.c_void_p]
    c_lib.beatmap_destroy.argtypes = [ctypes.c_void_p]
    c_lib.beatmap_from_bytes.argtypes = [SliceU8]
    c_lib.beatmap_from_path.argtypes = [ctypes.POINTER(ctypes.c_char)]
    c_lib.beatmap_hit_objects.argtypes = [ctypes.c_void_p]
    c_lib.beatmap_hp.argtypes = [ctypes.c_void_p]
    c_lib.beatmap_is_convert.argtypes = [ctypes.c_void_p]
    c_lib.beatmap_mode.argtypes = [ctypes.c_void_p]
    c_lib.beatmap_od.argtypes = [ctypes.c_void_p]
    c_lib.beatmap_slider_multiplier.argtypes = [ctypes.c_void_p]
    c_lib.beatmap_slider_tick_rate.argtypes = [ctypes.c_void_p]
    c_lib.beatmap_stack_leniency.argtypes = [ctypes.c_void_p]
    c_lib.beatmap_total_break_time.argtypes = [ctypes.c_void_p]
    c_lib.beatmap_version.argtypes = [ctypes.c_void_p]
    c_lib.calculate_accuracy.argtypes = [ctypes.POINTER(ScoreState), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
    c_lib.debug_difficulty_attributes.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_void_p]
    c_lib.debug_performance_attributes.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_void_p]
    c_lib.debug_score_state.argtypes = [ctypes.POINTER(ScoreState), ctypes.c_void_p]
    c_lib.difficulty_ar.argtypes = [ctypes.c_void_p, ctypes.c_float]
    c_lib.difficulty_calculate.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
    c_lib.difficulty_clock_rate.argtypes = [ctypes.c_void_p, ctypes.c_double]
    c_lib.difficulty_cs.argtypes = [ctypes.c_void_p, ctypes.c_float]
    c_lib.difficulty_destroy.argtypes = [ctypes.c_void_p]
    c_lib.difficulty_get_clock_rate.argtypes = [ctypes.c_void_p]
    c_lib.difficulty_hardrock_offsets.argtypes = [ctypes.c_void_p, ctypes.c_bool]
    c_lib.difficulty_hp.argtypes = [ctypes.c_void_p, ctypes.c_float]
    c_lib.difficulty_i_mods.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
    c_lib.difficulty_lazer.argtypes = [ctypes.c_void_p, ctypes.c_bool]
    c_lib.difficulty_new.argtypes = []
    c_lib.difficulty_od.argtypes = [ctypes.c_void_p, ctypes.c_float]
    c_lib.difficulty_p_mods.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
    c_lib.difficulty_passed_objects.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
    c_lib.difficulty_s_mods.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_char)]
    c_lib.gradual_difficulty_destroy.argtypes = [ctypes.c_void_p]
    c_lib.gradual_difficulty_len.argtypes = [ctypes.c_void_p]
    c_lib.gradual_difficulty_new.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
    c_lib.gradual_difficulty_new_with_mode.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]
    c_lib.gradual_difficulty_next.argtypes = [ctypes.c_void_p]
    c_lib.gradual_difficulty_nth.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
    c_lib.gradual_performance_destroy.argtypes = [ctypes.c_void_p]
    c_lib.gradual_performance_last.argtypes = [ctypes.c_void_p, ScoreState]
    c_lib.gradual_performance_len.argtypes = [ctypes.c_void_p]
    c_lib.gradual_performance_new.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
    c_lib.gradual_performance_new_with_mode.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]
    c_lib.gradual_performance_next.argtypes = [ctypes.c_void_p, ScoreState]
    c_lib.gradual_performance_nth.argtypes = [ctypes.c_void_p, ScoreState, ctypes.c_uint32]
    c_lib.interoptopus_string_clone.argtypes = [ctypes.POINTER(Utf8String), ctypes.POINTER(Utf8String)]
    c_lib.interoptopus_string_create.argtypes = [ctypes.c_void_p, ctypes.c_uint64, ctypes.POINTER(Utf8String)]
    c_lib.interoptopus_string_destroy.argtypes = [Utf8String]
    c_lib.interoptopus_vec_create_1095792466183922639.argtypes = [ctypes.c_void_p, ctypes.c_uint64, ctypes.POINTER(VecHitObject)]
    c_lib.interoptopus_vec_destroy_7642792079161229908.argtypes = [VecHitObject]
    c_lib.interoptopus_wire_destroy.argtypes = [ctypes.POINTER(ctypes.c_uint8), ctypes.c_int32, ctypes.c_int32]
    c_lib.mods_bits.argtypes = [ctypes.c_void_p]
    c_lib.mods_clear.argtypes = [ctypes.c_void_p]
    c_lib.mods_clock_rate.argtypes = [ctypes.c_void_p]
    c_lib.mods_contains.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_char)]
    c_lib.mods_destroy.argtypes = [ctypes.c_void_p]
    c_lib.mods_from_acronyms.argtypes = [ctypes.POINTER(ctypes.c_char), ctypes.c_int]
    c_lib.mods_from_bits.argtypes = [ctypes.c_uint32, ctypes.c_int]
    c_lib.mods_from_json.argtypes = [ctypes.POINTER(ctypes.c_char), ctypes.c_int, ctypes.c_bool]
    c_lib.mods_insert.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_char)]
    c_lib.mods_insert_json.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_bool]
    c_lib.mods_json.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
    c_lib.mods_len.argtypes = [ctypes.c_void_p]
    c_lib.mods_new.argtypes = [ctypes.c_int]
    c_lib.mods_remove_unknown_mods.argtypes = [ctypes.c_void_p]
    c_lib.mods_sanitize.argtypes = [ctypes.c_void_p]
    c_lib.performance_accuracy.argtypes = [ctypes.c_void_p, ctypes.c_double]
    c_lib.performance_ar.argtypes = [ctypes.c_void_p, ctypes.c_float]
    c_lib.performance_calculate.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
    c_lib.performance_calculate_from_difficulty.argtypes = [ctypes.c_void_p, ctypes.c_int]
    c_lib.performance_clock_rate.argtypes = [ctypes.c_void_p, ctypes.c_double]
    c_lib.performance_combo.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
    c_lib.performance_cs.argtypes = [ctypes.c_void_p, ctypes.c_float]
    c_lib.performance_destroy.argtypes = [ctypes.c_void_p]
    c_lib.performance_generate_state.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
    c_lib.performance_generate_state_from_difficulty.argtypes = [ctypes.c_void_p, ctypes.c_int]
    c_lib.performance_get_clock_rate.argtypes = [ctypes.c_void_p]
    c_lib.performance_hardrock_offsets.argtypes = [ctypes.c_void_p, ctypes.c_bool]
    c_lib.performance_hitresult_priority.argtypes = [ctypes.c_void_p, ctypes.c_int]
    c_lib.performance_hp.argtypes = [ctypes.c_void_p, ctypes.c_float]
    c_lib.performance_i_mods.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
    c_lib.performance_large_tick_hits.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
    c_lib.performance_lazer.argtypes = [ctypes.c_void_p, ctypes.c_bool]
    c_lib.performance_misses.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
    c_lib.performance_mode.argtypes = [ctypes.c_void_p, ctypes.c_int]
    c_lib.performance_n100.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
    c_lib.performance_n300.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
    c_lib.performance_n50.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
    c_lib.performance_n_geki.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
    c_lib.performance_n_katu.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
    c_lib.performance_new.argtypes = []
    c_lib.performance_od.argtypes = [ctypes.c_void_p, ctypes.c_float]
    c_lib.performance_p_mods.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
    c_lib.performance_passed_objects.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
    c_lib.performance_s_mods.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_char)]
    c_lib.performance_slider_end_hits.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
    c_lib.performance_small_tick_hits.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
    c_lib.performance_state.argtypes = [ctypes.c_void_p, ScoreState]
    c_lib.string_destroy.argtypes = [ctypes.c_void_p]
    c_lib.string_empty.argtypes = []
    c_lib.string_from_c_str.argtypes = [ctypes.POINTER(ctypes.c_char)]
    c_lib.string_is_init.argtypes = [ctypes.c_void_p]
    c_lib.string_to_cstr.argtypes = [ctypes.c_void_p]
    c_lib.beatmap_ar.restype = ctypes.c_float
    c_lib.beatmap_attributes_ar.restype = 
    c_lib.beatmap_attributes_build.restype = BeatmapAttributes
    c_lib.beatmap_attributes_clock_rate.restype = 
    c_lib.beatmap_attributes_cs.restype = 
    c_lib.beatmap_attributes_destroy.restype = ResultConstPtrBeatmapAttributesBuilderError
    c_lib.beatmap_attributes_get_clock_rate.restype = ctypes.c_double
    c_lib.beatmap_attributes_hp.restype = 
    c_lib.beatmap_attributes_i_mods.restype = 
    c_lib.beatmap_attributes_mode.restype = 
    c_lib.beatmap_attributes_new.restype = ResultConstPtrBeatmapAttributesBuilderError
    c_lib.beatmap_attributes_od.restype = 
    c_lib.beatmap_attributes_p_mods.restype = 
    c_lib.beatmap_attributes_s_mods.restype = ResultError
    c_lib.beatmap_bpm.restype = ctypes.c_double
    c_lib.beatmap_convert.restype = ctypes.c_bool
    c_lib.beatmap_cs.restype = ctypes.c_float
    c_lib.beatmap_destroy.restype = ResultConstPtrBeatmapError
    c_lib.beatmap_from_bytes.restype = ResultConstPtrBeatmapError
    c_lib.beatmap_from_path.restype = ResultConstPtrBeatmapError
    c_lib.beatmap_hit_objects.restype = VecHitObject
    c_lib.beatmap_hp.restype = ctypes.c_float
    c_lib.beatmap_is_convert.restype = ctypes.c_bool
    c_lib.beatmap_mode.restype = ctypes.c_int
    c_lib.beatmap_od.restype = ctypes.c_float
    c_lib.beatmap_slider_multiplier.restype = ctypes.c_double
    c_lib.beatmap_slider_tick_rate.restype = ctypes.c_double
    c_lib.beatmap_stack_leniency.restype = ctypes.c_float
    c_lib.beatmap_total_break_time.restype = ctypes.c_double
    c_lib.beatmap_version.restype = ctypes.c_int32
    c_lib.calculate_accuracy.restype = ctypes.c_double
    c_lib.debug_difficulty_attributes.restype = 
    c_lib.debug_performance_attributes.restype = 
    c_lib.debug_score_state.restype = 
    c_lib.difficulty_ar.restype = 
    c_lib.difficulty_calculate.restype = ctypes.c_int
    c_lib.difficulty_clock_rate.restype = 
    c_lib.difficulty_cs.restype = 
    c_lib.difficulty_destroy.restype = ResultConstPtrDifficultyError
    c_lib.difficulty_get_clock_rate.restype = ctypes.c_double
    c_lib.difficulty_hardrock_offsets.restype = 
    c_lib.difficulty_hp.restype = 
    c_lib.difficulty_i_mods.restype = 
    c_lib.difficulty_lazer.restype = 
    c_lib.difficulty_new.restype = ResultConstPtrDifficultyError
    c_lib.difficulty_od.restype = 
    c_lib.difficulty_p_mods.restype = 
    c_lib.difficulty_passed_objects.restype = 
    c_lib.difficulty_s_mods.restype = ResultError
    c_lib.gradual_difficulty_destroy.restype = ResultConstPtrGradualDifficultyError
    c_lib.gradual_difficulty_len.restype = ctypes.c_uint32
    c_lib.gradual_difficulty_new.restype = ResultConstPtrGradualDifficultyError
    c_lib.gradual_difficulty_new_with_mode.restype = ResultConstPtrGradualDifficultyError
    c_lib.gradual_difficulty_next.restype = TODO
    c_lib.gradual_difficulty_nth.restype = TODO
    c_lib.gradual_performance_destroy.restype = ResultConstPtrGradualPerformanceError
    c_lib.gradual_performance_last.restype = TODO
    c_lib.gradual_performance_len.restype = ctypes.c_uint32
    c_lib.gradual_performance_new.restype = ResultConstPtrGradualPerformanceError
    c_lib.gradual_performance_new_with_mode.restype = ResultConstPtrGradualPerformanceError
    c_lib.gradual_performance_next.restype = TODO
    c_lib.gradual_performance_nth.restype = TODO
    c_lib.interoptopus_string_clone.restype = ctypes.c_int64
    c_lib.interoptopus_string_create.restype = ctypes.c_int64
    c_lib.interoptopus_string_destroy.restype = ctypes.c_int64
    c_lib.interoptopus_vec_create_1095792466183922639.restype = ctypes.c_int64
    c_lib.interoptopus_vec_destroy_7642792079161229908.restype = ctypes.c_int64
    c_lib.interoptopus_wire_destroy.restype = 
    c_lib.mods_bits.restype = ctypes.c_uint32
    c_lib.mods_clear.restype = 
    c_lib.mods_clock_rate.restype = TODO
    c_lib.mods_contains.restype = ctypes.c_bool
    c_lib.mods_destroy.restype = ResultConstPtrModsError
    c_lib.mods_from_acronyms.restype = ResultConstPtrModsError
    c_lib.mods_from_bits.restype = ResultConstPtrModsError
    c_lib.mods_from_json.restype = ResultConstPtrModsError
    c_lib.mods_insert.restype = ctypes.c_bool
    c_lib.mods_insert_json.restype = ctypes.c_bool
    c_lib.mods_json.restype = 
    c_lib.mods_len.restype = ctypes.c_uint32
    c_lib.mods_new.restype = ResultConstPtrModsError
    c_lib.mods_remove_unknown_mods.restype = 
    c_lib.mods_sanitize.restype = 
    c_lib.performance_accuracy.restype = 
    c_lib.performance_ar.restype = 
    c_lib.performance_calculate.restype = ctypes.c_int
    c_lib.performance_calculate_from_difficulty.restype = ctypes.c_int
    c_lib.performance_clock_rate.restype = 
    c_lib.performance_combo.restype = 
    c_lib.performance_cs.restype = 
    c_lib.performance_destroy.restype = ResultConstPtrPerformanceError
    c_lib.performance_generate_state.restype = ScoreState
    c_lib.performance_generate_state_from_difficulty.restype = ScoreState
    c_lib.performance_get_clock_rate.restype = ctypes.c_double
    c_lib.performance_hardrock_offsets.restype = 
    c_lib.performance_hitresult_priority.restype = 
    c_lib.performance_hp.restype = 
    c_lib.performance_i_mods.restype = 
    c_lib.performance_large_tick_hits.restype = 
    c_lib.performance_lazer.restype = 
    c_lib.performance_misses.restype = 
    c_lib.performance_mode.restype = 
    c_lib.performance_n100.restype = 
    c_lib.performance_n300.restype = 
    c_lib.performance_n50.restype = 
    c_lib.performance_n_geki.restype = 
    c_lib.performance_n_katu.restype = 
    c_lib.performance_new.restype = ResultConstPtrPerformanceError
    c_lib.performance_od.restype = 
    c_lib.performance_p_mods.restype = 
    c_lib.performance_passed_objects.restype = 
    c_lib.performance_s_mods.restype = ResultError
    c_lib.performance_slider_end_hits.restype = 
    c_lib.performance_small_tick_hits.restype = 
    c_lib.performance_state.restype = 
    c_lib.string_destroy.restype = ResultConstPtrOwnedStringError
    c_lib.string_empty.restype = ResultConstPtrOwnedStringError
    c_lib.string_from_c_str.restype = ResultConstPtrOwnedStringError
    c_lib.string_is_init.restype = ctypes.c_bool
    c_lib.string_to_cstr.restype = ctypes.POINTER(ctypes.c_char)


def debug_difficulty_attributes(res: ctypes.POINTER(ctypes.c_int), str: ctypes.c_void_p):
    return c_lib.debug_difficulty_attributes(res, str)

def debug_performance_attributes(res: ctypes.POINTER(ctypes.c_int), str: ctypes.c_void_p):
    return c_lib.debug_performance_attributes(res, str)

def debug_score_state(res: ctypes.POINTER(ScoreState), str: ctypes.c_void_p):
    return c_lib.debug_score_state(res, str)

def calculate_accuracy(state: ctypes.POINTER(ScoreState), difficulty: ctypes.POINTER(ctypes.c_int), origin: TODO) -> float:
    return c_lib.calculate_accuracy(state, difficulty, origin)

def interoptopus_string_create(utf8: ctypes.c_void_p, len: int, rval: ctypes.POINTER(Utf8String)) -> int:
    return c_lib.interoptopus_string_create(utf8, len, rval)

def interoptopus_string_destroy(utf8) -> int:
    return c_lib.interoptopus_string_destroy(utf8)

def interoptopus_string_clone(utf8: ctypes.POINTER(Utf8String), rval: ctypes.POINTER(Utf8String)) -> int:
    return c_lib.interoptopus_string_clone(utf8, rval)

def interoptopus_wire_destroy(data: ctypes.POINTER(ctypes.c_uint8), len: int, capacity: int):
    return c_lib.interoptopus_wire_destroy(data, len, capacity)

def interoptopus_vec_create_1095792466183922639(data: ctypes.c_void_p, len: int, rval: ctypes.POINTER(VecHitObject)) -> int:
    return c_lib.interoptopus_vec_create_1095792466183922639(data, len, rval)

def interoptopus_vec_destroy_7642792079161229908(ignored) -> int:
    return c_lib.interoptopus_vec_destroy_7642792079161229908(ignored)






TRUE = ctypes.c_uint8(1)
FALSE = ctypes.c_uint8(0)


def _errcheck(returned, success):
    """Checks for FFIErrors and converts them to an exception."""
    if returned == success: return
    else: raise Exception(f"Function returned error: {returned}")


class CallbackVars(object):
    """Helper to be used `lambda x: setattr(cv, "x", x)` when getting values from callbacks."""
    def __str__(self):
        rval = ""
        for var in  filter(lambda x: "__" not in x, dir(self)):
            rval += f"{var}: {getattr(self, var)}"
        return rval


class _Iter(object):
    """Helper for slice iterators."""
    def __init__(self, target):
        self.i = 0
        self.target = target

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i >= self.target.len:
            raise StopIteration()
        rval = self.target[self.i]
        self.i += 1
        return rval


class Error:
    Unknown = 0
    Null = 1
    IO = 2
    InvalidString = 3
    UTF8 = 4
    Serialize = 5
    Convert = 6


class HitObjectKind:
    Circle = 0
    Slider = 1
    Spinner = 2
    Hold = 3


class HitResultPriority:
    BestCase = 0
    WorstCase = 1


class Mode:
    #  osu!standard
    Osu = 0
    #  osu!taiko
    Taiko = 1
    #  osu!catch
    Catch = 2
    #  osu!mania
    Mania = 3


class OsuScoreOrigin:
    """ Type to pass [`OsuScoreState::accuracy`] and specify the origin of a score."""
    #  For scores set on osu!stable
    Stable = 0
    #  For scores set on osu!lazer with slider accuracy
    WithSliderAcc = 1
    #  For scores set on osu!lazer without slider accuracy
    WithoutSliderAcc = 2


class Utf8String(ctypes.Structure):
    """ UTF-8 string marshalling helper.
 A highly dangerous 'use once type' that has ownership semantics!
 Once passed over an FFI boundary 'the other side' is meant to own
 (and free) it. Rust handles that fine, but if in C# you put this
 in a struct and then call Rust multiple times with that struct 
 you'll free the same pointer multiple times, and get UB!"""

    # These fields represent the underlying C data layout
    _fields_ = [
        ("ptr", ctypes.POINTER(ctypes.c_uint8)),
        ("len", ctypes.c_uint64),
        ("capacity", ctypes.c_uint64),
    ]

    def __init__(self, ptr: ctypes.POINTER(ctypes.c_uint8) = None, len: int = None, capacity: int = None):
        if ptr is not None:
            self.ptr = ptr
        if len is not None:
            self.len = len
        if capacity is not None:
            self.capacity = capacity

    @property
    def ptr(self) -> ctypes.POINTER(ctypes.c_uint8):
        return ctypes.Structure.__get__(self, "ptr")

    @ptr.setter
    def ptr(self, value: ctypes.POINTER(ctypes.c_uint8)):
        return ctypes.Structure.__set__(self, "ptr", value)

    @property
    def len(self) -> int:
        return ctypes.Structure.__get__(self, "len")

    @len.setter
    def len(self, value: int):
        return ctypes.Structure.__set__(self, "len", value)

    @property
    def capacity(self) -> int:
        return ctypes.Structure.__get__(self, "capacity")

    @capacity.setter
    def capacity(self, value: int):
        return ctypes.Structure.__set__(self, "capacity", value)


class CatchDifficultyAttributes(ctypes.Structure):
    """ The result of a difficulty calculation on an osu!catch map."""

    # These fields represent the underlying C data layout
    _fields_ = [
        ("stars", ctypes.c_double),
        ("ar", ctypes.c_double),
        ("n_fruits", ctypes.c_uint32),
        ("n_droplets", ctypes.c_uint32),
        ("n_tiny_droplets", ctypes.c_uint32),
        ("is_convert", ctypes.c_bool),
    ]

    def __init__(self, stars: float = None, ar: float = None, n_fruits: int = None, n_droplets: int = None, n_tiny_droplets: int = None, is_convert: bool = None):
        if stars is not None:
            self.stars = stars
        if ar is not None:
            self.ar = ar
        if n_fruits is not None:
            self.n_fruits = n_fruits
        if n_droplets is not None:
            self.n_droplets = n_droplets
        if n_tiny_droplets is not None:
            self.n_tiny_droplets = n_tiny_droplets
        if is_convert is not None:
            self.is_convert = is_convert

    @property
    def stars(self) -> float:
        """ The final star rating"""
        return ctypes.Structure.__get__(self, "stars")

    @stars.setter
    def stars(self, value: float):
        """ The final star rating"""
        return ctypes.Structure.__set__(self, "stars", value)

    @property
    def ar(self) -> float:
        """ The approach rate."""
        return ctypes.Structure.__get__(self, "ar")

    @ar.setter
    def ar(self, value: float):
        """ The approach rate."""
        return ctypes.Structure.__set__(self, "ar", value)

    @property
    def n_fruits(self) -> int:
        """ The amount of fruits."""
        return ctypes.Structure.__get__(self, "n_fruits")

    @n_fruits.setter
    def n_fruits(self, value: int):
        """ The amount of fruits."""
        return ctypes.Structure.__set__(self, "n_fruits", value)

    @property
    def n_droplets(self) -> int:
        """ The amount of droplets."""
        return ctypes.Structure.__get__(self, "n_droplets")

    @n_droplets.setter
    def n_droplets(self, value: int):
        """ The amount of droplets."""
        return ctypes.Structure.__set__(self, "n_droplets", value)

    @property
    def n_tiny_droplets(self) -> int:
        """ The amount of tiny droplets."""
        return ctypes.Structure.__get__(self, "n_tiny_droplets")

    @n_tiny_droplets.setter
    def n_tiny_droplets(self, value: int):
        """ The amount of tiny droplets."""
        return ctypes.Structure.__set__(self, "n_tiny_droplets", value)

    @property
    def is_convert(self) -> bool:
        """ Whether the [`Beatmap`] was a convert i.e. an osu!standard map.

 [`Beatmap`]: crate::model::beatmap::Beatmap"""
        return ctypes.Structure.__get__(self, "is_convert")

    @is_convert.setter
    def is_convert(self, value: bool):
        """ Whether the [`Beatmap`] was a convert i.e. an osu!standard map.

 [`Beatmap`]: crate::model::beatmap::Beatmap"""
        return ctypes.Structure.__set__(self, "is_convert", value)


class ManiaDifficultyAttributes(ctypes.Structure):
    """ The result of a difficulty calculation on an osu!mania map."""

    # These fields represent the underlying C data layout
    _fields_ = [
        ("stars", ctypes.c_double),
        ("n_objects", ctypes.c_uint32),
        ("n_hold_notes", ctypes.c_uint32),
        ("max_combo", ctypes.c_uint32),
        ("is_convert", ctypes.c_bool),
    ]

    def __init__(self, stars: float = None, n_objects: int = None, n_hold_notes: int = None, max_combo: int = None, is_convert: bool = None):
        if stars is not None:
            self.stars = stars
        if n_objects is not None:
            self.n_objects = n_objects
        if n_hold_notes is not None:
            self.n_hold_notes = n_hold_notes
        if max_combo is not None:
            self.max_combo = max_combo
        if is_convert is not None:
            self.is_convert = is_convert

    @property
    def stars(self) -> float:
        """ The final star rating."""
        return ctypes.Structure.__get__(self, "stars")

    @stars.setter
    def stars(self, value: float):
        """ The final star rating."""
        return ctypes.Structure.__set__(self, "stars", value)

    @property
    def n_objects(self) -> int:
        """ The amount of hitobjects in the map."""
        return ctypes.Structure.__get__(self, "n_objects")

    @n_objects.setter
    def n_objects(self, value: int):
        """ The amount of hitobjects in the map."""
        return ctypes.Structure.__set__(self, "n_objects", value)

    @property
    def n_hold_notes(self) -> int:
        """ The amount of hold notes in the map."""
        return ctypes.Structure.__get__(self, "n_hold_notes")

    @n_hold_notes.setter
    def n_hold_notes(self, value: int):
        """ The amount of hold notes in the map."""
        return ctypes.Structure.__set__(self, "n_hold_notes", value)

    @property
    def max_combo(self) -> int:
        """ The maximum achievable combo."""
        return ctypes.Structure.__get__(self, "max_combo")

    @max_combo.setter
    def max_combo(self, value: int):
        """ The maximum achievable combo."""
        return ctypes.Structure.__set__(self, "max_combo", value)

    @property
    def is_convert(self) -> bool:
        """ Whether the [`Beatmap`] was a convert i.e. an osu!standard map.

 [`Beatmap`]: crate::model::beatmap::Beatmap"""
        return ctypes.Structure.__get__(self, "is_convert")

    @is_convert.setter
    def is_convert(self, value: bool):
        """ Whether the [`Beatmap`] was a convert i.e. an osu!standard map.

 [`Beatmap`]: crate::model::beatmap::Beatmap"""
        return ctypes.Structure.__set__(self, "is_convert", value)


class OsuDifficultyAttributes(ctypes.Structure):
    """ The result of a difficulty calculation on an osu!standard map."""

    # These fields represent the underlying C data layout
    _fields_ = [
        ("aim", ctypes.c_double),
        ("aim_difficult_slider_count", ctypes.c_double),
        ("speed", ctypes.c_double),
        ("flashlight", ctypes.c_double),
        ("slider_factor", ctypes.c_double),
        ("speed_note_count", ctypes.c_double),
        ("aim_difficult_strain_count", ctypes.c_double),
        ("speed_difficult_strain_count", ctypes.c_double),
        ("ar", ctypes.c_double),
        ("great_hit_window", ctypes.c_double),
        ("ok_hit_window", ctypes.c_double),
        ("meh_hit_window", ctypes.c_double),
        ("hp", ctypes.c_double),
        ("n_circles", ctypes.c_uint32),
        ("n_sliders", ctypes.c_uint32),
        ("n_large_ticks", ctypes.c_uint32),
        ("n_spinners", ctypes.c_uint32),
        ("stars", ctypes.c_double),
        ("max_combo", ctypes.c_uint32),
    ]

    def __init__(self, aim: float = None, aim_difficult_slider_count: float = None, speed: float = None, flashlight: float = None, slider_factor: float = None, speed_note_count: float = None, aim_difficult_strain_count: float = None, speed_difficult_strain_count: float = None, ar: float = None, great_hit_window: float = None, ok_hit_window: float = None, meh_hit_window: float = None, hp: float = None, n_circles: int = None, n_sliders: int = None, n_large_ticks: int = None, n_spinners: int = None, stars: float = None, max_combo: int = None):
        if aim is not None:
            self.aim = aim
        if aim_difficult_slider_count is not None:
            self.aim_difficult_slider_count = aim_difficult_slider_count
        if speed is not None:
            self.speed = speed
        if flashlight is not None:
            self.flashlight = flashlight
        if slider_factor is not None:
            self.slider_factor = slider_factor
        if speed_note_count is not None:
            self.speed_note_count = speed_note_count
        if aim_difficult_strain_count is not None:
            self.aim_difficult_strain_count = aim_difficult_strain_count
        if speed_difficult_strain_count is not None:
            self.speed_difficult_strain_count = speed_difficult_strain_count
        if ar is not None:
            self.ar = ar
        if great_hit_window is not None:
            self.great_hit_window = great_hit_window
        if ok_hit_window is not None:
            self.ok_hit_window = ok_hit_window
        if meh_hit_window is not None:
            self.meh_hit_window = meh_hit_window
        if hp is not None:
            self.hp = hp
        if n_circles is not None:
            self.n_circles = n_circles
        if n_sliders is not None:
            self.n_sliders = n_sliders
        if n_large_ticks is not None:
            self.n_large_ticks = n_large_ticks
        if n_spinners is not None:
            self.n_spinners = n_spinners
        if stars is not None:
            self.stars = stars
        if max_combo is not None:
            self.max_combo = max_combo

    @property
    def aim(self) -> float:
        """ The difficulty of the aim skill."""
        return ctypes.Structure.__get__(self, "aim")

    @aim.setter
    def aim(self, value: float):
        """ The difficulty of the aim skill."""
        return ctypes.Structure.__set__(self, "aim", value)

    @property
    def aim_difficult_slider_count(self) -> float:
        """ The number of sliders weighted by difficulty."""
        return ctypes.Structure.__get__(self, "aim_difficult_slider_count")

    @aim_difficult_slider_count.setter
    def aim_difficult_slider_count(self, value: float):
        """ The number of sliders weighted by difficulty."""
        return ctypes.Structure.__set__(self, "aim_difficult_slider_count", value)

    @property
    def speed(self) -> float:
        """ The difficulty of the speed skill."""
        return ctypes.Structure.__get__(self, "speed")

    @speed.setter
    def speed(self, value: float):
        """ The difficulty of the speed skill."""
        return ctypes.Structure.__set__(self, "speed", value)

    @property
    def flashlight(self) -> float:
        """ The difficulty of the flashlight skill."""
        return ctypes.Structure.__get__(self, "flashlight")

    @flashlight.setter
    def flashlight(self, value: float):
        """ The difficulty of the flashlight skill."""
        return ctypes.Structure.__set__(self, "flashlight", value)

    @property
    def slider_factor(self) -> float:
        """ The ratio of the aim strain with and without considering sliders"""
        return ctypes.Structure.__get__(self, "slider_factor")

    @slider_factor.setter
    def slider_factor(self, value: float):
        """ The ratio of the aim strain with and without considering sliders"""
        return ctypes.Structure.__set__(self, "slider_factor", value)

    @property
    def speed_note_count(self) -> float:
        """ The number of clickable objects weighted by difficulty."""
        return ctypes.Structure.__get__(self, "speed_note_count")

    @speed_note_count.setter
    def speed_note_count(self, value: float):
        """ The number of clickable objects weighted by difficulty."""
        return ctypes.Structure.__set__(self, "speed_note_count", value)

    @property
    def aim_difficult_strain_count(self) -> float:
        """ Weighted sum of aim strains."""
        return ctypes.Structure.__get__(self, "aim_difficult_strain_count")

    @aim_difficult_strain_count.setter
    def aim_difficult_strain_count(self, value: float):
        """ Weighted sum of aim strains."""
        return ctypes.Structure.__set__(self, "aim_difficult_strain_count", value)

    @property
    def speed_difficult_strain_count(self) -> float:
        """ Weighted sum of speed strains."""
        return ctypes.Structure.__get__(self, "speed_difficult_strain_count")

    @speed_difficult_strain_count.setter
    def speed_difficult_strain_count(self, value: float):
        """ Weighted sum of speed strains."""
        return ctypes.Structure.__set__(self, "speed_difficult_strain_count", value)

    @property
    def ar(self) -> float:
        """ The approach rate."""
        return ctypes.Structure.__get__(self, "ar")

    @ar.setter
    def ar(self, value: float):
        """ The approach rate."""
        return ctypes.Structure.__set__(self, "ar", value)

    @property
    def great_hit_window(self) -> float:
        """ The great hit window."""
        return ctypes.Structure.__get__(self, "great_hit_window")

    @great_hit_window.setter
    def great_hit_window(self, value: float):
        """ The great hit window."""
        return ctypes.Structure.__set__(self, "great_hit_window", value)

    @property
    def ok_hit_window(self) -> float:
        """ The ok hit window."""
        return ctypes.Structure.__get__(self, "ok_hit_window")

    @ok_hit_window.setter
    def ok_hit_window(self, value: float):
        """ The ok hit window."""
        return ctypes.Structure.__set__(self, "ok_hit_window", value)

    @property
    def meh_hit_window(self) -> float:
        """ The meh hit window."""
        return ctypes.Structure.__get__(self, "meh_hit_window")

    @meh_hit_window.setter
    def meh_hit_window(self, value: float):
        """ The meh hit window."""
        return ctypes.Structure.__set__(self, "meh_hit_window", value)

    @property
    def hp(self) -> float:
        """ The overall difficulty"""
        return ctypes.Structure.__get__(self, "hp")

    @hp.setter
    def hp(self, value: float):
        """ The overall difficulty"""
        return ctypes.Structure.__set__(self, "hp", value)

    @property
    def n_circles(self) -> int:
        """ The amount of circles."""
        return ctypes.Structure.__get__(self, "n_circles")

    @n_circles.setter
    def n_circles(self, value: int):
        """ The amount of circles."""
        return ctypes.Structure.__set__(self, "n_circles", value)

    @property
    def n_sliders(self) -> int:
        """ The amount of sliders."""
        return ctypes.Structure.__get__(self, "n_sliders")

    @n_sliders.setter
    def n_sliders(self, value: int):
        """ The amount of sliders."""
        return ctypes.Structure.__set__(self, "n_sliders", value)

    @property
    def n_large_ticks(self) -> int:
        """ The amount of "large ticks".

 The meaning depends on the kind of score:
 - if set on osu!stable, this value is irrelevant
 - if set on osu!lazer *without* `CL`, this value is the amount of
   slider ticks and repeats
 - if set on osu!lazer *with* `CL`, this value is the amount of slider
   heads, ticks, and repeats"""
        return ctypes.Structure.__get__(self, "n_large_ticks")

    @n_large_ticks.setter
    def n_large_ticks(self, value: int):
        """ The amount of "large ticks".

 The meaning depends on the kind of score:
 - if set on osu!stable, this value is irrelevant
 - if set on osu!lazer *without* `CL`, this value is the amount of
   slider ticks and repeats
 - if set on osu!lazer *with* `CL`, this value is the amount of slider
   heads, ticks, and repeats"""
        return ctypes.Structure.__set__(self, "n_large_ticks", value)

    @property
    def n_spinners(self) -> int:
        """ The amount of spinners."""
        return ctypes.Structure.__get__(self, "n_spinners")

    @n_spinners.setter
    def n_spinners(self, value: int):
        """ The amount of spinners."""
        return ctypes.Structure.__set__(self, "n_spinners", value)

    @property
    def stars(self) -> float:
        """ The final star rating"""
        return ctypes.Structure.__get__(self, "stars")

    @stars.setter
    def stars(self, value: float):
        """ The final star rating"""
        return ctypes.Structure.__set__(self, "stars", value)

    @property
    def max_combo(self) -> int:
        """ The maximum combo."""
        return ctypes.Structure.__get__(self, "max_combo")

    @max_combo.setter
    def max_combo(self, value: int):
        """ The maximum combo."""
        return ctypes.Structure.__set__(self, "max_combo", value)


class Pos(ctypes.Structure):

    # These fields represent the underlying C data layout
    _fields_ = [
        ("x", ctypes.c_float),
        ("y", ctypes.c_float),
    ]

    def __init__(self, x: float = None, y: float = None):
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    @property
    def x(self) -> float:
        """ Position on the x-axis."""
        return ctypes.Structure.__get__(self, "x")

    @x.setter
    def x(self, value: float):
        """ Position on the x-axis."""
        return ctypes.Structure.__set__(self, "x", value)

    @property
    def y(self) -> float:
        """ Position on the y-axis."""
        return ctypes.Structure.__get__(self, "y")

    @y.setter
    def y(self, value: float):
        """ Position on the y-axis."""
        return ctypes.Structure.__set__(self, "y", value)


class ScoreState(ctypes.Structure):
    """ Aggregation for a score's current state."""

    # These fields represent the underlying C data layout
    _fields_ = [
        ("max_combo", ctypes.c_uint32),
        ("osu_large_tick_hits", ctypes.c_uint32),
        ("osu_small_tick_hits", ctypes.c_uint32),
        ("slider_end_hits", ctypes.c_uint32),
        ("n_geki", ctypes.c_uint32),
        ("n_katu", ctypes.c_uint32),
        ("n300", ctypes.c_uint32),
        ("n100", ctypes.c_uint32),
        ("n50", ctypes.c_uint32),
        ("misses", ctypes.c_uint32),
    ]

    def __init__(self, max_combo: int = None, osu_large_tick_hits: int = None, osu_small_tick_hits: int = None, slider_end_hits: int = None, n_geki: int = None, n_katu: int = None, n300: int = None, n100: int = None, n50: int = None, misses: int = None):
        if max_combo is not None:
            self.max_combo = max_combo
        if osu_large_tick_hits is not None:
            self.osu_large_tick_hits = osu_large_tick_hits
        if osu_small_tick_hits is not None:
            self.osu_small_tick_hits = osu_small_tick_hits
        if slider_end_hits is not None:
            self.slider_end_hits = slider_end_hits
        if n_geki is not None:
            self.n_geki = n_geki
        if n_katu is not None:
            self.n_katu = n_katu
        if n300 is not None:
            self.n300 = n300
        if n100 is not None:
            self.n100 = n100
        if n50 is not None:
            self.n50 = n50
        if misses is not None:
            self.misses = misses

    @property
    def max_combo(self) -> int:
        """ Maximum combo that the score has had so far. **Not** the maximum
 possible combo of the map so far.

 Note that for osu!catch only fruits and droplets are considered for
 combo.

 Irrelevant for osu!mania."""
        return ctypes.Structure.__get__(self, "max_combo")

    @max_combo.setter
    def max_combo(self, value: int):
        """ Maximum combo that the score has had so far. **Not** the maximum
 possible combo of the map so far.

 Note that for osu!catch only fruits and droplets are considered for
 combo.

 Irrelevant for osu!mania."""
        return ctypes.Structure.__set__(self, "max_combo", value)

    @property
    def osu_large_tick_hits(self) -> int:
        """ "Large tick" hits for osu!standard.

 The meaning depends on the kind of score:
 - if set on osu!stable, this field is irrelevant and can be `0`
 - if set on osu!lazer *without* `CL`, this field is the amount of hit
   slider ticks and repeats
 - if set on osu!lazer *with* `CL`, this field is the amount of hit
   slider heads, ticks, and repeats

 Only relevant for osu!lazer."""
        return ctypes.Structure.__get__(self, "osu_large_tick_hits")

    @osu_large_tick_hits.setter
    def osu_large_tick_hits(self, value: int):
        """ "Large tick" hits for osu!standard.

 The meaning depends on the kind of score:
 - if set on osu!stable, this field is irrelevant and can be `0`
 - if set on osu!lazer *without* `CL`, this field is the amount of hit
   slider ticks and repeats
 - if set on osu!lazer *with* `CL`, this field is the amount of hit
   slider heads, ticks, and repeats

 Only relevant for osu!lazer."""
        return ctypes.Structure.__set__(self, "osu_large_tick_hits", value)

    @property
    def osu_small_tick_hits(self) -> int:
        """ "Small ticks" hits for osu!standard.

 These are essentially the slider end hits for lazer scores without
 slider accuracy.

 Only relevant for osu!lazer."""
        return ctypes.Structure.__get__(self, "osu_small_tick_hits")

    @osu_small_tick_hits.setter
    def osu_small_tick_hits(self, value: int):
        """ "Small ticks" hits for osu!standard.

 These are essentially the slider end hits for lazer scores without
 slider accuracy.

 Only relevant for osu!lazer."""
        return ctypes.Structure.__set__(self, "osu_small_tick_hits", value)

    @property
    def slider_end_hits(self) -> int:
        """ Amount of successfully hit slider ends.

 Only relevant for osu!standard in lazer."""
        return ctypes.Structure.__get__(self, "slider_end_hits")

    @slider_end_hits.setter
    def slider_end_hits(self, value: int):
        """ Amount of successfully hit slider ends.

 Only relevant for osu!standard in lazer."""
        return ctypes.Structure.__set__(self, "slider_end_hits", value)

    @property
    def n_geki(self) -> int:
        """ Amount of current gekis (n320 for osu!mania)."""
        return ctypes.Structure.__get__(self, "n_geki")

    @n_geki.setter
    def n_geki(self, value: int):
        """ Amount of current gekis (n320 for osu!mania)."""
        return ctypes.Structure.__set__(self, "n_geki", value)

    @property
    def n_katu(self) -> int:
        """ Amount of current katus (tiny droplet misses for osu!catch / n200 for
 osu!mania)."""
        return ctypes.Structure.__get__(self, "n_katu")

    @n_katu.setter
    def n_katu(self, value: int):
        """ Amount of current katus (tiny droplet misses for osu!catch / n200 for
 osu!mania)."""
        return ctypes.Structure.__set__(self, "n_katu", value)

    @property
    def n300(self) -> int:
        """ Amount of current 300s (fruits for osu!catch)."""
        return ctypes.Structure.__get__(self, "n300")

    @n300.setter
    def n300(self, value: int):
        """ Amount of current 300s (fruits for osu!catch)."""
        return ctypes.Structure.__set__(self, "n300", value)

    @property
    def n100(self) -> int:
        """ Amount of current 100s (droplets for osu!catch)."""
        return ctypes.Structure.__get__(self, "n100")

    @n100.setter
    def n100(self, value: int):
        """ Amount of current 100s (droplets for osu!catch)."""
        return ctypes.Structure.__set__(self, "n100", value)

    @property
    def n50(self) -> int:
        """ Amount of current 50s (tiny droplets for osu!catch)."""
        return ctypes.Structure.__get__(self, "n50")

    @n50.setter
    def n50(self, value: int):
        """ Amount of current 50s (tiny droplets for osu!catch)."""
        return ctypes.Structure.__set__(self, "n50", value)

    @property
    def misses(self) -> int:
        """ Amount of current misses (fruits + droplets for osu!catch)."""
        return ctypes.Structure.__get__(self, "misses")

    @misses.setter
    def misses(self, value: int):
        """ Amount of current misses (fruits + droplets for osu!catch)."""
        return ctypes.Structure.__set__(self, "misses", value)


class TaikoDifficultyAttributes(ctypes.Structure):
    """ The result of a difficulty calculation on an osu!taiko map."""

    # These fields represent the underlying C data layout
    _fields_ = [
        ("stamina", ctypes.c_double),
        ("rhythm", ctypes.c_double),
        ("color", ctypes.c_double),
        ("reading", ctypes.c_double),
        ("great_hit_window", ctypes.c_double),
        ("ok_hit_window", ctypes.c_double),
        ("mono_stamina_factor", ctypes.c_double),
        ("stars", ctypes.c_double),
        ("max_combo", ctypes.c_uint32),
        ("is_convert", ctypes.c_bool),
    ]

    def __init__(self, stamina: float = None, rhythm: float = None, color: float = None, reading: float = None, great_hit_window: float = None, ok_hit_window: float = None, mono_stamina_factor: float = None, stars: float = None, max_combo: int = None, is_convert: bool = None):
        if stamina is not None:
            self.stamina = stamina
        if rhythm is not None:
            self.rhythm = rhythm
        if color is not None:
            self.color = color
        if reading is not None:
            self.reading = reading
        if great_hit_window is not None:
            self.great_hit_window = great_hit_window
        if ok_hit_window is not None:
            self.ok_hit_window = ok_hit_window
        if mono_stamina_factor is not None:
            self.mono_stamina_factor = mono_stamina_factor
        if stars is not None:
            self.stars = stars
        if max_combo is not None:
            self.max_combo = max_combo
        if is_convert is not None:
            self.is_convert = is_convert

    @property
    def stamina(self) -> float:
        """ The difficulty of the stamina skill."""
        return ctypes.Structure.__get__(self, "stamina")

    @stamina.setter
    def stamina(self, value: float):
        """ The difficulty of the stamina skill."""
        return ctypes.Structure.__set__(self, "stamina", value)

    @property
    def rhythm(self) -> float:
        """ The difficulty of the rhythm skill."""
        return ctypes.Structure.__get__(self, "rhythm")

    @rhythm.setter
    def rhythm(self, value: float):
        """ The difficulty of the rhythm skill."""
        return ctypes.Structure.__set__(self, "rhythm", value)

    @property
    def color(self) -> float:
        """ The difficulty of the color skill."""
        return ctypes.Structure.__get__(self, "color")

    @color.setter
    def color(self, value: float):
        """ The difficulty of the color skill."""
        return ctypes.Structure.__set__(self, "color", value)

    @property
    def reading(self) -> float:
        """ The difficulty of the reading skill."""
        return ctypes.Structure.__get__(self, "reading")

    @reading.setter
    def reading(self, value: float):
        """ The difficulty of the reading skill."""
        return ctypes.Structure.__set__(self, "reading", value)

    @property
    def great_hit_window(self) -> float:
        """ The perceived hit window for an n300 inclusive of rate-adjusting mods (DT/HT/etc)"""
        return ctypes.Structure.__get__(self, "great_hit_window")

    @great_hit_window.setter
    def great_hit_window(self, value: float):
        """ The perceived hit window for an n300 inclusive of rate-adjusting mods (DT/HT/etc)"""
        return ctypes.Structure.__set__(self, "great_hit_window", value)

    @property
    def ok_hit_window(self) -> float:
        """ The perceived hit window for an n100 inclusive of rate-adjusting mods (DT/HT/etc)"""
        return ctypes.Structure.__get__(self, "ok_hit_window")

    @ok_hit_window.setter
    def ok_hit_window(self, value: float):
        """ The perceived hit window for an n100 inclusive of rate-adjusting mods (DT/HT/etc)"""
        return ctypes.Structure.__set__(self, "ok_hit_window", value)

    @property
    def mono_stamina_factor(self) -> float:
        """ The ratio of stamina difficulty from mono-color (single color) streams to total
 stamina difficulty."""
        return ctypes.Structure.__get__(self, "mono_stamina_factor")

    @mono_stamina_factor.setter
    def mono_stamina_factor(self, value: float):
        """ The ratio of stamina difficulty from mono-color (single color) streams to total
 stamina difficulty."""
        return ctypes.Structure.__set__(self, "mono_stamina_factor", value)

    @property
    def stars(self) -> float:
        """ The final star rating."""
        return ctypes.Structure.__get__(self, "stars")

    @stars.setter
    def stars(self, value: float):
        """ The final star rating."""
        return ctypes.Structure.__set__(self, "stars", value)

    @property
    def max_combo(self) -> int:
        """ The maximum combo."""
        return ctypes.Structure.__get__(self, "max_combo")

    @max_combo.setter
    def max_combo(self, value: int):
        """ The maximum combo."""
        return ctypes.Structure.__set__(self, "max_combo", value)

    @property
    def is_convert(self) -> bool:
        """ Whether the [`Beatmap`] was a convert i.e. an osu!standard map.

 [`Beatmap`]: crate::model::beatmap::Beatmap"""
        return ctypes.Structure.__get__(self, "is_convert")

    @is_convert.setter
    def is_convert(self, value: bool):
        """ Whether the [`Beatmap`] was a convert i.e. an osu!standard map.

 [`Beatmap`]: crate::model::beatmap::Beatmap"""
        return ctypes.Structure.__set__(self, "is_convert", value)


class SliceU8(ctypes.Structure):
    # These fields represent the underlying C data layout
    _fields_ = [
        ("data", ctypes.POINTER(ctypes.c_uint8)),
        ("len", ctypes.c_uint64),
    ]

    def __len__(self):
        return self.len

    def __getitem__(self, i) -> int:
        if i < 0:
            index = self.len+i
        else:
            index = i

        if index >= self.len:
            raise IndexError("Index out of range")

        return self.data[index]

    def copied(self) -> SliceU8:
        """Returns a shallow, owned copy of the underlying slice.

        The returned object owns the immediate data, but not the targets of any contained
        pointers. In other words, if your struct contains any pointers the returned object
        may only be used as long as these pointers are valid. If the struct did not contain
        any pointers the returned object is valid indefinitely."""
        array = (ctypes.c_uint8 * len(self))()
        ctypes.memmove(array, self.data, len(self) * ctypes.sizeof(ctypes.c_uint8))
        rval = SliceU8(data=ctypes.cast(array, ctypes.POINTER(ctypes.c_uint8)), len=len(self))
        rval.owned = array  # Store array in returned slice to prevent memory deallocation
        return rval

    def __iter__(self) -> typing.Iterable[ctypes.c_uint8]:
        return _Iter(self)

    def iter(self) -> typing.Iterable[ctypes.c_uint8]:
        """Convenience method returning a value iterator."""
        return iter(self)

    def first(self) -> int:
        """Returns the first element of this slice."""
        return self[0]

    def last(self) -> int:
        """Returns the last element of this slice."""
        return self[len(self)-1]

    def bytearray(self):
        """Returns a bytearray with the content of this slice."""
        rval = bytearray(len(self))
        for i in range(len(self)):
            rval[i] = self[i]
        return rval


class OptionF64:
    """Option that contains Some(value) or None."""
    # Element if Some().
# TODO - OMITTED DATA VARIANT - BINDINGS ARE BROKEN
    None = 1


class ResultError:
    """Result that contains value or an error."""
    # Element if err is `Ok`.
# TODO - OMITTED DATA VARIANT - BINDINGS ARE BROKEN
    # Error value.
# TODO - OMITTED DATA VARIANT - BINDINGS ARE BROKEN
    Panic = 2
    Null = 3


class DifficultyAttributes:
# TODO - OMITTED DATA VARIANT - BINDINGS ARE BROKEN
# TODO - OMITTED DATA VARIANT - BINDINGS ARE BROKEN
# TODO - OMITTED DATA VARIANT - BINDINGS ARE BROKEN
# TODO - OMITTED DATA VARIANT - BINDINGS ARE BROKEN


class CatchPerformanceAttributes(ctypes.Structure):
    """ The result of a performance calculation on an osu!catch map."""

    # These fields represent the underlying C data layout
    _fields_ = [
        ("difficulty", CatchDifficultyAttributes),
        ("pp", ctypes.c_double),
    ]

    def __init__(self, difficulty: CatchDifficultyAttributes = None, pp: float = None):
        if difficulty is not None:
            self.difficulty = difficulty
        if pp is not None:
            self.pp = pp

    @property
    def difficulty(self) -> CatchDifficultyAttributes:
        """ The difficulty attributes that were used for the performance calculation"""
        return ctypes.Structure.__get__(self, "difficulty")

    @difficulty.setter
    def difficulty(self, value: CatchDifficultyAttributes):
        """ The difficulty attributes that were used for the performance calculation"""
        return ctypes.Structure.__set__(self, "difficulty", value)

    @property
    def pp(self) -> float:
        """ The final performance points."""
        return ctypes.Structure.__get__(self, "pp")

    @pp.setter
    def pp(self, value: float):
        """ The final performance points."""
        return ctypes.Structure.__set__(self, "pp", value)


class HitObjectData(ctypes.Structure):

    # These fields represent the underlying C data layout
    _fields_ = [
        ("kind", ctypes.c_int),
        ("repeats", ctypes.c_uint32),
        ("expected_dist", TODO),
        ("duration", ctypes.c_double),
    ]

    def __init__(self, kind: TODO = None, repeats: int = None, expected_dist: TODO = None, duration: float = None):
        if kind is not None:
            self.kind = kind
        if repeats is not None:
            self.repeats = repeats
        if expected_dist is not None:
            self.expected_dist = expected_dist
        if duration is not None:
            self.duration = duration

    @property
    def kind(self) -> TODO:
        return ctypes.Structure.__get__(self, "kind")

    @kind.setter
    def kind(self, value: TODO):
        return ctypes.Structure.__set__(self, "kind", value)

    @property
    def repeats(self) -> int:
        return ctypes.Structure.__get__(self, "repeats")

    @repeats.setter
    def repeats(self, value: int):
        return ctypes.Structure.__set__(self, "repeats", value)

    @property
    def expected_dist(self) -> TODO:
        return ctypes.Structure.__get__(self, "expected_dist")

    @expected_dist.setter
    def expected_dist(self, value: TODO):
        return ctypes.Structure.__set__(self, "expected_dist", value)

    @property
    def duration(self) -> float:
        return ctypes.Structure.__get__(self, "duration")

    @duration.setter
    def duration(self, value: float):
        return ctypes.Structure.__set__(self, "duration", value)


class HitWindows(ctypes.Structure):
    """ AR and OD hit windows"""

    # These fields represent the underlying C data layout
    _fields_ = [
        ("ar", ctypes.c_double),
        ("od_great", ctypes.c_double),
        ("od_ok", TODO),
    ]

    def __init__(self, ar: float = None, od_great: float = None, od_ok: TODO = None):
        if ar is not None:
            self.ar = ar
        if od_great is not None:
            self.od_great = od_great
        if od_ok is not None:
            self.od_ok = od_ok

    @property
    def ar(self) -> float:
        """ Hit window for approach rate i.e. `TimePreempt` in milliseconds."""
        return ctypes.Structure.__get__(self, "ar")

    @ar.setter
    def ar(self, value: float):
        """ Hit window for approach rate i.e. `TimePreempt` in milliseconds."""
        return ctypes.Structure.__set__(self, "ar", value)

    @property
    def od_great(self) -> float:
        """ Hit window for overall difficulty i.e. time to hit a 300 ("Great") in milliseconds."""
        return ctypes.Structure.__get__(self, "od_great")

    @od_great.setter
    def od_great(self, value: float):
        """ Hit window for overall difficulty i.e. time to hit a 300 ("Great") in milliseconds."""
        return ctypes.Structure.__set__(self, "od_great", value)

    @property
    def od_ok(self) -> TODO:
        """ Hit window for overall difficulty i.e. time to hit a 100 ("Ok") in milliseconds.

 `None` for osu!mania."""
        return ctypes.Structure.__get__(self, "od_ok")

    @od_ok.setter
    def od_ok(self, value: TODO):
        """ Hit window for overall difficulty i.e. time to hit a 100 ("Ok") in milliseconds.

 `None` for osu!mania."""
        return ctypes.Structure.__set__(self, "od_ok", value)


class ManiaPerformanceAttributes(ctypes.Structure):
    """ The result of a performance calculation on an osu!mania map."""

    # These fields represent the underlying C data layout
    _fields_ = [
        ("difficulty", ManiaDifficultyAttributes),
        ("pp", ctypes.c_double),
        ("pp_difficulty", ctypes.c_double),
    ]

    def __init__(self, difficulty: ManiaDifficultyAttributes = None, pp: float = None, pp_difficulty: float = None):
        if difficulty is not None:
            self.difficulty = difficulty
        if pp is not None:
            self.pp = pp
        if pp_difficulty is not None:
            self.pp_difficulty = pp_difficulty

    @property
    def difficulty(self) -> ManiaDifficultyAttributes:
        """ The difficulty attributes that were used for the performance calculation."""
        return ctypes.Structure.__get__(self, "difficulty")

    @difficulty.setter
    def difficulty(self, value: ManiaDifficultyAttributes):
        """ The difficulty attributes that were used for the performance calculation."""
        return ctypes.Structure.__set__(self, "difficulty", value)

    @property
    def pp(self) -> float:
        """ The final performance points."""
        return ctypes.Structure.__get__(self, "pp")

    @pp.setter
    def pp(self, value: float):
        """ The final performance points."""
        return ctypes.Structure.__set__(self, "pp", value)

    @property
    def pp_difficulty(self) -> float:
        """ The difficulty portion of the final pp."""
        return ctypes.Structure.__get__(self, "pp_difficulty")

    @pp_difficulty.setter
    def pp_difficulty(self, value: float):
        """ The difficulty portion of the final pp."""
        return ctypes.Structure.__set__(self, "pp_difficulty", value)


class OsuPerformanceAttributes(ctypes.Structure):
    """ The result of a performance calculation on an osu!standard map."""

    # These fields represent the underlying C data layout
    _fields_ = [
        ("difficulty", OsuDifficultyAttributes),
        ("pp", ctypes.c_double),
        ("pp_acc", ctypes.c_double),
        ("pp_aim", ctypes.c_double),
        ("pp_flashlight", ctypes.c_double),
        ("pp_speed", ctypes.c_double),
        ("effective_miss_count", ctypes.c_double),
        ("speed_deviation", TODO),
    ]

    def __init__(self, difficulty: OsuDifficultyAttributes = None, pp: float = None, pp_acc: float = None, pp_aim: float = None, pp_flashlight: float = None, pp_speed: float = None, effective_miss_count: float = None, speed_deviation: TODO = None):
        if difficulty is not None:
            self.difficulty = difficulty
        if pp is not None:
            self.pp = pp
        if pp_acc is not None:
            self.pp_acc = pp_acc
        if pp_aim is not None:
            self.pp_aim = pp_aim
        if pp_flashlight is not None:
            self.pp_flashlight = pp_flashlight
        if pp_speed is not None:
            self.pp_speed = pp_speed
        if effective_miss_count is not None:
            self.effective_miss_count = effective_miss_count
        if speed_deviation is not None:
            self.speed_deviation = speed_deviation

    @property
    def difficulty(self) -> OsuDifficultyAttributes:
        """ The difficulty attributes that were used for the performance calculation"""
        return ctypes.Structure.__get__(self, "difficulty")

    @difficulty.setter
    def difficulty(self, value: OsuDifficultyAttributes):
        """ The difficulty attributes that were used for the performance calculation"""
        return ctypes.Structure.__set__(self, "difficulty", value)

    @property
    def pp(self) -> float:
        """ The final performance points."""
        return ctypes.Structure.__get__(self, "pp")

    @pp.setter
    def pp(self, value: float):
        """ The final performance points."""
        return ctypes.Structure.__set__(self, "pp", value)

    @property
    def pp_acc(self) -> float:
        """ The accuracy portion of the final pp."""
        return ctypes.Structure.__get__(self, "pp_acc")

    @pp_acc.setter
    def pp_acc(self, value: float):
        """ The accuracy portion of the final pp."""
        return ctypes.Structure.__set__(self, "pp_acc", value)

    @property
    def pp_aim(self) -> float:
        """ The aim portion of the final pp."""
        return ctypes.Structure.__get__(self, "pp_aim")

    @pp_aim.setter
    def pp_aim(self, value: float):
        """ The aim portion of the final pp."""
        return ctypes.Structure.__set__(self, "pp_aim", value)

    @property
    def pp_flashlight(self) -> float:
        """ The flashlight portion of the final pp."""
        return ctypes.Structure.__get__(self, "pp_flashlight")

    @pp_flashlight.setter
    def pp_flashlight(self, value: float):
        """ The flashlight portion of the final pp."""
        return ctypes.Structure.__set__(self, "pp_flashlight", value)

    @property
    def pp_speed(self) -> float:
        """ The speed portion of the final pp."""
        return ctypes.Structure.__get__(self, "pp_speed")

    @pp_speed.setter
    def pp_speed(self, value: float):
        """ The speed portion of the final pp."""
        return ctypes.Structure.__set__(self, "pp_speed", value)

    @property
    def effective_miss_count(self) -> float:
        """ Misses including an approximated amount of slider breaks"""
        return ctypes.Structure.__get__(self, "effective_miss_count")

    @effective_miss_count.setter
    def effective_miss_count(self, value: float):
        """ Misses including an approximated amount of slider breaks"""
        return ctypes.Structure.__set__(self, "effective_miss_count", value)

    @property
    def speed_deviation(self) -> TODO:
        """ Approximated unstable-rate"""
        return ctypes.Structure.__get__(self, "speed_deviation")

    @speed_deviation.setter
    def speed_deviation(self, value: TODO):
        """ Approximated unstable-rate"""
        return ctypes.Structure.__set__(self, "speed_deviation", value)


class TaikoPerformanceAttributes(ctypes.Structure):
    """ The result of a performance calculation on an osu!taiko map."""

    # These fields represent the underlying C data layout
    _fields_ = [
        ("difficulty", TaikoDifficultyAttributes),
        ("pp", ctypes.c_double),
        ("pp_acc", ctypes.c_double),
        ("pp_difficulty", ctypes.c_double),
        ("effective_miss_count", ctypes.c_double),
        ("estimated_unstable_rate", TODO),
    ]

    def __init__(self, difficulty: TaikoDifficultyAttributes = None, pp: float = None, pp_acc: float = None, pp_difficulty: float = None, effective_miss_count: float = None, estimated_unstable_rate: TODO = None):
        if difficulty is not None:
            self.difficulty = difficulty
        if pp is not None:
            self.pp = pp
        if pp_acc is not None:
            self.pp_acc = pp_acc
        if pp_difficulty is not None:
            self.pp_difficulty = pp_difficulty
        if effective_miss_count is not None:
            self.effective_miss_count = effective_miss_count
        if estimated_unstable_rate is not None:
            self.estimated_unstable_rate = estimated_unstable_rate

    @property
    def difficulty(self) -> TaikoDifficultyAttributes:
        """ The difficulty attributes that were used for the performance calculation"""
        return ctypes.Structure.__get__(self, "difficulty")

    @difficulty.setter
    def difficulty(self, value: TaikoDifficultyAttributes):
        """ The difficulty attributes that were used for the performance calculation"""
        return ctypes.Structure.__set__(self, "difficulty", value)

    @property
    def pp(self) -> float:
        """ The final performance points."""
        return ctypes.Structure.__get__(self, "pp")

    @pp.setter
    def pp(self, value: float):
        """ The final performance points."""
        return ctypes.Structure.__set__(self, "pp", value)

    @property
    def pp_acc(self) -> float:
        """ The accuracy portion of the final pp."""
        return ctypes.Structure.__get__(self, "pp_acc")

    @pp_acc.setter
    def pp_acc(self, value: float):
        """ The accuracy portion of the final pp."""
        return ctypes.Structure.__set__(self, "pp_acc", value)

    @property
    def pp_difficulty(self) -> float:
        """ The strain portion of the final pp."""
        return ctypes.Structure.__get__(self, "pp_difficulty")

    @pp_difficulty.setter
    def pp_difficulty(self, value: float):
        """ The strain portion of the final pp."""
        return ctypes.Structure.__set__(self, "pp_difficulty", value)

    @property
    def effective_miss_count(self) -> float:
        """ Scaled miss count based on total hits."""
        return ctypes.Structure.__get__(self, "effective_miss_count")

    @effective_miss_count.setter
    def effective_miss_count(self, value: float):
        """ Scaled miss count based on total hits."""
        return ctypes.Structure.__set__(self, "effective_miss_count", value)

    @property
    def estimated_unstable_rate(self) -> TODO:
        """ Upper bound on the player's tap deviation."""
        return ctypes.Structure.__get__(self, "estimated_unstable_rate")

    @estimated_unstable_rate.setter
    def estimated_unstable_rate(self, value: TODO):
        """ Upper bound on the player's tap deviation."""
        return ctypes.Structure.__set__(self, "estimated_unstable_rate", value)


class ResultConstPtrBeatmapAttributesBuilderError:
    """Result that contains value or an error."""
    # Element if err is `Ok`.
# TODO - OMITTED DATA VARIANT - BINDINGS ARE BROKEN
    # Error value.
# TODO - OMITTED DATA VARIANT - BINDINGS ARE BROKEN
    Panic = 2
    Null = 3


class ResultConstPtrBeatmapError:
    """Result that contains value or an error."""
    # Element if err is `Ok`.
# TODO - OMITTED DATA VARIANT - BINDINGS ARE BROKEN
    # Error value.
# TODO - OMITTED DATA VARIANT - BINDINGS ARE BROKEN
    Panic = 2
    Null = 3


class ResultConstPtrDifficultyError:
    """Result that contains value or an error."""
    # Element if err is `Ok`.
# TODO - OMITTED DATA VARIANT - BINDINGS ARE BROKEN
    # Error value.
# TODO - OMITTED DATA VARIANT - BINDINGS ARE BROKEN
    Panic = 2
    Null = 3


class ResultConstPtrGradualDifficultyError:
    """Result that contains value or an error."""
    # Element if err is `Ok`.
# TODO - OMITTED DATA VARIANT - BINDINGS ARE BROKEN
    # Error value.
# TODO - OMITTED DATA VARIANT - BINDINGS ARE BROKEN
    Panic = 2
    Null = 3


class ResultConstPtrGradualPerformanceError:
    """Result that contains value or an error."""
    # Element if err is `Ok`.
# TODO - OMITTED DATA VARIANT - BINDINGS ARE BROKEN
    # Error value.
# TODO - OMITTED DATA VARIANT - BINDINGS ARE BROKEN
    Panic = 2
    Null = 3


class ResultConstPtrModsError:
    """Result that contains value or an error."""
    # Element if err is `Ok`.
# TODO - OMITTED DATA VARIANT - BINDINGS ARE BROKEN
    # Error value.
# TODO - OMITTED DATA VARIANT - BINDINGS ARE BROKEN
    Panic = 2
    Null = 3


class ResultConstPtrOwnedStringError:
    """Result that contains value or an error."""
    # Element if err is `Ok`.
# TODO - OMITTED DATA VARIANT - BINDINGS ARE BROKEN
    # Error value.
# TODO - OMITTED DATA VARIANT - BINDINGS ARE BROKEN
    Panic = 2
    Null = 3


class ResultConstPtrPerformanceError:
    """Result that contains value or an error."""
    # Element if err is `Ok`.
# TODO - OMITTED DATA VARIANT - BINDINGS ARE BROKEN
    # Error value.
# TODO - OMITTED DATA VARIANT - BINDINGS ARE BROKEN
    Panic = 2
    Null = 3


class PerformanceAttributes:
# TODO - OMITTED DATA VARIANT - BINDINGS ARE BROKEN
# TODO - OMITTED DATA VARIANT - BINDINGS ARE BROKEN
# TODO - OMITTED DATA VARIANT - BINDINGS ARE BROKEN
# TODO - OMITTED DATA VARIANT - BINDINGS ARE BROKEN


class BeatmapAttributes(ctypes.Structure):
    """ Summary struct for a [`Beatmap`]'s attributes."""

    # These fields represent the underlying C data layout
    _fields_ = [
        ("ar", ctypes.c_double),
        ("od", ctypes.c_double),
        ("cs", ctypes.c_double),
        ("hp", ctypes.c_double),
        ("clock_rate", ctypes.c_double),
        ("hit_windows", HitWindows),
    ]

    def __init__(self, ar: float = None, od: float = None, cs: float = None, hp: float = None, clock_rate: float = None, hit_windows: HitWindows = None):
        if ar is not None:
            self.ar = ar
        if od is not None:
            self.od = od
        if cs is not None:
            self.cs = cs
        if hp is not None:
            self.hp = hp
        if clock_rate is not None:
            self.clock_rate = clock_rate
        if hit_windows is not None:
            self.hit_windows = hit_windows

    @property
    def ar(self) -> float:
        """ The approach rate."""
        return ctypes.Structure.__get__(self, "ar")

    @ar.setter
    def ar(self, value: float):
        """ The approach rate."""
        return ctypes.Structure.__set__(self, "ar", value)

    @property
    def od(self) -> float:
        """ The overall difficulty."""
        return ctypes.Structure.__get__(self, "od")

    @od.setter
    def od(self, value: float):
        """ The overall difficulty."""
        return ctypes.Structure.__set__(self, "od", value)

    @property
    def cs(self) -> float:
        """ The circle size."""
        return ctypes.Structure.__get__(self, "cs")

    @cs.setter
    def cs(self, value: float):
        """ The circle size."""
        return ctypes.Structure.__set__(self, "cs", value)

    @property
    def hp(self) -> float:
        """ The health drain rate"""
        return ctypes.Structure.__get__(self, "hp")

    @hp.setter
    def hp(self, value: float):
        """ The health drain rate"""
        return ctypes.Structure.__set__(self, "hp", value)

    @property
    def clock_rate(self) -> float:
        """ The clock rate with respect to mods."""
        return ctypes.Structure.__get__(self, "clock_rate")

    @clock_rate.setter
    def clock_rate(self, value: float):
        """ The clock rate with respect to mods."""
        return ctypes.Structure.__set__(self, "clock_rate", value)

    @property
    def hit_windows(self) -> HitWindows:
        """ The hit windows for approach rate and overall difficulty."""
        return ctypes.Structure.__get__(self, "hit_windows")

    @hit_windows.setter
    def hit_windows(self, value: HitWindows):
        """ The hit windows for approach rate and overall difficulty."""
        return ctypes.Structure.__set__(self, "hit_windows", value)


class HitObject(ctypes.Structure):

    # These fields represent the underlying C data layout
    _fields_ = [
        ("pos", Pos),
        ("start_time", ctypes.c_double),
        ("data", HitObjectData),
    ]

    def __init__(self, pos: Pos = None, start_time: float = None, data: HitObjectData = None):
        if pos is not None:
            self.pos = pos
        if start_time is not None:
            self.start_time = start_time
        if data is not None:
            self.data = data

    @property
    def pos(self) -> Pos:
        return ctypes.Structure.__get__(self, "pos")

    @pos.setter
    def pos(self, value: Pos):
        return ctypes.Structure.__set__(self, "pos", value)

    @property
    def start_time(self) -> float:
        return ctypes.Structure.__get__(self, "start_time")

    @start_time.setter
    def start_time(self, value: float):
        return ctypes.Structure.__set__(self, "start_time", value)

    @property
    def data(self) -> HitObjectData:
        return ctypes.Structure.__get__(self, "data")

    @data.setter
    def data(self, value: HitObjectData):
        return ctypes.Structure.__set__(self, "data", value)


class OptionDifficultyAttributes:
    """Option that contains Some(value) or None."""
    # Element if Some().
# TODO - OMITTED DATA VARIANT - BINDINGS ARE BROKEN
    None = 1


class OptionPerformanceAttributes:
    """Option that contains Some(value) or None."""
    # Element if Some().
# TODO - OMITTED DATA VARIANT - BINDINGS ARE BROKEN
    None = 1




class callbacks:
    """Helpers to define callbacks."""


class BeatmapAttributesBuilder:
    __api_lock = object()

    def __init__(self, api_lock, ctx):
        assert(api_lock == BeatmapAttributesBuilder.__api_lock), "You must create this with a static constructor." 
        self._ctx = ctx

    @property
    def _as_parameter_(self):
        return self._ctx

    @staticmethod
    def new() -> BeatmapAttributesBuilder:
        """"""
        ctx = c_lib.beatmap_attributes_new().t
        self = BeatmapAttributesBuilder(BeatmapAttributesBuilder.__api_lock, ctx)
        return self

    def __del__(self):
        c_lib.beatmap_attributes_destroy(self._ctx, )
    def mode(self, mode: TODO):
        """"""
        return c_lib.beatmap_attributes_mode(self._ctx, mode)

    def p_mods(self, mods: ctypes.c_void_p):
        """"""
        return c_lib.beatmap_attributes_p_mods(self._ctx, mods)

    def i_mods(self, mods: int):
        """"""
        return c_lib.beatmap_attributes_i_mods(self._ctx, mods)

    def s_mods(self, str: bytes):
        """"""
        if not hasattr(str, "__ctypes_from_outparam__"):
            str = ctypes.cast(str, ctypes.POINTER(ctypes.c_char))
        return c_lib.beatmap_attributes_s_mods(self._ctx, str)

    def clock_rate(self, clock_rate: float):
        """"""
        return c_lib.beatmap_attributes_clock_rate(self._ctx, clock_rate)

    def ar(self, ar: float):
        """"""
        return c_lib.beatmap_attributes_ar(self._ctx, ar)

    def cs(self, cs: float):
        """"""
        return c_lib.beatmap_attributes_cs(self._ctx, cs)

    def hp(self, hp: float):
        """"""
        return c_lib.beatmap_attributes_hp(self._ctx, hp)

    def od(self, od: float):
        """"""
        return c_lib.beatmap_attributes_od(self._ctx, od)

    def get_clock_rate(self, ) -> float:
        """"""
        return c_lib.beatmap_attributes_get_clock_rate(self._ctx, )

    def build(self, beatmap: ctypes.c_void_p) -> BeatmapAttributes:
        """"""
        return c_lib.beatmap_attributes_build(self._ctx, beatmap)



class Beatmap:
    __api_lock = object()

    def __init__(self, api_lock, ctx):
        assert(api_lock == Beatmap.__api_lock), "You must create this with a static constructor." 
        self._ctx = ctx

    @property
    def _as_parameter_(self):
        return self._ctx

    @staticmethod
    def from_bytes() -> Beatmap:
        """"""
        if hasattr(data, "_length_") and getattr(data, "_type_", "") == ctypes.c_uint8:
            data = SliceU8(data=ctypes.cast(data, ctypes.POINTER(ctypes.c_uint8)), len=len(data))

        ctx = c_lib.beatmap_from_bytes().t
        self = Beatmap(Beatmap.__api_lock, ctx)
        return self

    @staticmethod
    def from_path() -> Beatmap:
        """"""
        if not hasattr(path, "__ctypes_from_outparam__"):
            path = ctypes.cast(path, ctypes.POINTER(ctypes.c_char))
        ctx = c_lib.beatmap_from_path().t
        self = Beatmap(Beatmap.__api_lock, ctx)
        return self

    def __del__(self):
        c_lib.beatmap_destroy(self._ctx, )
    def convert(self, mode: TODO, mods: ctypes.c_void_p) -> bool:
        """ Convert a Beatmap to the specified mode"""
        return c_lib.beatmap_convert(self._ctx, mode, mods)

    def bpm(self, ) -> float:
        """"""
        return c_lib.beatmap_bpm(self._ctx, )

    def total_break_time(self, ) -> float:
        """"""
        return c_lib.beatmap_total_break_time(self._ctx, )

    def version(self, ) -> int:
        """"""
        return c_lib.beatmap_version(self._ctx, )

    def is_convert(self, ) -> bool:
        """"""
        return c_lib.beatmap_is_convert(self._ctx, )

    def stack_leniency(self, ) -> float:
        """"""
        return c_lib.beatmap_stack_leniency(self._ctx, )

    def mode(self, ) -> TODO:
        """"""
        return c_lib.beatmap_mode(self._ctx, )

    def ar(self, ) -> float:
        """"""
        return c_lib.beatmap_ar(self._ctx, )

    def cs(self, ) -> float:
        """"""
        return c_lib.beatmap_cs(self._ctx, )

    def hp(self, ) -> float:
        """"""
        return c_lib.beatmap_hp(self._ctx, )

    def od(self, ) -> float:
        """"""
        return c_lib.beatmap_od(self._ctx, )

    def slider_multiplier(self, ) -> float:
        """"""
        return c_lib.beatmap_slider_multiplier(self._ctx, )

    def slider_tick_rate(self, ) -> float:
        """"""
        return c_lib.beatmap_slider_tick_rate(self._ctx, )

    def hit_objects(self, ):
        """"""
        return c_lib.beatmap_hit_objects(self._ctx, )



class Difficulty:
    __api_lock = object()

    def __init__(self, api_lock, ctx):
        assert(api_lock == Difficulty.__api_lock), "You must create this with a static constructor." 
        self._ctx = ctx

    @property
    def _as_parameter_(self):
        return self._ctx

    @staticmethod
    def new() -> Difficulty:
        """"""
        ctx = c_lib.difficulty_new().t
        self = Difficulty(Difficulty.__api_lock, ctx)
        return self

    def __del__(self):
        c_lib.difficulty_destroy(self._ctx, )
    def p_mods(self, mods: ctypes.c_void_p):
        """"""
        return c_lib.difficulty_p_mods(self._ctx, mods)

    def i_mods(self, mods: int):
        """"""
        return c_lib.difficulty_i_mods(self._ctx, mods)

    def s_mods(self, str: bytes):
        """"""
        if not hasattr(str, "__ctypes_from_outparam__"):
            str = ctypes.cast(str, ctypes.POINTER(ctypes.c_char))
        return c_lib.difficulty_s_mods(self._ctx, str)

    def passed_objects(self, passed_objects: int):
        """"""
        return c_lib.difficulty_passed_objects(self._ctx, passed_objects)

    def clock_rate(self, clock_rate: float):
        """"""
        return c_lib.difficulty_clock_rate(self._ctx, clock_rate)

    def ar(self, ar: float):
        """"""
        return c_lib.difficulty_ar(self._ctx, ar)

    def cs(self, cs: float):
        """"""
        return c_lib.difficulty_cs(self._ctx, cs)

    def hp(self, hp: float):
        """"""
        return c_lib.difficulty_hp(self._ctx, hp)

    def od(self, od: float):
        """"""
        return c_lib.difficulty_od(self._ctx, od)

    def hardrock_offsets(self, hardrock_offsets: bool):
        """"""
        return c_lib.difficulty_hardrock_offsets(self._ctx, hardrock_offsets)

    def lazer(self, lazer: bool):
        """"""
        return c_lib.difficulty_lazer(self._ctx, lazer)

    def calculate(self, beatmap: ctypes.c_void_p) -> TODO:
        """"""
        return c_lib.difficulty_calculate(self._ctx, beatmap)

    def get_clock_rate(self, ) -> float:
        """"""
        return c_lib.difficulty_get_clock_rate(self._ctx, )



class Performance:
    __api_lock = object()

    def __init__(self, api_lock, ctx):
        assert(api_lock == Performance.__api_lock), "You must create this with a static constructor." 
        self._ctx = ctx

    @property
    def _as_parameter_(self):
        return self._ctx

    @staticmethod
    def new() -> Performance:
        """"""
        ctx = c_lib.performance_new().t
        self = Performance(Performance.__api_lock, ctx)
        return self

    def __del__(self):
        c_lib.performance_destroy(self._ctx, )
    def mode(self, mode: TODO):
        """"""
        return c_lib.performance_mode(self._ctx, mode)

    def p_mods(self, mods: ctypes.c_void_p):
        """"""
        return c_lib.performance_p_mods(self._ctx, mods)

    def i_mods(self, mods: int):
        """"""
        return c_lib.performance_i_mods(self._ctx, mods)

    def s_mods(self, str: bytes):
        """"""
        if not hasattr(str, "__ctypes_from_outparam__"):
            str = ctypes.cast(str, ctypes.POINTER(ctypes.c_char))
        return c_lib.performance_s_mods(self._ctx, str)

    def passed_objects(self, passed_objects: int):
        """"""
        return c_lib.performance_passed_objects(self._ctx, passed_objects)

    def clock_rate(self, clock_rate: float):
        """"""
        return c_lib.performance_clock_rate(self._ctx, clock_rate)

    def ar(self, ar: float):
        """"""
        return c_lib.performance_ar(self._ctx, ar)

    def cs(self, cs: float):
        """"""
        return c_lib.performance_cs(self._ctx, cs)

    def hp(self, hp: float):
        """"""
        return c_lib.performance_hp(self._ctx, hp)

    def od(self, od: float):
        """"""
        return c_lib.performance_od(self._ctx, od)

    def hardrock_offsets(self, hardrock_offsets: bool):
        """"""
        return c_lib.performance_hardrock_offsets(self._ctx, hardrock_offsets)

    def state(self, state: ScoreState):
        """"""
        return c_lib.performance_state(self._ctx, state)

    def accuracy(self, accuracy: float):
        """"""
        return c_lib.performance_accuracy(self._ctx, accuracy)

    def misses(self, misses: int):
        """"""
        return c_lib.performance_misses(self._ctx, misses)

    def combo(self, combo: int):
        """"""
        return c_lib.performance_combo(self._ctx, combo)

    def hitresult_priority(self, hitresult_priority: TODO):
        """"""
        return c_lib.performance_hitresult_priority(self._ctx, hitresult_priority)

    def lazer(self, lazer: bool):
        """"""
        return c_lib.performance_lazer(self._ctx, lazer)

    def large_tick_hits(self, large_tick_hits: int):
        """"""
        return c_lib.performance_large_tick_hits(self._ctx, large_tick_hits)

    def small_tick_hits(self, small_tick_hits: int):
        """"""
        return c_lib.performance_small_tick_hits(self._ctx, small_tick_hits)

    def slider_end_hits(self, slider_end_hits: int):
        """"""
        return c_lib.performance_slider_end_hits(self._ctx, slider_end_hits)

    def n300(self, n300: int):
        """"""
        return c_lib.performance_n300(self._ctx, n300)

    def n100(self, n100: int):
        """"""
        return c_lib.performance_n100(self._ctx, n100)

    def n50(self, n50: int):
        """"""
        return c_lib.performance_n50(self._ctx, n50)

    def n_katu(self, n_katu: int):
        """"""
        return c_lib.performance_n_katu(self._ctx, n_katu)

    def n_geki(self, n_geki: int):
        """"""
        return c_lib.performance_n_geki(self._ctx, n_geki)

    def generate_state(self, beatmap: ctypes.c_void_p) -> ScoreState:
        """"""
        return c_lib.performance_generate_state(self._ctx, beatmap)

    def generate_state_from_difficulty(self, difficulty_attr: TODO) -> ScoreState:
        """"""
        return c_lib.performance_generate_state_from_difficulty(self._ctx, difficulty_attr)

    def calculate(self, beatmap: ctypes.c_void_p) -> TODO:
        """"""
        return c_lib.performance_calculate(self._ctx, beatmap)

    def calculate_from_difficulty(self, difficulty_attr: TODO) -> TODO:
        """"""
        return c_lib.performance_calculate_from_difficulty(self._ctx, difficulty_attr)

    def get_clock_rate(self, ) -> float:
        """"""
        return c_lib.performance_get_clock_rate(self._ctx, )



class GradualDifficulty:
    __api_lock = object()

    def __init__(self, api_lock, ctx):
        assert(api_lock == GradualDifficulty.__api_lock), "You must create this with a static constructor." 
        self._ctx = ctx

    @property
    def _as_parameter_(self):
        return self._ctx

    @staticmethod
    def new(beatmap: ctypes.c_void_p) -> GradualDifficulty:
        """ Create a [`GradualDifficulty`] for a map of any mode."""
        ctx = c_lib.gradual_difficulty_new(beatmap).t
        self = GradualDifficulty(GradualDifficulty.__api_lock, ctx)
        return self

    @staticmethod
    def new_with_mode(beatmap: ctypes.c_void_p, mode: TODO) -> GradualDifficulty:
        """ Create a [`GradualDifficulty`] for a [`Beatmap`] on a specific [`GameMode`]."""
        ctx = c_lib.gradual_difficulty_new_with_mode(beatmap, mode).t
        self = GradualDifficulty(GradualDifficulty.__api_lock, ctx)
        return self

    def __del__(self):
        c_lib.gradual_difficulty_destroy(self._ctx, )
    def next(self, ) -> TODO:
        """"""
        return c_lib.gradual_difficulty_next(self._ctx, )

    def nth(self, n: int) -> TODO:
        """"""
        return c_lib.gradual_difficulty_nth(self._ctx, n)

    def len(self, ) -> int:
        """"""
        return c_lib.gradual_difficulty_len(self._ctx, )



class GradualPerformance:
    __api_lock = object()

    def __init__(self, api_lock, ctx):
        assert(api_lock == GradualPerformance.__api_lock), "You must create this with a static constructor." 
        self._ctx = ctx

    @property
    def _as_parameter_(self):
        return self._ctx

    @staticmethod
    def new(beatmap: ctypes.c_void_p) -> GradualPerformance:
        """ Create a [`GradualPerformance`] for a map of any mode."""
        ctx = c_lib.gradual_performance_new(beatmap).t
        self = GradualPerformance(GradualPerformance.__api_lock, ctx)
        return self

    @staticmethod
    def new_with_mode(beatmap: ctypes.c_void_p, mode: TODO) -> GradualPerformance:
        """ Create a [`GradualPerformance`] for a [`Beatmap`] on a specific [`GameMode`]."""
        ctx = c_lib.gradual_performance_new_with_mode(beatmap, mode).t
        self = GradualPerformance(GradualPerformance.__api_lock, ctx)
        return self

    def __del__(self):
        c_lib.gradual_performance_destroy(self._ctx, )
    def next(self, state: ScoreState) -> TODO:
        """ Process the next hit object and calculate the performance attributes
 for the resulting score state."""
        return c_lib.gradual_performance_next(self._ctx, state)

    def last(self, state: ScoreState) -> TODO:
        """ Process all remaining hit objects and calculate the final performance
 attributes."""
        return c_lib.gradual_performance_last(self._ctx, state)

    def nth(self, state: ScoreState, n: int) -> TODO:
        """ Process everything up to the next `n`th hitobject and calculate the
 performance attributes for the resulting score state.

 Note that the count is zero indexed
 `n=1` will process 2, and so on."""
        return c_lib.gradual_performance_nth(self._ctx, state, n)

    def len(self, ) -> int:
        """ Returns the amount of remaining objects."""
        return c_lib.gradual_performance_len(self._ctx, )



class OwnedString:
    __api_lock = object()

    def __init__(self, api_lock, ctx):
        assert(api_lock == OwnedString.__api_lock), "You must create this with a static constructor." 
        self._ctx = ctx

    @property
    def _as_parameter_(self):
        return self._ctx

    @staticmethod
    def from_c_str() -> OwnedString:
        """"""
        if not hasattr(str, "__ctypes_from_outparam__"):
            str = ctypes.cast(str, ctypes.POINTER(ctypes.c_char))
        ctx = c_lib.string_from_c_str().t
        self = OwnedString(OwnedString.__api_lock, ctx)
        return self

    @staticmethod
    def empty() -> OwnedString:
        """"""
        ctx = c_lib.string_empty().t
        self = OwnedString(OwnedString.__api_lock, ctx)
        return self

    def __del__(self):
        c_lib.string_destroy(self._ctx, )
    def is_init(self, ) -> bool:
        """"""
        return c_lib.string_is_init(self._ctx, )

    def to_cstr(self, ) -> bytes:
        """"""
        rval = c_lib.string_to_cstr(self._ctx, )
        return ctypes.string_at(rval)



class Mods:
    __api_lock = object()

    def __init__(self, api_lock, ctx):
        assert(api_lock == Mods.__api_lock), "You must create this with a static constructor." 
        self._ctx = ctx

    @property
    def _as_parameter_(self):
        return self._ctx

    @staticmethod
    def new() -> Mods:
        """"""
        ctx = c_lib.mods_new().t
        self = Mods(Mods.__api_lock, ctx)
        return self

    @staticmethod
    def from_acronyms(mode: TODO) -> Mods:
        """"""
        if not hasattr(str, "__ctypes_from_outparam__"):
            str = ctypes.cast(str, ctypes.POINTER(ctypes.c_char))
        ctx = c_lib.mods_from_acronyms(mode).t
        self = Mods(Mods.__api_lock, ctx)
        return self

    @staticmethod
    def from_bits(mode: TODO) -> Mods:
        """"""
        ctx = c_lib.mods_from_bits(mode).t
        self = Mods(Mods.__api_lock, ctx)
        return self

    @staticmethod
    def from_json(mode: TODO, deny_unknown_fields: bool) -> Mods:
        """"""
        if not hasattr(str, "__ctypes_from_outparam__"):
            str = ctypes.cast(str, ctypes.POINTER(ctypes.c_char))
        ctx = c_lib.mods_from_json(mode, deny_unknown_fields).t
        self = Mods(Mods.__api_lock, ctx)
        return self

    def __del__(self):
        c_lib.mods_destroy(self._ctx, )
    def remove_unknown_mods(self, ):
        """"""
        return c_lib.mods_remove_unknown_mods(self._ctx, )

    def sanitize(self, ):
        """"""
        return c_lib.mods_sanitize(self._ctx, )

    def bits(self, ) -> int:
        """"""
        return c_lib.mods_bits(self._ctx, )

    def len(self, ) -> int:
        """"""
        return c_lib.mods_len(self._ctx, )

    def json(self, str: ctypes.c_void_p):
        """"""
        return c_lib.mods_json(self._ctx, str)

    def insert_json(self, str: bytes, deny_unknown_fields: bool) -> bool:
        """"""
        if not hasattr(str, "__ctypes_from_outparam__"):
            str = ctypes.cast(str, ctypes.POINTER(ctypes.c_char))
        return c_lib.mods_insert_json(self._ctx, str, deny_unknown_fields)

    def insert(self, str: bytes) -> bool:
        """"""
        if not hasattr(str, "__ctypes_from_outparam__"):
            str = ctypes.cast(str, ctypes.POINTER(ctypes.c_char))
        return c_lib.mods_insert(self._ctx, str)

    def contains(self, str: bytes) -> bool:
        """"""
        if not hasattr(str, "__ctypes_from_outparam__"):
            str = ctypes.cast(str, ctypes.POINTER(ctypes.c_char))
        return c_lib.mods_contains(self._ctx, str)

    def clear(self, ):
        """"""
        return c_lib.mods_clear(self._ctx, )

    def clock_rate(self, ) -> TODO:
        """"""
        return c_lib.mods_clock_rate(self._ctx, )



