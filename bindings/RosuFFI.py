from __future__ import annotations
import ctypes
import typing

T = typing.TypeVar("T")
c_lib = None

def init_lib(path):
    """Initializes the native library. Must be called at least once before anything else."""
    global c_lib
    c_lib = ctypes.cdll.LoadLibrary(path)

    c_lib.beatmap_attributes_destroy.argtypes = [ctypes.POINTER(ctypes.c_void_p)]
    c_lib.beatmap_attributes_new.argtypes = [ctypes.POINTER(ctypes.c_void_p)]
    c_lib.beatmap_attributes_mode.argtypes = [ctypes.c_void_p, ctypes.c_int]
    c_lib.beatmap_attributes_p_mods.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
    c_lib.beatmap_attributes_i_mods.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
    c_lib.beatmap_attributes_s_mods.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_char)]
    c_lib.beatmap_attributes_clock_rate.argtypes = [ctypes.c_void_p, ctypes.c_double]
    c_lib.beatmap_attributes_ar.argtypes = [ctypes.c_void_p, ctypes.c_float]
    c_lib.beatmap_attributes_cs.argtypes = [ctypes.c_void_p, ctypes.c_float]
    c_lib.beatmap_attributes_hp.argtypes = [ctypes.c_void_p, ctypes.c_float]
    c_lib.beatmap_attributes_od.argtypes = [ctypes.c_void_p, ctypes.c_float]
    c_lib.beatmap_attributes_get_clock_rate.argtypes = [ctypes.c_void_p]
    c_lib.beatmap_attributes_build.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
    c_lib.beatmap_destroy.argtypes = [ctypes.POINTER(ctypes.c_void_p)]
    c_lib.beatmap_from_bytes.argtypes = [ctypes.POINTER(ctypes.c_void_p), Sliceu8]
    c_lib.beatmap_from_path.argtypes = [ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(ctypes.c_char)]
    c_lib.beatmap_convert.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p]
    c_lib.beatmap_bpm.argtypes = [ctypes.c_void_p]
    c_lib.beatmap_total_break_time.argtypes = [ctypes.c_void_p]
    c_lib.beatmap_version.argtypes = [ctypes.c_void_p]
    c_lib.beatmap_is_convert.argtypes = [ctypes.c_void_p]
    c_lib.beatmap_stack_leniency.argtypes = [ctypes.c_void_p]
    c_lib.beatmap_mode.argtypes = [ctypes.c_void_p]
    c_lib.beatmap_ar.argtypes = [ctypes.c_void_p]
    c_lib.beatmap_cs.argtypes = [ctypes.c_void_p]
    c_lib.beatmap_hp.argtypes = [ctypes.c_void_p]
    c_lib.beatmap_od.argtypes = [ctypes.c_void_p]
    c_lib.beatmap_slider_multiplier.argtypes = [ctypes.c_void_p]
    c_lib.beatmap_slider_tick_rate.argtypes = [ctypes.c_void_p]
    c_lib.hitobjects_destroy.argtypes = [ctypes.POINTER(ctypes.c_void_p)]
    c_lib.hitobjects_new.argtypes = [ctypes.POINTER(ctypes.c_void_p), ctypes.c_void_p]
    c_lib.hitobjects_len.argtypes = [ctypes.c_void_p]
    c_lib.hitobjects_get.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
    c_lib.hitobjects_next.argtypes = [ctypes.c_void_p]
    c_lib.hitobjects_prev.argtypes = [ctypes.c_void_p]
    c_lib.hitobjects_reset.argtypes = [ctypes.c_void_p]
    c_lib.difficulty_destroy.argtypes = [ctypes.POINTER(ctypes.c_void_p)]
    c_lib.difficulty_new.argtypes = [ctypes.POINTER(ctypes.c_void_p)]
    c_lib.difficulty_p_mods.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
    c_lib.difficulty_i_mods.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
    c_lib.difficulty_s_mods.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_char)]
    c_lib.difficulty_passed_objects.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
    c_lib.difficulty_clock_rate.argtypes = [ctypes.c_void_p, ctypes.c_double]
    c_lib.difficulty_ar.argtypes = [ctypes.c_void_p, ctypes.c_float]
    c_lib.difficulty_cs.argtypes = [ctypes.c_void_p, ctypes.c_float]
    c_lib.difficulty_hp.argtypes = [ctypes.c_void_p, ctypes.c_float]
    c_lib.difficulty_od.argtypes = [ctypes.c_void_p, ctypes.c_float]
    c_lib.difficulty_hardrock_offsets.argtypes = [ctypes.c_void_p, ctypes.c_bool]
    c_lib.difficulty_lazer.argtypes = [ctypes.c_void_p, ctypes.c_bool]
    c_lib.difficulty_calculate.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
    c_lib.difficulty_get_clock_rate.argtypes = [ctypes.c_void_p]
    c_lib.performance_destroy.argtypes = [ctypes.POINTER(ctypes.c_void_p)]
    c_lib.performance_new.argtypes = [ctypes.POINTER(ctypes.c_void_p)]
    c_lib.performance_mode.argtypes = [ctypes.c_void_p, ctypes.c_int]
    c_lib.performance_p_mods.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
    c_lib.performance_i_mods.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
    c_lib.performance_s_mods.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_char)]
    c_lib.performance_legacy_total_score.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
    c_lib.performance_passed_objects.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
    c_lib.performance_clock_rate.argtypes = [ctypes.c_void_p, ctypes.c_double]
    c_lib.performance_ar.argtypes = [ctypes.c_void_p, ctypes.c_float]
    c_lib.performance_cs.argtypes = [ctypes.c_void_p, ctypes.c_float]
    c_lib.performance_hp.argtypes = [ctypes.c_void_p, ctypes.c_float]
    c_lib.performance_od.argtypes = [ctypes.c_void_p, ctypes.c_float]
    c_lib.performance_hardrock_offsets.argtypes = [ctypes.c_void_p, ctypes.c_bool]
    c_lib.performance_state.argtypes = [ctypes.c_void_p, ScoreState]
    c_lib.performance_accuracy.argtypes = [ctypes.c_void_p, ctypes.c_double]
    c_lib.performance_misses.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
    c_lib.performance_combo.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
    c_lib.performance_hitresult_priority.argtypes = [ctypes.c_void_p, ctypes.c_int]
    c_lib.performance_lazer.argtypes = [ctypes.c_void_p, ctypes.c_bool]
    c_lib.performance_large_tick_hits.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
    c_lib.performance_small_tick_hits.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
    c_lib.performance_slider_end_hits.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
    c_lib.performance_n300.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
    c_lib.performance_n100.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
    c_lib.performance_n50.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
    c_lib.performance_n_katu.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
    c_lib.performance_n_geki.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
    c_lib.performance_generate_state.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
    c_lib.performance_generate_state_from_difficulty.argtypes = [ctypes.c_void_p, DifficultyAttributes]
    c_lib.performance_calculate.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
    c_lib.performance_calculate_from_difficulty.argtypes = [ctypes.c_void_p, DifficultyAttributes]
    c_lib.performance_get_clock_rate.argtypes = [ctypes.c_void_p]
    c_lib.gradual_difficulty_destroy.argtypes = [ctypes.POINTER(ctypes.c_void_p)]
    c_lib.gradual_difficulty_new.argtypes = [ctypes.POINTER(ctypes.c_void_p), ctypes.c_void_p, ctypes.c_void_p]
    c_lib.gradual_difficulty_new_with_mode.argtypes = [ctypes.POINTER(ctypes.c_void_p), ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]
    c_lib.gradual_difficulty_next.argtypes = [ctypes.c_void_p]
    c_lib.gradual_difficulty_nth.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
    c_lib.gradual_difficulty_len.argtypes = [ctypes.c_void_p]
    c_lib.gradual_performance_destroy.argtypes = [ctypes.POINTER(ctypes.c_void_p)]
    c_lib.gradual_performance_new.argtypes = [ctypes.POINTER(ctypes.c_void_p), ctypes.c_void_p, ctypes.c_void_p]
    c_lib.gradual_performance_new_with_mode.argtypes = [ctypes.POINTER(ctypes.c_void_p), ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]
    c_lib.gradual_performance_next.argtypes = [ctypes.c_void_p, ScoreState]
    c_lib.gradual_performance_last.argtypes = [ctypes.c_void_p, ScoreState]
    c_lib.gradual_performance_nth.argtypes = [ctypes.c_void_p, ScoreState, ctypes.c_uint32]
    c_lib.gradual_performance_len.argtypes = [ctypes.c_void_p]
    c_lib.string_destroy.argtypes = [ctypes.POINTER(ctypes.c_void_p)]
    c_lib.string_from_c_str.argtypes = [ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(ctypes.c_char)]
    c_lib.string_empty.argtypes = [ctypes.POINTER(ctypes.c_void_p)]
    c_lib.string_is_init.argtypes = [ctypes.c_void_p]
    c_lib.string_to_cstr.argtypes = [ctypes.c_void_p]
    c_lib.mods_destroy.argtypes = [ctypes.POINTER(ctypes.c_void_p)]
    c_lib.mods_new.argtypes = [ctypes.POINTER(ctypes.c_void_p), ctypes.c_int]
    c_lib.mods_from_acronyms.argtypes = [ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(ctypes.c_char), ctypes.c_int]
    c_lib.mods_from_bits.argtypes = [ctypes.POINTER(ctypes.c_void_p), ctypes.c_uint32, ctypes.c_int]
    c_lib.mods_from_json.argtypes = [ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(ctypes.c_char), ctypes.c_int, ctypes.c_bool]
    c_lib.mods_remove_unknown_mods.argtypes = [ctypes.c_void_p]
    c_lib.mods_sanitize.argtypes = [ctypes.c_void_p]
    c_lib.mods_bits.argtypes = [ctypes.c_void_p]
    c_lib.mods_len.argtypes = [ctypes.c_void_p]
    c_lib.mods_json.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
    c_lib.mods_insert_json.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_char), ctypes.c_bool]
    c_lib.mods_insert.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_char)]
    c_lib.mods_contains.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_char)]
    c_lib.mods_clear.argtypes = [ctypes.c_void_p]
    c_lib.mods_clock_rate.argtypes = [ctypes.c_void_p]
    c_lib.debug_difficylty_attributes.argtypes = [ctypes.POINTER(DifficultyAttributes), ctypes.c_void_p]
    c_lib.debug_performance_attributes.argtypes = [ctypes.POINTER(PerformanceAttributes), ctypes.c_void_p]
    c_lib.debug_score_state.argtypes = [ctypes.POINTER(ScoreState), ctypes.c_void_p]
    c_lib.calculate_accuacy.argtypes = [ctypes.POINTER(ScoreState), ctypes.POINTER(DifficultyAttributes), ctypes.c_int]

    c_lib.beatmap_attributes_destroy.restype = ctypes.c_int
    c_lib.beatmap_attributes_new.restype = ctypes.c_int
    c_lib.beatmap_attributes_s_mods.restype = ctypes.c_int
    c_lib.beatmap_attributes_get_clock_rate.restype = ctypes.c_double
    c_lib.beatmap_attributes_build.restype = BeatmapAttributes
    c_lib.beatmap_destroy.restype = ctypes.c_int
    c_lib.beatmap_from_bytes.restype = ctypes.c_int
    c_lib.beatmap_from_path.restype = ctypes.c_int
    c_lib.beatmap_convert.restype = ctypes.c_bool
    c_lib.beatmap_bpm.restype = ctypes.c_double
    c_lib.beatmap_total_break_time.restype = ctypes.c_double
    c_lib.beatmap_version.restype = ctypes.c_int32
    c_lib.beatmap_is_convert.restype = ctypes.c_bool
    c_lib.beatmap_stack_leniency.restype = ctypes.c_float
    c_lib.beatmap_mode.restype = ctypes.c_int
    c_lib.beatmap_ar.restype = ctypes.c_float
    c_lib.beatmap_cs.restype = ctypes.c_float
    c_lib.beatmap_hp.restype = ctypes.c_float
    c_lib.beatmap_od.restype = ctypes.c_float
    c_lib.beatmap_slider_multiplier.restype = ctypes.c_double
    c_lib.beatmap_slider_tick_rate.restype = ctypes.c_double
    c_lib.hitobjects_destroy.restype = ctypes.c_int
    c_lib.hitobjects_new.restype = ctypes.c_int
    c_lib.hitobjects_len.restype = ctypes.c_uint32
    c_lib.hitobjects_get.restype = OptionHitObject
    c_lib.hitobjects_next.restype = OptionHitObject
    c_lib.hitobjects_prev.restype = OptionHitObject
    c_lib.difficulty_destroy.restype = ctypes.c_int
    c_lib.difficulty_new.restype = ctypes.c_int
    c_lib.difficulty_s_mods.restype = ctypes.c_int
    c_lib.difficulty_calculate.restype = DifficultyAttributes
    c_lib.difficulty_get_clock_rate.restype = ctypes.c_double
    c_lib.performance_destroy.restype = ctypes.c_int
    c_lib.performance_new.restype = ctypes.c_int
    c_lib.performance_s_mods.restype = ctypes.c_int
    c_lib.performance_generate_state.restype = ScoreState
    c_lib.performance_generate_state_from_difficulty.restype = ScoreState
    c_lib.performance_calculate.restype = PerformanceAttributes
    c_lib.performance_calculate_from_difficulty.restype = PerformanceAttributes
    c_lib.performance_get_clock_rate.restype = ctypes.c_double
    c_lib.gradual_difficulty_destroy.restype = ctypes.c_int
    c_lib.gradual_difficulty_new.restype = ctypes.c_int
    c_lib.gradual_difficulty_new_with_mode.restype = ctypes.c_int
    c_lib.gradual_difficulty_next.restype = OptionDifficultyAttributes
    c_lib.gradual_difficulty_nth.restype = OptionDifficultyAttributes
    c_lib.gradual_difficulty_len.restype = ctypes.c_uint32
    c_lib.gradual_performance_destroy.restype = ctypes.c_int
    c_lib.gradual_performance_new.restype = ctypes.c_int
    c_lib.gradual_performance_new_with_mode.restype = ctypes.c_int
    c_lib.gradual_performance_next.restype = OptionPerformanceAttributes
    c_lib.gradual_performance_last.restype = OptionPerformanceAttributes
    c_lib.gradual_performance_nth.restype = OptionPerformanceAttributes
    c_lib.gradual_performance_len.restype = ctypes.c_uint32
    c_lib.string_destroy.restype = ctypes.c_int
    c_lib.string_from_c_str.restype = ctypes.c_int
    c_lib.string_empty.restype = ctypes.c_int
    c_lib.string_is_init.restype = ctypes.c_bool
    c_lib.string_to_cstr.restype = ctypes.POINTER(ctypes.c_char)
    c_lib.mods_destroy.restype = ctypes.c_int
    c_lib.mods_new.restype = ctypes.c_int
    c_lib.mods_from_acronyms.restype = ctypes.c_int
    c_lib.mods_from_bits.restype = ctypes.c_int
    c_lib.mods_from_json.restype = ctypes.c_int
    c_lib.mods_bits.restype = ctypes.c_uint32
    c_lib.mods_len.restype = ctypes.c_uint32
    c_lib.mods_insert_json.restype = ctypes.c_bool
    c_lib.mods_insert.restype = ctypes.c_bool
    c_lib.mods_contains.restype = ctypes.c_bool
    c_lib.mods_clock_rate.restype = Optionf64
    c_lib.calculate_accuacy.restype = ctypes.c_double

    c_lib.beatmap_attributes_destroy.errcheck = lambda rval, _fptr, _args: _errcheck(rval, 0)
    c_lib.beatmap_attributes_new.errcheck = lambda rval, _fptr, _args: _errcheck(rval, 0)
    c_lib.beatmap_attributes_s_mods.errcheck = lambda rval, _fptr, _args: _errcheck(rval, 0)
    c_lib.beatmap_destroy.errcheck = lambda rval, _fptr, _args: _errcheck(rval, 0)
    c_lib.beatmap_from_bytes.errcheck = lambda rval, _fptr, _args: _errcheck(rval, 0)
    c_lib.beatmap_from_path.errcheck = lambda rval, _fptr, _args: _errcheck(rval, 0)
    c_lib.hitobjects_destroy.errcheck = lambda rval, _fptr, _args: _errcheck(rval, 0)
    c_lib.hitobjects_new.errcheck = lambda rval, _fptr, _args: _errcheck(rval, 0)
    c_lib.difficulty_destroy.errcheck = lambda rval, _fptr, _args: _errcheck(rval, 0)
    c_lib.difficulty_new.errcheck = lambda rval, _fptr, _args: _errcheck(rval, 0)
    c_lib.difficulty_s_mods.errcheck = lambda rval, _fptr, _args: _errcheck(rval, 0)
    c_lib.performance_destroy.errcheck = lambda rval, _fptr, _args: _errcheck(rval, 0)
    c_lib.performance_new.errcheck = lambda rval, _fptr, _args: _errcheck(rval, 0)
    c_lib.performance_s_mods.errcheck = lambda rval, _fptr, _args: _errcheck(rval, 0)
    c_lib.gradual_difficulty_destroy.errcheck = lambda rval, _fptr, _args: _errcheck(rval, 0)
    c_lib.gradual_difficulty_new.errcheck = lambda rval, _fptr, _args: _errcheck(rval, 0)
    c_lib.gradual_difficulty_new_with_mode.errcheck = lambda rval, _fptr, _args: _errcheck(rval, 0)
    c_lib.gradual_performance_destroy.errcheck = lambda rval, _fptr, _args: _errcheck(rval, 0)
    c_lib.gradual_performance_new.errcheck = lambda rval, _fptr, _args: _errcheck(rval, 0)
    c_lib.gradual_performance_new_with_mode.errcheck = lambda rval, _fptr, _args: _errcheck(rval, 0)
    c_lib.string_destroy.errcheck = lambda rval, _fptr, _args: _errcheck(rval, 0)
    c_lib.string_from_c_str.errcheck = lambda rval, _fptr, _args: _errcheck(rval, 0)
    c_lib.string_empty.errcheck = lambda rval, _fptr, _args: _errcheck(rval, 0)
    c_lib.mods_destroy.errcheck = lambda rval, _fptr, _args: _errcheck(rval, 0)
    c_lib.mods_new.errcheck = lambda rval, _fptr, _args: _errcheck(rval, 0)
    c_lib.mods_from_acronyms.errcheck = lambda rval, _fptr, _args: _errcheck(rval, 0)
    c_lib.mods_from_bits.errcheck = lambda rval, _fptr, _args: _errcheck(rval, 0)
    c_lib.mods_from_json.errcheck = lambda rval, _fptr, _args: _errcheck(rval, 0)


