use crate::{ffi_result, mode::Mode, mods::Mods, Error, FFIError};

use interoptopus::{
    ffi,
    ffi::{Option as FFIOption, Slice, String as FFIString},
};
use rosu_mods::{GameMods, GameModsIntermode};

mod attributes;
#[macro_use]
mod r#macro;
mod calculators;

pub use attributes::{LegacyDifficultyAttributes, LegacyPerformanceAttributes};

#[ffi]
#[repr(C)]
#[derive(Copy, Clone, Debug, Default, Hash, PartialEq, Eq)]
pub enum LegacyVersion {
    #[default]
    V2022 = 0,
    Osu2014May = 1,
    Osu2014July = 2,
    Osu2015February = 3,
    Osu2015April = 4,
    Osu2018 = 5,
    Osu2019 = 6,
    Osu2021January = 7,
    Osu2021July = 8,
    Osu2021November = 9,
    Osu2022 = 10,
    Osu2024 = 11,
    Osu2025 = 12,
    TaikoPpv1 = 13,
    Taiko2020 = 14,
    Taiko2022 = 15,
    Taiko2024 = 16,
    Taiko2025 = 17,
    FruitsPpv1 = 18,
    Fruits2022 = 19,
    Fruits2024 = 20,
    ManiaPpv1 = 21,
    Mania2018 = 22,
    Mania2022 = 23,
    RosuPpOlderBase = 24,
}

#[ffi(service)]
#[derive(Default)]
pub struct LegacyBeatmap {
    inner: rosu_pp_older_base::Beatmap,
}

#[ffi(prefix = "legacy_beatmap_")]
impl LegacyBeatmap {
    pub fn from_bytes(data: Slice<u8>) -> ffi::Result<Self, FFIError> {
        ffi_result(
            rosu_pp_older_base::Beatmap::from_bytes(data.as_slice())
                .map(|inner| Self { inner })
                .map_err(Error::from),
        )
    }
}

#[ffi(service)]
pub struct LegacyDifficulty {
    attributes: LegacyDifficultyAttributes,
    mods: u32,
    passed_objects: Option<u32>,
    clock_rate: Option<f64>,
    inner: Option<Box<dyn PreparedDifficulty>>,
}

impl Default for LegacyDifficulty {
    fn default() -> Self {
        Self {
            attributes: LegacyDifficultyAttributes::default(),
            mods: 0,
            passed_objects: None,
            clock_rate: None,
            inner: None,
        }
    }
}

impl LegacyDifficulty {
    fn new(attributes: LegacyDifficultyAttributes, inner: Box<dyn PreparedDifficulty>) -> Self {
        Self {
            attributes,
            mods: 0,
            passed_objects: None,
            clock_rate: None,
            inner: Some(inner),
        }
    }

    fn attributes(&self) -> LegacyDifficultyAttributes {
        self.attributes
    }
}

#[ffi(prefix = "legacy_difficulty_")]
impl LegacyDifficulty {
    pub fn create() -> ffi::Result<Self, FFIError> {
        ffi_result(Ok(Self::default()))
    }

    pub fn set_mode(&mut self, mode: Mode) {
        self.attributes.mode = mode;
    }

    pub fn mods(&mut self, mods: u32) {
        self.mods = mods;
    }

    pub fn passed_objects(&mut self, passed_objects: u32) {
        self.passed_objects = Some(passed_objects);
    }

    pub fn clock_rate(&mut self, clock_rate: f64) {
        self.clock_rate = Some(clock_rate);
    }

    pub fn calculate(
        &mut self,
        beatmap: &LegacyBeatmap,
        version: LegacyVersion,
    ) -> FFIOption<LegacyDifficultyAttributes> {
        let Some(calculator) = calculators::find(version, self.attributes.mode) else {
            return None.into();
        };

        *self = calculator.difficulty(&beatmap.inner, self);

        Some(self.attributes()).into()
    }

    pub fn version(&self) -> LegacyVersion {
        self.attributes.version
    }

    pub fn mode(&self) -> Mode {
        self.attributes.mode
    }

    pub fn stars(&self) -> f64 {
        self.attributes.stars
    }

    pub fn max_combo(&self) -> u32 {
        self.attributes.max_combo
    }
}

#[ffi(service)]
#[derive(Clone, Default, PartialEq)]
#[allow(non_snake_case)]
pub struct LegacyPerformance {
    pub mods: Option<GameMods>,
    pub mods_intermode: Option<GameModsIntermode>,
    pub accuracy: Option<f64>,
    pub score: Option<u32>,
    pub misses: Option<u32>,
    pub combo: Option<u32>,
    pub n300: Option<u32>,
    pub n100: Option<u32>,
    pub n50: Option<u32>,
    pub n_katu: Option<u32>,
    pub n_geki: Option<u32>,
    pub lazer: Option<bool>,
    pub legacy_total_score: Option<u32>,
    pub large_tick_hits: Option<u32>,
    pub small_tick_hits: Option<u32>,
    pub slider_end_hits: Option<u32>,
}

