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
    c_lib.beatmap_mode.argtypes = [ctypes.c_void_p]
    c_lib.beatmap_is_convert.argtypes = [ctypes.c_void_p]
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
    c_lib.string_destroy.argtypes = [ctypes.POINTER(ctypes.c_void_p)]
    c_lib.string_from_c_str.argtypes = [ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(ctypes.c_char)]
    c_lib.string_empty.argtypes = [ctypes.POINTER(ctypes.c_void_p)]
    c_lib.string_is_init.argtypes = [ctypes.c_void_p]
    c_lib.string_to_cstr.argtypes = [ctypes.c_void_p]
    c_lib.mods_destroy.argtypes = [ctypes.POINTER(ctypes.c_void_p)]
    c_lib.mods_new.argtypes = [ctypes.POINTER(ctypes.c_void_p), ctypes.c_int]
    c_lib.mods_from_acronyms.argtypes = [ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(ctypes.c_char), ctypes.c_int]
    c_lib.mods_from_bits.argtypes = [ctypes.POINTER(ctypes.c_void_p), ctypes.c_uint32, ctypes.c_int]
    c_lib.mods_from_json.argtypes = [ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(ctypes.c_char), ctypes.c_int]
    c_lib.mods_from_json_sanitize.argtypes = [ctypes.POINTER(ctypes.c_void_p), ctypes.POINTER(ctypes.c_char), ctypes.c_int]
    c_lib.mods_remove_incompatible_mods.argtypes = [ctypes.c_void_p]
    c_lib.mods_bits.argtypes = [ctypes.c_void_p]
    c_lib.mods_len.argtypes = [ctypes.c_void_p]
    c_lib.mods_json.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
    c_lib.mods_insert_json.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_char)]
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
    c_lib.beatmap_mode.restype = ctypes.c_int
    c_lib.beatmap_is_convert.restype = ctypes.c_bool
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
    c_lib.mods_from_json_sanitize.restype = ctypes.c_int
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
    c_lib.difficulty_destroy.errcheck = lambda rval, _fptr, _args: _errcheck(rval, 0)
    c_lib.difficulty_new.errcheck = lambda rval, _fptr, _args: _errcheck(rval, 0)
    c_lib.difficulty_s_mods.errcheck = lambda rval, _fptr, _args: _errcheck(rval, 0)
    c_lib.performance_destroy.errcheck = lambda rval, _fptr, _args: _errcheck(rval, 0)
    c_lib.performance_new.errcheck = lambda rval, _fptr, _args: _errcheck(rval, 0)
    c_lib.performance_s_mods.errcheck = lambda rval, _fptr, _args: _errcheck(rval, 0)
    c_lib.string_destroy.errcheck = lambda rval, _fptr, _args: _errcheck(rval, 0)
    c_lib.string_from_c_str.errcheck = lambda rval, _fptr, _args: _errcheck(rval, 0)
    c_lib.string_empty.errcheck = lambda rval, _fptr, _args: _errcheck(rval, 0)
    c_lib.mods_destroy.errcheck = lambda rval, _fptr, _args: _errcheck(rval, 0)
    c_lib.mods_new.errcheck = lambda rval, _fptr, _args: _errcheck(rval, 0)
    c_lib.mods_from_acronyms.errcheck = lambda rval, _fptr, _args: _errcheck(rval, 0)
    c_lib.mods_from_bits.errcheck = lambda rval, _fptr, _args: _errcheck(rval, 0)
    c_lib.mods_from_json.errcheck = lambda rval, _fptr, _args: _errcheck(rval, 0)
    c_lib.mods_from_json_sanitize.errcheck = lambda rval, _fptr, _args: _errcheck(rval, 0)


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
    Unknown = 1000


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
        ("hit_window", ctypes.c_double),
        ("n_objects", ctypes.c_uint32),
        ("n_hold_notes", ctypes.c_uint32),
        ("max_combo", ctypes.c_uint32),
        ("is_convert", ctypes.c_bool),
    ]

    def __init__(self, stars: float = None, hit_window: float = None, n_objects: int = None, n_hold_notes: int = None, max_combo: int = None, is_convert: bool = None):
        if stars is not None:
            self.stars = stars
        if hit_window is not None:
            self.hit_window = hit_window
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
    def hit_window(self) -> float:
        """ The perceived hit window for an n300 inclusive of rate-adjusting mods (DT/HT/etc)."""
        return ctypes.Structure.__get__(self, "hit_window")

    @hit_window.setter
    def hit_window(self, value: float):
        """ The perceived hit window for an n300 inclusive of rate-adjusting mods (DT/HT/etc)."""
        return ctypes.Structure.__set__(self, "hit_window", value)

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
        ("speed", ctypes.c_double),
        ("flashlight", ctypes.c_double),
        ("slider_factor", ctypes.c_double),
        ("speed_note_count", ctypes.c_double),
        ("aim_difficult_strain_count", ctypes.c_double),
        ("speed_difficult_strain_count", ctypes.c_double),
        ("ar", ctypes.c_double),
        ("od", ctypes.c_double),
        ("hp", ctypes.c_double),
        ("n_circles", ctypes.c_uint32),
        ("n_sliders", ctypes.c_uint32),
        ("n_large_ticks", ctypes.c_uint32),
        ("n_spinners", ctypes.c_uint32),
        ("stars", ctypes.c_double),
        ("max_combo", ctypes.c_uint32),
    ]

    def __init__(self, aim: float = None, speed: float = None, flashlight: float = None, slider_factor: float = None, speed_note_count: float = None, aim_difficult_strain_count: float = None, speed_difficult_strain_count: float = None, ar: float = None, od: float = None, hp: float = None, n_circles: int = None, n_sliders: int = None, n_large_ticks: int = None, n_spinners: int = None, stars: float = None, max_combo: int = None):
        if aim is not None:
            self.aim = aim
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
        if od is not None:
            self.od = od
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
    def od(self) -> float:
        """ The overall difficulty"""
        return ctypes.Structure.__get__(self, "od")

    @od.setter
    def od(self, value: float):
        """ The overall difficulty"""
        return ctypes.Structure.__set__(self, "od", value)

    @property
    def hp(self) -> float:
        """ The health drain rate."""
        return ctypes.Structure.__get__(self, "hp")

    @hp.setter
    def hp(self, value: float):
        """ The health drain rate."""
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
        ("peak", ctypes.c_double),
        ("great_hit_window", ctypes.c_double),
        ("ok_hit_window", ctypes.c_double),
        ("mono_stamina_factor", ctypes.c_double),
        ("stars", ctypes.c_double),
        ("max_combo", ctypes.c_uint32),
        ("is_convert", ctypes.c_bool),
    ]

    def __init__(self, stamina: float = None, rhythm: float = None, color: float = None, peak: float = None, great_hit_window: float = None, ok_hit_window: float = None, mono_stamina_factor: float = None, stars: float = None, max_combo: int = None, is_convert: bool = None):
        if stamina is not None:
            self.stamina = stamina
        if rhythm is not None:
            self.rhythm = rhythm
        if color is not None:
            self.color = color
        if peak is not None:
            self.peak = peak
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
    def peak(self) -> float:
        """ The difficulty of the hardest parts of the map."""
        return ctypes.Structure.__get__(self, "peak")

    @peak.setter
    def peak(self, value: float):
        """ The difficulty of the hardest parts of the map."""
        return ctypes.Structure.__set__(self, "peak", value)

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