def debug_difficylty_attributes(res: ctypes.POINTER(DifficultyAttributes), str: ctypes.c_void_p):
    return c_lib.debug_difficylty_attributes(res, str)

def debug_performance_attributes(res: ctypes.POINTER(PerformanceAttributes), str: ctypes.c_void_p):
    return c_lib.debug_performance_attributes(res, str)

def debug_score_state(res: ctypes.POINTER(ScoreState), str: ctypes.c_void_p):
    return c_lib.debug_score_state(res, str)

def calculate_accuacy(state: ctypes.POINTER(ScoreState), difficulty: ctypes.POINTER(DifficultyAttributes), origin: ctypes.c_int) -> float:
    return c_lib.calculate_accuacy(state, difficulty, origin)





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


class FFIError:
    Ok = 0
    Null = 100
    Panic = 200
    IoError = 300
    Utf8Error = 400
    InvalidString = 500
    SerializeError = 600
    ConvertError = 700
    Unknown = 1000


class CatchDifficultyAttributes(ctypes.Structure):
    """ The result of a difficulty calculation on an osu!catch map."""

    # These fields represent the underlying C data layout
    _fields_ = [
        ("stars", ctypes.c_double),
        ("preempt", ctypes.c_double),
        ("n_fruits", ctypes.c_uint32),
        ("n_droplets", ctypes.c_uint32),
        ("n_tiny_droplets", ctypes.c_uint32),
        ("is_convert", ctypes.c_bool),
    ]

    def __init__(self, stars: float = None, preempt: float = None, n_fruits: int = None, n_droplets: int = None, n_tiny_droplets: int = None, is_convert: bool = None):
        if stars is not None:
            self.stars = stars
        if preempt is not None:
            self.preempt = preempt
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
    def preempt(self) -> float:
        """ Time preempt (AR time window)."""
        return ctypes.Structure.__get__(self, "preempt")

    @preempt.setter
    def preempt(self, value: float):
        """ Time preempt (AR time window)."""
        return ctypes.Structure.__set__(self, "preempt", value)

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
        ("aim_top_weighted_slider_factor", ctypes.c_double),
        ("speed_top_weighted_slider_factor", ctypes.c_double),
        ("speed_note_count", ctypes.c_double),
        ("aim_difficult_strain_count", ctypes.c_double),
        ("speed_difficult_strain_count", ctypes.c_double),
        ("nested_score_per_object", ctypes.c_double),
        ("legacy_score_base_multiplier", ctypes.c_double),
        ("maximum_legacy_combo_score", ctypes.c_double),
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

    def __init__(self, aim: float = None, aim_difficult_slider_count: float = None, speed: float = None, flashlight: float = None, slider_factor: float = None, aim_top_weighted_slider_factor: float = None, speed_top_weighted_slider_factor: float = None, speed_note_count: float = None, aim_difficult_strain_count: float = None, speed_difficult_strain_count: float = None, nested_score_per_object: float = None, legacy_score_base_multiplier: float = None, maximum_legacy_combo_score: float = None, ar: float = None, great_hit_window: float = None, ok_hit_window: float = None, meh_hit_window: float = None, hp: float = None, n_circles: int = None, n_sliders: int = None, n_large_ticks: int = None, n_spinners: int = None, stars: float = None, max_combo: int = None):
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
        if aim_top_weighted_slider_factor is not None:
            self.aim_top_weighted_slider_factor = aim_top_weighted_slider_factor
        if speed_top_weighted_slider_factor is not None:
            self.speed_top_weighted_slider_factor = speed_top_weighted_slider_factor
        if speed_note_count is not None:
            self.speed_note_count = speed_note_count
        if aim_difficult_strain_count is not None:
            self.aim_difficult_strain_count = aim_difficult_strain_count
        if speed_difficult_strain_count is not None:
            self.speed_difficult_strain_count = speed_difficult_strain_count
        if nested_score_per_object is not None:
            self.nested_score_per_object = nested_score_per_object
        if legacy_score_base_multiplier is not None:
            self.legacy_score_base_multiplier = legacy_score_base_multiplier
        if maximum_legacy_combo_score is not None:
            self.maximum_legacy_combo_score = maximum_legacy_combo_score
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
    def aim_top_weighted_slider_factor(self) -> float:
        """ Describes how much of aim's difficult strain count is contributed to by sliders."""
        return ctypes.Structure.__get__(self, "aim_top_weighted_slider_factor")

    @aim_top_weighted_slider_factor.setter
    def aim_top_weighted_slider_factor(self, value: float):
        """ Describes how much of aim's difficult strain count is contributed to by sliders."""
        return ctypes.Structure.__set__(self, "aim_top_weighted_slider_factor", value)

    @property
    def speed_top_weighted_slider_factor(self) -> float:
        """ Describes how much of speed's difficult strain count is contributed to by sliders."""
        return ctypes.Structure.__get__(self, "speed_top_weighted_slider_factor")

    @speed_top_weighted_slider_factor.setter
    def speed_top_weighted_slider_factor(self, value: float):
        """ Describes how much of speed's difficult strain count is contributed to by sliders."""
        return ctypes.Structure.__set__(self, "speed_top_weighted_slider_factor", value)

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
    def nested_score_per_object(self) -> float:
        """ The amount of nested score per object."""
        return ctypes.Structure.__get__(self, "nested_score_per_object")

    @nested_score_per_object.setter
    def nested_score_per_object(self, value: float):
        """ The amount of nested score per object."""
        return ctypes.Structure.__set__(self, "nested_score_per_object", value)

    @property
    def legacy_score_base_multiplier(self) -> float:
        """ The legacy score base multiplier."""
        return ctypes.Structure.__get__(self, "legacy_score_base_multiplier")

    @legacy_score_base_multiplier.setter
    def legacy_score_base_multiplier(self, value: float):
        """ The legacy score base multiplier."""
        return ctypes.Structure.__set__(self, "legacy_score_base_multiplier", value)

    @property
    def maximum_legacy_combo_score(self) -> float:
        """ The maximum legacy combo score."""
        return ctypes.Structure.__get__(self, "maximum_legacy_combo_score")

    @maximum_legacy_combo_score.setter
    def maximum_legacy_combo_score(self, value: float):
        """ The maximum legacy combo score."""
        return ctypes.Structure.__set__(self, "maximum_legacy_combo_score", value)

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
        ("mechanical_difficulty", ctypes.c_double),
        ("consistency_factor", ctypes.c_double),
        ("stars", ctypes.c_double),
        ("max_combo", ctypes.c_uint32),
        ("is_convert", ctypes.c_bool),
    ]

    def __init__(self, stamina: float = None, rhythm: float = None, color: float = None, reading: float = None, great_hit_window: float = None, ok_hit_window: float = None, mono_stamina_factor: float = None, mechanical_difficulty: float = None, consistency_factor: float = None, stars: float = None, max_combo: int = None, is_convert: bool = None):
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
        if mechanical_difficulty is not None:
            self.mechanical_difficulty = mechanical_difficulty
        if consistency_factor is not None:
            self.consistency_factor = consistency_factor
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
    def mechanical_difficulty(self) -> float:
        """ The difficulty corresponding to the mechanical skills."""
        return ctypes.Structure.__get__(self, "mechanical_difficulty")

    @mechanical_difficulty.setter
    def mechanical_difficulty(self, value: float):
        """ The difficulty corresponding to the mechanical skills."""
        return ctypes.Structure.__set__(self, "mechanical_difficulty", value)

    @property
    def consistency_factor(self) -> float:
        """ The factor corresponding to the consistency of a map."""
        return ctypes.Structure.__get__(self, "consistency_factor")

    @consistency_factor.setter
    def consistency_factor(self, value: float):
        """ The factor corresponding to the consistency of a map."""
        return ctypes.Structure.__set__(self, "consistency_factor", value)

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