#[ffi(prefix = "legacy_performance_")]
impl LegacyPerformance {
    pub fn create() -> ffi::Result<Self, FFIError> {
        ffi_result(Ok(Self::default()))
    }

    pub fn p_mods(&mut self, mods: &Mods) {
        self.mods = Some(mods.mods.clone());
    }

    pub fn i_mods(&mut self, mods: u32) {
        self.mods_intermode = Some(GameModsIntermode::from_bits(mods));
    }

    pub fn s_mods(&mut self, str: FFIString) {
        self.mods_intermode = Some(GameModsIntermode::from_acronyms(str.as_str()));
    }

    pub fn accuracy(&mut self, accuracy: f64) {
        self.accuracy = Some(accuracy);
    }

    pub fn score(&mut self, score: u32) {
        self.score = Some(score);
    }

    pub fn lazer(&mut self, lazer: bool) {
        self.lazer = Some(lazer);
    }

    pub fn legacy_total_score(&mut self, legacy_total_score: u32) {
        self.legacy_total_score = Some(legacy_total_score);
    }

    pub fn large_tick_hits(&mut self, large_tick_hits: u32) {
        self.large_tick_hits = Some(large_tick_hits);
    }

    pub fn small_tick_hits(&mut self, small_tick_hits: u32) {
        self.small_tick_hits = Some(small_tick_hits);
    }

    pub fn slider_end_hits(&mut self, slider_end_hits: u32) {
        self.slider_end_hits = Some(slider_end_hits);
    }

    pub fn misses(&mut self, misses: u32) {
        self.misses = Some(misses);
    }

    pub fn combo(&mut self, combo: u32) {
        self.combo = Some(combo);
    }

    pub fn n300(&mut self, n300: u32) {
        self.n300 = Some(n300);
    }

    pub fn n100(&mut self, n100: u32) {
        self.n100 = Some(n100);
    }

    pub fn n50(&mut self, n50: u32) {
        self.n50 = Some(n50);
    }

    pub fn n_katu(&mut self, n_katu: u32) {
        self.n_katu = Some(n_katu);
    }

    pub fn n_geki(&mut self, n_geki: u32) {
        self.n_geki = Some(n_geki);
    }

    pub fn calculate(
        &self,
        beatmap: &LegacyBeatmap,
        difficulty: &LegacyDifficulty,
    ) -> ffi::Result<LegacyPerformanceAttributes, FFIError> {
        if difficulty.inner.is_none() {
            return ffi_result(Err(Error::Unknown));
        }

        let Some(calculator) = calculators::find(difficulty.version(), difficulty.mode()) else {
            return ffi_result(Err(Error::Unknown));
        };

        ffi_result(Ok(calculator.performance(&beatmap.inner, difficulty, self)))
    }
}

impl LegacyPerformance {
    /// Derive legacy mod bits from whichever mod representation was set.
    pub fn bits(&self) -> u32 {
        if let Some(mods) = self.mods.as_ref() {
            return mods.bits();
        }

        if let Some(mods_intermode) = self.mods_intermode.as_ref() {
            return mods_intermode.bits();
        }

        0
    }
}

trait LegacyCalculator: Send + Sync {
    fn version(&self) -> LegacyVersion;

    fn mode(&self) -> Mode;

    fn difficulty(
        &self,
        beatmap: &rosu_pp_older_base::Beatmap,
        settings: &LegacyDifficulty,
    ) -> LegacyDifficulty;

    fn performance(
        &self,
        beatmap: &rosu_pp_older_base::Beatmap,
        difficulty: &LegacyDifficulty,
        state: &LegacyPerformance,
    ) -> LegacyPerformanceAttributes {
        let mut result = difficulty
            .inner
            .as_ref()
            .expect("legacy difficulty attributes were not calculated")
            .performance(beatmap, state);
        result.difficulty = difficulty.attributes();
        result
    }
}

trait PreparedDifficulty: Send + Sync {
    fn performance(
        &self,
        beatmap: &rosu_pp_older_base::Beatmap,
        state: &LegacyPerformance,
    ) -> LegacyPerformanceAttributes;
}

struct Prepared<T, F> {
    attributes: T,
    calculate: F,
}

impl<T, F> PreparedDifficulty for Prepared<T, F>
where
    T: Send + Sync,
    F: Fn(&T, &rosu_pp_older_base::Beatmap, &LegacyPerformance) -> LegacyPerformanceAttributes
        + Send
        + Sync,
{
    fn performance(
        &self,
        beatmap: &rosu_pp_older_base::Beatmap,
        state: &LegacyPerformance,
    ) -> LegacyPerformanceAttributes {
        (self.calculate)(&self.attributes, beatmap, state)
    }
}

fn prepare<T, F>(attributes: T, calculate: F) -> Box<dyn PreparedDifficulty>
where
    T: Send + Sync + 'static,
    F: Fn(&T, &rosu_pp_older_base::Beatmap, &LegacyPerformance) -> LegacyPerformanceAttributes
        + Send
        + Sync
        + 'static,
{
    Box::new(Prepared {
        attributes,
        calculate,
    })
}
