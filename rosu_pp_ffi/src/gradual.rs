use crate::*;
use beatmap::Beatmap;
use difficulty::Difficulty;
use interoptopus::{
    ffi_service, ffi_type,
    pattern::option::Option as FFIOption,
    pattern::result::{result_to_ffi, Result},
};
use mode::Mode;
use state::ScoreState;

#[ffi_type(opaque)]
#[allow(non_snake_case)]
pub struct GradualDifficulty {
    pub inner: rosu_pp::GradualDifficulty,
}

#[ffi_service(prefix = "gradual_difficulty_")]
impl GradualDifficulty {
    /// Create a [`GradualDifficulty`] for a map of any mode.
    pub fn new(difficulty: &Difficulty, beatmap: &Beatmap) -> Result<Self, Error> {
        Result::Ok(Self {
            inner: rosu_pp::GradualDifficulty::new(difficulty.construct(), &beatmap.inner),
        })
    }

    /// Create a [`GradualDifficulty`] for a [`Beatmap`] on a specific [`GameMode`].
    pub fn new_with_mode(
        difficulty: &Difficulty,
        beatmap: &Beatmap,
        mode: Mode,
    ) -> Result<Self, Error> {
        result_to_ffi(|| {
            Ok(Self {
                inner: rosu_pp::GradualDifficulty::new_with_mode(
                    difficulty.construct(),
                    &beatmap.inner,
                    mode.into(),
                )?,
            })
        })
    }

    pub fn next(&mut self) -> FFIOption<attributes::DifficultyAttributes> {
        self.inner
            .next()
            .map(attributes::DifficultyAttributes::from)
            .into()
    }

    pub fn nth(&mut self, n: u32) -> FFIOption<attributes::DifficultyAttributes> {
        self.inner
            .nth(n as usize)
            .map(attributes::DifficultyAttributes::from)
            .into()
    }

    pub fn len(&self) -> u32 {
        self.inner.len() as u32
    }
}

#[ffi_type(opaque)]
#[allow(non_snake_case)]
pub struct GradualPerformance {
    pub inner: rosu_pp::GradualPerformance,
}

#[ffi_service(prefix = "gradual_performance_")]
impl GradualPerformance {
    /// Create a [`GradualPerformance`] for a map of any mode.
    pub fn new(difficulty: &Difficulty, beatmap: &Beatmap) -> Result<Self, Error> {
        Result::Ok(Self {
            inner: rosu_pp::GradualPerformance::new(difficulty.construct(), &beatmap.inner),
        })
    }

    /// Create a [`GradualPerformance`] for a [`Beatmap`] on a specific [`GameMode`].
    pub fn new_with_mode(
        difficulty: &Difficulty,
        beatmap: &Beatmap,
        mode: Mode,
    ) -> Result<Self, Error> {
        result_to_ffi(|| {
            Ok(Self {
                inner: rosu_pp::GradualPerformance::new_with_mode(
                    difficulty.construct(),
                    &beatmap.inner,
                    mode.into(),
                )?,
            })
        })
    }

    /// Process the next hit object and calculate the performance attributes
    /// for the resulting score state.
    pub fn next(&mut self, state: ScoreState) -> FFIOption<attributes::PerformanceAttributes> {
        self.inner
            .next(state.into())
            .map(attributes::PerformanceAttributes::from)
            .into()
    }

    /// Process all remaining hit objects and calculate the final performance
    /// attributes.
    pub fn last(&mut self, state: ScoreState) -> FFIOption<attributes::PerformanceAttributes> {
        self.inner
            .last(state.into())
            .map(attributes::PerformanceAttributes::from)
            .into()
    }

    /// Process everything up to the next `n`th hitobject and calculate the
    /// performance attributes for the resulting score state.
    ///
    /// Note that the count is zero indexed
    /// `n=1` will process 2, and so on.
    pub fn nth(
        &mut self,
        state: ScoreState,
        n: u32,
    ) -> FFIOption<attributes::PerformanceAttributes> {
        self.inner
            .nth(state.into(), n as usize)
            .map(attributes::PerformanceAttributes::from)
            .into()
    }

    /// Returns the amount of remaining objects.
    pub fn len(&self) -> u32 {
        self.inner.len() as u32
    }
}