class Optionf64(ctypes.Structure):
    """May optionally hold a value."""

    _fields_ = [
        ("_t", ctypes.c_double),
        ("_is_some", ctypes.c_uint8),
    ]

    @property
    def value(self) -> ctypes.c_double:
        """Returns the value if it exists, or None."""
        if self._is_some == 1:
            return self._t
        else:
            return None

    def is_some(self) -> bool:
        """Returns true if the value exists."""
        return self._is_some == 1

    def is_none(self) -> bool:
        """Returns true if the value does not exist."""
        return self._is_some != 0


class Optionu32(ctypes.Structure):
    """May optionally hold a value."""

    _fields_ = [
        ("_t", ctypes.c_uint32),
        ("_is_some", ctypes.c_uint8),
    ]

    @property
    def value(self) -> ctypes.c_uint32:
        """Returns the value if it exists, or None."""
        if self._is_some == 1:
            return self._t
        else:
            return None

    def is_some(self) -> bool:
        """Returns true if the value exists."""
        return self._is_some == 1

    def is_none(self) -> bool:
        """Returns true if the value does not exist."""
        return self._is_some != 0


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
        ("expected_dist", Optionf64),
        ("duration", ctypes.c_double),
    ]

    def __init__(self, kind: ctypes.c_int = None, repeats: int = None, expected_dist: Optionf64 = None, duration: float = None):
        if kind is not None:
            self.kind = kind
        if repeats is not None:
            self.repeats = repeats
        if expected_dist is not None:
            self.expected_dist = expected_dist
        if duration is not None:
            self.duration = duration

    @property
    def kind(self) -> ctypes.c_int:
        return ctypes.Structure.__get__(self, "kind")

    @kind.setter
    def kind(self, value: ctypes.c_int):
        return ctypes.Structure.__set__(self, "kind", value)

    @property
    def repeats(self) -> int:
        return ctypes.Structure.__get__(self, "repeats")

    @repeats.setter
    def repeats(self, value: int):
        return ctypes.Structure.__set__(self, "repeats", value)

    @property
    def expected_dist(self) -> Optionf64:
        return ctypes.Structure.__get__(self, "expected_dist")

    @expected_dist.setter
    def expected_dist(self, value: Optionf64):
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
        ("ar", Optionf64),
        ("od_perfect", Optionf64),
        ("od_great", Optionf64),
        ("od_good", Optionf64),
        ("od_ok", Optionf64),
        ("od_meh", Optionf64),
    ]

    def __init__(self, ar: Optionf64 = None, od_perfect: Optionf64 = None, od_great: Optionf64 = None, od_good: Optionf64 = None, od_ok: Optionf64 = None, od_meh: Optionf64 = None):
        if ar is not None:
            self.ar = ar
        if od_perfect is not None:
            self.od_perfect = od_perfect
        if od_great is not None:
            self.od_great = od_great
        if od_good is not None:
            self.od_good = od_good
        if od_ok is not None:
            self.od_ok = od_ok
        if od_meh is not None:
            self.od_meh = od_meh

    @property
    def ar(self) -> Optionf64:
        """ Hit window for approach rate i.e. `TimePreempt` in milliseconds."""
        return ctypes.Structure.__get__(self, "ar")

    @ar.setter
    def ar(self, value: Optionf64):
        """ Hit window for approach rate i.e. `TimePreempt` in milliseconds."""
        return ctypes.Structure.__set__(self, "ar", value)

    @property
    def od_perfect(self) -> Optionf64:
        """ Hit window for overall difficulty i.e. time to hit a "Perfect" in milliseconds."""
        return ctypes.Structure.__get__(self, "od_perfect")

    @od_perfect.setter
    def od_perfect(self, value: Optionf64):
        """ Hit window for overall difficulty i.e. time to hit a "Perfect" in milliseconds."""
        return ctypes.Structure.__set__(self, "od_perfect", value)

    @property
    def od_great(self) -> Optionf64:
        """ Hit window for overall difficulty i.e. time to hit a 300 ("Great") in milliseconds."""
        return ctypes.Structure.__get__(self, "od_great")

    @od_great.setter
    def od_great(self, value: Optionf64):
        """ Hit window for overall difficulty i.e. time to hit a 300 ("Great") in milliseconds."""
        return ctypes.Structure.__set__(self, "od_great", value)

    @property
    def od_good(self) -> Optionf64:
        """ Hit window for overall difficulty i.e. time to hit a "Good" in milliseconds."""
        return ctypes.Structure.__get__(self, "od_good")

    @od_good.setter
    def od_good(self, value: Optionf64):
        """ Hit window for overall difficulty i.e. time to hit a "Good" in milliseconds."""
        return ctypes.Structure.__set__(self, "od_good", value)

    @property
    def od_ok(self) -> Optionf64:
        """ Hit window for overall difficulty i.e. time to hit a 100 ("Ok") in milliseconds."""
        return ctypes.Structure.__get__(self, "od_ok")

    @od_ok.setter
    def od_ok(self, value: Optionf64):
        """ Hit window for overall difficulty i.e. time to hit a 100 ("Ok") in milliseconds."""
        return ctypes.Structure.__set__(self, "od_ok", value)

    @property
    def od_meh(self) -> Optionf64:
        """ Hit window for overall difficulty i.e. time to hit a 50 ("Meh") in milliseconds."""
        return ctypes.Structure.__get__(self, "od_meh")

    @od_meh.setter
    def od_meh(self, value: Optionf64):
        """ Hit window for overall difficulty i.e. time to hit a 50 ("Meh") in milliseconds."""
        return ctypes.Structure.__set__(self, "od_meh", value)


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
        ("speed_deviation", Optionf64),
        ("combo_based_estimated_miss_count", ctypes.c_double),
        ("score_based_estimated_miss_count", Optionf64),
        ("aim_estimated_slider_breaks", ctypes.c_double),
        ("speed_estimated_slider_breaks", ctypes.c_double),
    ]

    def __init__(self, difficulty: OsuDifficultyAttributes = None, pp: float = None, pp_acc: float = None, pp_aim: float = None, pp_flashlight: float = None, pp_speed: float = None, effective_miss_count: float = None, speed_deviation: Optionf64 = None, combo_based_estimated_miss_count: float = None, score_based_estimated_miss_count: Optionf64 = None, aim_estimated_slider_breaks: float = None, speed_estimated_slider_breaks: float = None):
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
        if combo_based_estimated_miss_count is not None:
            self.combo_based_estimated_miss_count = combo_based_estimated_miss_count
        if score_based_estimated_miss_count is not None:
            self.score_based_estimated_miss_count = score_based_estimated_miss_count
        if aim_estimated_slider_breaks is not None:
            self.aim_estimated_slider_breaks = aim_estimated_slider_breaks
        if speed_estimated_slider_breaks is not None:
            self.speed_estimated_slider_breaks = speed_estimated_slider_breaks

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
    def speed_deviation(self) -> Optionf64:
        """ Approximated unstable-rate"""
        return ctypes.Structure.__get__(self, "speed_deviation")

    @speed_deviation.setter
    def speed_deviation(self, value: Optionf64):
        """ Approximated unstable-rate"""
        return ctypes.Structure.__set__(self, "speed_deviation", value)

    @property
    def combo_based_estimated_miss_count(self) -> float:
        return ctypes.Structure.__get__(self, "combo_based_estimated_miss_count")

    @combo_based_estimated_miss_count.setter
    def combo_based_estimated_miss_count(self, value: float):
        return ctypes.Structure.__set__(self, "combo_based_estimated_miss_count", value)

    @property
    def score_based_estimated_miss_count(self) -> Optionf64:
        return ctypes.Structure.__get__(self, "score_based_estimated_miss_count")

    @score_based_estimated_miss_count.setter
    def score_based_estimated_miss_count(self, value: Optionf64):
        return ctypes.Structure.__set__(self, "score_based_estimated_miss_count", value)

    @property
    def aim_estimated_slider_breaks(self) -> float:
        return ctypes.Structure.__get__(self, "aim_estimated_slider_breaks")

    @aim_estimated_slider_breaks.setter
    def aim_estimated_slider_breaks(self, value: float):
        return ctypes.Structure.__set__(self, "aim_estimated_slider_breaks", value)

    @property
    def speed_estimated_slider_breaks(self) -> float:
        return ctypes.Structure.__get__(self, "speed_estimated_slider_breaks")

    @speed_estimated_slider_breaks.setter
    def speed_estimated_slider_breaks(self, value: float):
        return ctypes.Structure.__set__(self, "speed_estimated_slider_breaks", value)


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
        ("legacy_total_score", Optionu32),
    ]

    def __init__(self, max_combo: int = None, osu_large_tick_hits: int = None, osu_small_tick_hits: int = None, slider_end_hits: int = None, n_geki: int = None, n_katu: int = None, n300: int = None, n100: int = None, n50: int = None, misses: int = None, legacy_total_score: Optionu32 = None):
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
        if legacy_total_score is not None:
            self.legacy_total_score = legacy_total_score

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

    @property
    def legacy_total_score(self) -> Optionu32:
        """ Legacy total score.

 Only relevant for osu!standard in stable."""
        return ctypes.Structure.__get__(self, "legacy_total_score")

    @legacy_total_score.setter
    def legacy_total_score(self, value: Optionu32):
        """ Legacy total score.

 Only relevant for osu!standard in stable."""
        return ctypes.Structure.__set__(self, "legacy_total_score", value)