class HitWindows(ctypes.Structure):
    """ AR and OD hit windows"""

    # These fields represent the underlying C data layout
    _fields_ = [
        ("ar", ctypes.c_double),
        ("od_great", ctypes.c_double),
        ("od_ok", Optionf64),
    ]

    def __init__(self, ar: float = None, od_great: float = None, od_ok: Optionf64 = None):
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
    def od_ok(self) -> Optionf64:
        """ Hit window for overall difficulty i.e. time to hit a 100 ("Ok") in milliseconds.

 `None` for osu!mania."""
        return ctypes.Structure.__get__(self, "od_ok")

    @od_ok.setter
    def od_ok(self, value: Optionf64):
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
    ]

    def __init__(self, difficulty: OsuDifficultyAttributes = None, pp: float = None, pp_acc: float = None, pp_aim: float = None, pp_flashlight: float = None, pp_speed: float = None, effective_miss_count: float = None):
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


class TaikoPerformanceAttributes(ctypes.Structure):
    """ The result of a performance calculation on an osu!taiko map."""

    # These fields represent the underlying C data layout
    _fields_ = [
        ("difficulty", TaikoDifficultyAttributes),
        ("pp", ctypes.c_double),
        ("pp_acc", ctypes.c_double),
        ("pp_difficulty", ctypes.c_double),
        ("effective_miss_count", ctypes.c_double),
        ("estimated_unstable_rate", Optionf64),
    ]

    def __init__(self, difficulty: TaikoDifficultyAttributes = None, pp: float = None, pp_acc: float = None, pp_difficulty: float = None, effective_miss_count: float = None, estimated_unstable_rate: Optionf64 = None):
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

    def mode(self, ) -> ctypes.c_int:
        """"""
        return c_lib.beatmap_mode(self._ctx, )

    def is_convert(self, ) -> bool:
        """"""
        return c_lib.beatmap_is_convert(self._ctx, )



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
    def from_json(str: bytes, mode: ctypes.c_int) -> Mods:
        """"""
        ctx = ctypes.c_void_p()
        if not hasattr(str, "__ctypes_from_outparam__"):
            str = ctypes.cast(str, ctypes.POINTER(ctypes.c_char))
        c_lib.mods_from_json(ctx, str, mode)
        self = Mods(Mods.__api_lock, ctx)
        return self

    @staticmethod
    def from_json_sanitize(str: bytes, mode: ctypes.c_int) -> Mods:
        """"""
        ctx = ctypes.c_void_p()
        if not hasattr(str, "__ctypes_from_outparam__"):
            str = ctypes.cast(str, ctypes.POINTER(ctypes.c_char))
        c_lib.mods_from_json_sanitize(ctx, str, mode)
        self = Mods(Mods.__api_lock, ctx)
        return self

    def __del__(self):
        c_lib.mods_destroy(self._ctx, )
    def remove_incompatible_mods(self, ):
        """"""
        return c_lib.mods_remove_incompatible_mods(self._ctx, )

    def bits(self, ) -> int:
        """"""
        return c_lib.mods_bits(self._ctx, )

    def len(self, ) -> int:
        """"""
        return c_lib.mods_len(self._ctx, )

    def json(self, str: ctypes.c_void_p):
        """"""
        return c_lib.mods_json(self._ctx, str)

    def insert_json(self, str: bytes) -> bool:
        """"""
        if not hasattr(str, "__ctypes_from_outparam__"):
            str = ctypes.cast(str, ctypes.POINTER(ctypes.c_char))
        return c_lib.mods_insert_json(self._ctx, str)

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