class TaikoPerformanceAttributes(ctypes.Structure):
    """ The result of a performance calculation on an osu!taiko map."""

    # These fields represent the underlying C data layout
    _fields_ = [
        ("difficulty", TaikoDifficultyAttributes),
        ("pp", ctypes.c_double),
        ("pp_acc", ctypes.c_double),
        ("pp_difficulty", ctypes.c_double),
        ("estimated_unstable_rate", Optionf64),
    ]

    def __init__(self, difficulty: TaikoDifficultyAttributes = None, pp: float = None, pp_acc: float = None, pp_difficulty: float = None, estimated_unstable_rate: Optionf64 = None):
        if difficulty is not None:
            self.difficulty = difficulty
        if pp is not None:
            self.pp = pp
        if pp_acc is not None:
            self.pp_acc = pp_acc
        if pp_difficulty is not None:
            self.pp_difficulty = pp_difficulty
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
    def estimated_unstable_rate(self) -> Optionf64:
        """ Upper bound on the player's tap deviation."""
        return ctypes.Structure.__get__(self, "estimated_unstable_rate")

    @estimated_unstable_rate.setter
    def estimated_unstable_rate(self, value: Optionf64):
        """ Upper bound on the player's tap deviation."""
        return ctypes.Structure.__set__(self, "estimated_unstable_rate", value)


class Sliceu8(ctypes.Structure):
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

    def copied(self) -> Sliceu8:
        """Returns a shallow, owned copy of the underlying slice.

        The returned object owns the immediate data, but not the targets of any contained
        pointers. In other words, if your struct contains any pointers the returned object
        may only be used as long as these pointers are valid. If the struct did not contain
        any pointers the returned object is valid indefinitely."""
        array = (ctypes.c_uint8 * len(self))()
        ctypes.memmove(array, self.data, len(self) * ctypes.sizeof(ctypes.c_uint8))
        rval = Sliceu8(data=ctypes.cast(array, ctypes.POINTER(ctypes.c_uint8)), len=len(self))
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


class OptionCatchDifficultyAttributes(ctypes.Structure):
    """May optionally hold a value."""

    _fields_ = [
        ("_t", CatchDifficultyAttributes),
        ("_is_some", ctypes.c_uint8),
    ]

    @property
    def value(self) -> CatchDifficultyAttributes:
        """Returns the value if it exists, or None."""
        if self._is_some == 1:
            return self._t
        else:
            return None

    def is_some(self) -> bool:
        """Returns true if the value exists."""
        return self._is_some == 1

    def is_none(self) -> bool:
        """Returns true if the value does not exist."""
        return self._is_some != 0


class OptionManiaDifficultyAttributes(ctypes.Structure):
    """May optionally hold a value."""

    _fields_ = [
        ("_t", ManiaDifficultyAttributes),
        ("_is_some", ctypes.c_uint8),
    ]

    @property
    def value(self) -> ManiaDifficultyAttributes:
        """Returns the value if it exists, or None."""
        if self._is_some == 1:
            return self._t
        else:
            return None

    def is_some(self) -> bool:
        """Returns true if the value exists."""
        return self._is_some == 1

    def is_none(self) -> bool:
        """Returns true if the value does not exist."""
        return self._is_some != 0


class OptionOsuDifficultyAttributes(ctypes.Structure):
    """May optionally hold a value."""

    _fields_ = [
        ("_t", OsuDifficultyAttributes),
        ("_is_some", ctypes.c_uint8),
    ]

    @property
    def value(self) -> OsuDifficultyAttributes:
        """Returns the value if it exists, or None."""
        if self._is_some == 1:
            return self._t
        else:
            return None

    def is_some(self) -> bool:
        """Returns true if the value exists."""
        return self._is_some == 1

    def is_none(self) -> bool:
        """Returns true if the value does not exist."""
        return self._is_some != 0


class OptionTaikoDifficultyAttributes(ctypes.Structure):
    """May optionally hold a value."""

    _fields_ = [
        ("_t", TaikoDifficultyAttributes),
        ("_is_some", ctypes.c_uint8),
    ]

    @property
    def value(self) -> TaikoDifficultyAttributes:
        """Returns the value if it exists, or None."""
        if self._is_some == 1:
            return self._t
        else:
            return None

    def is_some(self) -> bool:
        """Returns true if the value exists."""
        return self._is_some == 1

    def is_none(self) -> bool:
        """Returns true if the value does not exist."""
        return self._is_some != 0


class BeatmapAttributes(ctypes.Structure):
    """ Summary struct for a [`Beatmap`]'s attributes."""

    # These fields represent the underlying C data layout
    _fields_ = [
        ("ar", ctypes.c_double),
        ("od", ctypes.c_double),
        ("cs", ctypes.c_float),
        ("hp", ctypes.c_float),
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


class DifficultyAttributes(ctypes.Structure):

    # These fields represent the underlying C data layout
    _fields_ = [
        ("osu", OptionOsuDifficultyAttributes),
        ("taiko", OptionTaikoDifficultyAttributes),
        ("fruit", OptionCatchDifficultyAttributes),
        ("mania", OptionManiaDifficultyAttributes),
        ("mode", ctypes.c_int),
    ]

    def __init__(self, osu: OptionOsuDifficultyAttributes = None, taiko: OptionTaikoDifficultyAttributes = None, fruit: OptionCatchDifficultyAttributes = None, mania: OptionManiaDifficultyAttributes = None, mode: ctypes.c_int = None):
        if osu is not None:
            self.osu = osu
        if taiko is not None:
            self.taiko = taiko
        if fruit is not None:
            self.fruit = fruit
        if mania is not None:
            self.mania = mania
        if mode is not None:
            self.mode = mode

    @property
    def osu(self) -> OptionOsuDifficultyAttributes:
        return ctypes.Structure.__get__(self, "osu")

    @osu.setter
    def osu(self, value: OptionOsuDifficultyAttributes):
        return ctypes.Structure.__set__(self, "osu", value)

    @property
    def taiko(self) -> OptionTaikoDifficultyAttributes:
        return ctypes.Structure.__get__(self, "taiko")

    @taiko.setter
    def taiko(self, value: OptionTaikoDifficultyAttributes):
        return ctypes.Structure.__set__(self, "taiko", value)

    @property
    def fruit(self) -> OptionCatchDifficultyAttributes:
        return ctypes.Structure.__get__(self, "fruit")

    @fruit.setter
    def fruit(self, value: OptionCatchDifficultyAttributes):
        return ctypes.Structure.__set__(self, "fruit", value)

    @property
    def mania(self) -> OptionManiaDifficultyAttributes:
        return ctypes.Structure.__get__(self, "mania")

    @mania.setter
    def mania(self, value: OptionManiaDifficultyAttributes):
        return ctypes.Structure.__set__(self, "mania", value)

    @property
    def mode(self) -> ctypes.c_int:
        return ctypes.Structure.__get__(self, "mode")

    @mode.setter
    def mode(self, value: ctypes.c_int):
        return ctypes.Structure.__set__(self, "mode", value)


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


class OptionCatchPerformanceAttributes(ctypes.Structure):
    """May optionally hold a value."""

    _fields_ = [
        ("_t", CatchPerformanceAttributes),
        ("_is_some", ctypes.c_uint8),
    ]

    @property
    def value(self) -> CatchPerformanceAttributes:
        """Returns the value if it exists, or None."""
        if self._is_some == 1:
            return self._t
        else:
            return None

    def is_some(self) -> bool:
        """Returns true if the value exists."""
        return self._is_some == 1

    def is_none(self) -> bool:
        """Returns true if the value does not exist."""
        return self._is_some != 0


class OptionManiaPerformanceAttributes(ctypes.Structure):
    """May optionally hold a value."""

    _fields_ = [
        ("_t", ManiaPerformanceAttributes),
        ("_is_some", ctypes.c_uint8),
    ]

    @property
    def value(self) -> ManiaPerformanceAttributes:
        """Returns the value if it exists, or None."""
        if self._is_some == 1:
            return self._t
        else:
            return None

    def is_some(self) -> bool:
        """Returns true if the value exists."""
        return self._is_some == 1

    def is_none(self) -> bool:
        """Returns true if the value does not exist."""
        return self._is_some != 0


class OptionOsuPerformanceAttributes(ctypes.Structure):
    """May optionally hold a value."""

    _fields_ = [
        ("_t", OsuPerformanceAttributes),
        ("_is_some", ctypes.c_uint8),
    ]

    @property
    def value(self) -> OsuPerformanceAttributes:
        """Returns the value if it exists, or None."""
        if self._is_some == 1:
            return self._t
        else:
            return None

    def is_some(self) -> bool:
        """Returns true if the value exists."""
        return self._is_some == 1

    def is_none(self) -> bool:
        """Returns true if the value does not exist."""
        return self._is_some != 0


class OptionTaikoPerformanceAttributes(ctypes.Structure):
    """May optionally hold a value."""

    _fields_ = [
        ("_t", TaikoPerformanceAttributes),
        ("_is_some", ctypes.c_uint8),
    ]

    @property
    def value(self) -> TaikoPerformanceAttributes:
        """Returns the value if it exists, or None."""
        if self._is_some == 1:
            return self._t
        else:
            return None

    def is_some(self) -> bool:
        """Returns true if the value exists."""
        return self._is_some == 1

    def is_none(self) -> bool:
        """Returns true if the value does not exist."""
        return self._is_some != 0


class PerformanceAttributes(ctypes.Structure):

    # These fields represent the underlying C data layout
    _fields_ = [
        ("osu", OptionOsuPerformanceAttributes),
        ("taiko", OptionTaikoPerformanceAttributes),
        ("fruit", OptionCatchPerformanceAttributes),
        ("mania", OptionManiaPerformanceAttributes),
        ("mode", ctypes.c_int),
    ]

    def __init__(self, osu: OptionOsuPerformanceAttributes = None, taiko: OptionTaikoPerformanceAttributes = None, fruit: OptionCatchPerformanceAttributes = None, mania: OptionManiaPerformanceAttributes = None, mode: ctypes.c_int = None):
        if osu is not None:
            self.osu = osu
        if taiko is not None:
            self.taiko = taiko
        if fruit is not None:
            self.fruit = fruit
        if mania is not None:
            self.mania = mania
        if mode is not None:
            self.mode = mode

    @property
    def osu(self) -> OptionOsuPerformanceAttributes:
        return ctypes.Structure.__get__(self, "osu")

    @osu.setter
    def osu(self, value: OptionOsuPerformanceAttributes):
        return ctypes.Structure.__set__(self, "osu", value)

    @property
    def taiko(self) -> OptionTaikoPerformanceAttributes:
        return ctypes.Structure.__get__(self, "taiko")

    @taiko.setter
    def taiko(self, value: OptionTaikoPerformanceAttributes):
        return ctypes.Structure.__set__(self, "taiko", value)

    @property
    def fruit(self) -> OptionCatchPerformanceAttributes:
        return ctypes.Structure.__get__(self, "fruit")

    @fruit.setter
    def fruit(self, value: OptionCatchPerformanceAttributes):
        return ctypes.Structure.__set__(self, "fruit", value)

    @property
    def mania(self) -> OptionManiaPerformanceAttributes:
        return ctypes.Structure.__get__(self, "mania")

    @mania.setter
    def mania(self, value: OptionManiaPerformanceAttributes):
        return ctypes.Structure.__set__(self, "mania", value)

    @property
    def mode(self) -> ctypes.c_int:
        return ctypes.Structure.__get__(self, "mode")

    @mode.setter
    def mode(self, value: ctypes.c_int):
        return ctypes.Structure.__set__(self, "mode", value)


class OptionDifficultyAttributes(ctypes.Structure):
    """May optionally hold a value."""

    _fields_ = [
        ("_t", DifficultyAttributes),
        ("_is_some", ctypes.c_uint8),
    ]

    @property
    def value(self) -> DifficultyAttributes:
        """Returns the value if it exists, or None."""
        if self._is_some == 1:
            return self._t
        else:
            return None

    def is_some(self) -> bool:
        """Returns true if the value exists."""
        return self._is_some == 1

    def is_none(self) -> bool:
        """Returns true if the value does not exist."""
        return self._is_some != 0


class OptionHitObject(ctypes.Structure):
    """May optionally hold a value."""

    _fields_ = [
        ("_t", HitObject),
        ("_is_some", ctypes.c_uint8),
    ]

    @property
    def value(self) -> HitObject:
        """Returns the value if it exists, or None."""
        if self._is_some == 1:
            return self._t
        else:
            return None

    def is_some(self) -> bool:
        """Returns true if the value exists."""
        return self._is_some == 1

    def is_none(self) -> bool:
        """Returns true if the value does not exist."""
        return self._is_some != 0


class OptionPerformanceAttributes(ctypes.Structure):
    """May optionally hold a value."""

    _fields_ = [
        ("_t", PerformanceAttributes),
        ("_is_some", ctypes.c_uint8),
    ]

    @property
    def value(self) -> PerformanceAttributes:
        """Returns the value if it exists, or None."""
        if self._is_some == 1:
            return self._t
        else:
            return None

    def is_some(self) -> bool:
        """Returns true if the value exists."""
        return self._is_some == 1

    def is_none(self) -> bool:
        """Returns true if the value does not exist."""
        return self._is_some != 0




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
        ctx = ctypes.c_void_p()
        c_lib.beatmap_attributes_new(ctx, )
        self = BeatmapAttributesBuilder(BeatmapAttributesBuilder.__api_lock, ctx)
        return self

    def __del__(self):
        c_lib.beatmap_attributes_destroy(self._ctx, )
    def mode(self, mode: ctypes.c_int):
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
    def from_bytes(data: Sliceu8 | ctypes.Array[ctypes.c_uint8]) -> Beatmap:
        """"""
        ctx = ctypes.c_void_p()
        if hasattr(data, "_length_") and getattr(data, "_type_", "") == ctypes.c_uint8:
            data = Sliceu8(data=ctypes.cast(data, ctypes.POINTER(ctypes.c_uint8)), len=len(data))

        c_lib.beatmap_from_bytes(ctx, data)
        self = Beatmap(Beatmap.__api_lock, ctx)
        return self

    @staticmethod
    def from_path(path: bytes) -> Beatmap:
        """"""
        ctx = ctypes.c_void_p()
        if not hasattr(path, "__ctypes_from_outparam__"):
            path = ctypes.cast(path, ctypes.POINTER(ctypes.c_char))
        c_lib.beatmap_from_path(ctx, path)
        self = Beatmap(Beatmap.__api_lock, ctx)
        return self

    def __del__(self):
        c_lib.beatmap_destroy(self._ctx, )
    def convert(self, mode: ctypes.c_int, mods: ctypes.c_void_p) -> bool:
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

    def mode(self, ) -> ctypes.c_int:
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



class HitObjects:
    __api_lock = object()

    def __init__(self, api_lock, ctx):
        assert(api_lock == HitObjects.__api_lock), "You must create this with a static constructor." 
        self._ctx = ctx

    @property
    def _as_parameter_(self):
        return self._ctx

    @staticmethod
    def new(beatmap: ctypes.c_void_p) -> HitObjects:
        """"""
        ctx = ctypes.c_void_p()
        c_lib.hitobjects_new(ctx, beatmap)
        self = HitObjects(HitObjects.__api_lock, ctx)
        return self

    def __del__(self):
        c_lib.hitobjects_destroy(self._ctx, )
    def len(self, ) -> int:
        """"""
        return c_lib.hitobjects_len(self._ctx, )

    def get(self, index: int) -> OptionHitObject:
        """"""
        return c_lib.hitobjects_get(self._ctx, index)

    def next(self, ) -> OptionHitObject:
        """"""
        return c_lib.hitobjects_next(self._ctx, )

    def prev(self, ) -> OptionHitObject:
        """"""
        return c_lib.hitobjects_prev(self._ctx, )

    def reset(self, ):
        """"""
        return c_lib.hitobjects_reset(self._ctx, )



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
        ctx = ctypes.c_void_p()
        c_lib.difficulty_new(ctx, )
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

    def calculate(self, beatmap: ctypes.c_void_p) -> DifficultyAttributes:
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
        ctx = ctypes.c_void_p()
        c_lib.performance_new(ctx, )
        self = Performance(Performance.__api_lock, ctx)
        return self

    def __del__(self):
        c_lib.performance_destroy(self._ctx, )
    def mode(self, mode: ctypes.c_int):
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

    def legacy_total_score(self, legacy_total_score: int):
        """"""
        return c_lib.performance_legacy_total_score(self._ctx, legacy_total_score)

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

    def hitresult_priority(self, hitresult_priority: ctypes.c_int):
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

    def generate_state_from_difficulty(self, difficulty_attr: DifficultyAttributes) -> ScoreState:
        """"""
        return c_lib.performance_generate_state_from_difficulty(self._ctx, difficulty_attr)

    def calculate(self, beatmap: ctypes.c_void_p) -> PerformanceAttributes:
        """"""
        return c_lib.performance_calculate(self._ctx, beatmap)

    def calculate_from_difficulty(self, difficulty_attr: DifficultyAttributes) -> PerformanceAttributes:
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
    def new(difficulty: ctypes.c_void_p, beatmap: ctypes.c_void_p) -> GradualDifficulty:
        """ Create a [`GradualDifficulty`] for a map of any mode."""
        ctx = ctypes.c_void_p()
        c_lib.gradual_difficulty_new(ctx, difficulty, beatmap)
        self = GradualDifficulty(GradualDifficulty.__api_lock, ctx)
        return self

    @staticmethod
    def new_with_mode(difficulty: ctypes.c_void_p, beatmap: ctypes.c_void_p, mode: ctypes.c_int) -> GradualDifficulty:
        """ Create a [`GradualDifficulty`] for a [`Beatmap`] on a specific [`GameMode`]."""
        ctx = ctypes.c_void_p()
        c_lib.gradual_difficulty_new_with_mode(ctx, difficulty, beatmap, mode)
        self = GradualDifficulty(GradualDifficulty.__api_lock, ctx)
        return self

    def __del__(self):
        c_lib.gradual_difficulty_destroy(self._ctx, )
    def next(self, ) -> OptionDifficultyAttributes:
        """"""
        return c_lib.gradual_difficulty_next(self._ctx, )

    def nth(self, n: int) -> OptionDifficultyAttributes:
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
    def new(difficulty: ctypes.c_void_p, beatmap: ctypes.c_void_p) -> GradualPerformance:
        """ Create a [`GradualPerformance`] for a map of any mode."""
        ctx = ctypes.c_void_p()
        c_lib.gradual_performance_new(ctx, difficulty, beatmap)
        self = GradualPerformance(GradualPerformance.__api_lock, ctx)
        return self

    @staticmethod
    def new_with_mode(difficulty: ctypes.c_void_p, beatmap: ctypes.c_void_p, mode: ctypes.c_int) -> GradualPerformance:
        """ Create a [`GradualPerformance`] for a [`Beatmap`] on a specific [`GameMode`]."""
        ctx = ctypes.c_void_p()
        c_lib.gradual_performance_new_with_mode(ctx, difficulty, beatmap, mode)
        self = GradualPerformance(GradualPerformance.__api_lock, ctx)
        return self

    def __del__(self):
        c_lib.gradual_performance_destroy(self._ctx, )
    def next(self, state: ScoreState) -> OptionPerformanceAttributes:
        """ Process the next hit object and calculate the performance attributes
 for the resulting score state."""
        return c_lib.gradual_performance_next(self._ctx, state)

    def last(self, state: ScoreState) -> OptionPerformanceAttributes:
        """ Process all remaining hit objects and calculate the final performance
 attributes."""
        return c_lib.gradual_performance_last(self._ctx, state)

    def nth(self, state: ScoreState, n: int) -> OptionPerformanceAttributes:
        """ Process everything up to the next `n`th hitobject and calculate the
 performance attributes for the resulting score state.

 Note that the count is zero-indexed, so `n=0` will process 1 object,
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
    def from_c_str(str: bytes) -> OwnedString:
        """"""
        ctx = ctypes.c_void_p()
        if not hasattr(str, "__ctypes_from_outparam__"):
            str = ctypes.cast(str, ctypes.POINTER(ctypes.c_char))
        c_lib.string_from_c_str(ctx, str)
        self = OwnedString(OwnedString.__api_lock, ctx)
        return self

    @staticmethod
    def empty() -> OwnedString:
        """"""
        ctx = ctypes.c_void_p()
        c_lib.string_empty(ctx, )
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
    def new(mode: ctypes.c_int) -> Mods:
        """"""
        ctx = ctypes.c_void_p()
        c_lib.mods_new(ctx, mode)
        self = Mods(Mods.__api_lock, ctx)
        return self

    @staticmethod
    def from_acronyms(str: bytes, mode: ctypes.c_int) -> Mods:
        """"""
        ctx = ctypes.c_void_p()
        if not hasattr(str, "__ctypes_from_outparam__"):
            str = ctypes.cast(str, ctypes.POINTER(ctypes.c_char))
        c_lib.mods_from_acronyms(ctx, str, mode)
        self = Mods(Mods.__api_lock, ctx)
        return self

    @staticmethod
    def from_bits(bits: int, mode: ctypes.c_int) -> Mods:
        """"""
        ctx = ctypes.c_void_p()
        c_lib.mods_from_bits(ctx, bits, mode)
        self = Mods(Mods.__api_lock, ctx)
        return self

    @staticmethod
    def from_json(str: bytes, mode: ctypes.c_int, deny_unknown_fields: bool) -> Mods:
        """"""
        ctx = ctypes.c_void_p()
        if not hasattr(str, "__ctypes_from_outparam__"):
            str = ctypes.cast(str, ctypes.POINTER(ctypes.c_char))
        c_lib.mods_from_json(ctx, str, mode, deny_unknown_fields)
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

    def clock_rate(self, ) -> Optionf64:
        """"""
        return c_lib.mods_clock_rate(self._ctx, )



