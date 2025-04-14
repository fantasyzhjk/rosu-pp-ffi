use crate::*;
use mode::Mode;
use beatmap::Beatmap;
use difficulty::Difficulty;
use state::ScoreState;
use interoptopus::{
    ffi_service, ffi_service_ctor, ffi_service_method, ffi_type,
    patterns::option::FFIOption,
};


#[ffi_type(opaque)]
#[repr(C)]
#[allow(non_snake_case)]
pub struct GradualDifficulty {
    pub inner: rosu_pp::GradualDifficulty,
}


#[ffi_service(error = "FFIError", prefix = "gradual_difficulty_")]
impl GradualDifficulty {
    /// Create a [`GradualDifficulty`] for a map of any mode.
    #[ffi_service_ctor]
    pub fn new(difficulty: &Difficulty, beatmap: &Beatmap) -> Result<Self, Error> {
        Ok(Self { inner: rosu_pp::GradualDifficulty::new(difficulty.construct(), &beatmap.inner) })
    }

    /// Create a [`GradualDifficulty`] for a [`Beatmap`] on a specific [`GameMode`].
    #[ffi_service_ctor]
    pub fn new_with_mode(difficulty: &Difficulty, beatmap: &Beatmap, mode: Mode) -> Result<Self, Error> {
        Ok(Self { inner: rosu_pp::GradualDifficulty::new_with_mode(difficulty.construct(), &beatmap.inner, mode.into())? })
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn next(&mut self) -> FFIOption<attributes::DifficultyAttributes> {
        self.inner.next().map(attributes::DifficultyAttributes::from).into()
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn nth(&mut self, n: u32) -> FFIOption<attributes::DifficultyAttributes> {
        self.inner.nth(n as usize).map(attributes::DifficultyAttributes::from).into()
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn len(&self) -> u32 {
        self.inner.len() as u32
    }
}


#[ffi_type(opaque)]
#[repr(C)]
#[allow(non_snake_case)]
pub struct GradualPerformance {
    pub inner: rosu_pp::GradualPerformance,
}


#[ffi_service(error = "FFIError", prefix = "gradual_performance_")]
impl GradualPerformance {
    /// Create a [`GradualPerformance`] for a map of any mode.
    #[ffi_service_ctor]
    pub fn new(difficulty: &Difficulty, beatmap: &Beatmap) -> Result<Self, Error> {
        Ok(Self { inner: rosu_pp::GradualPerformance::new(difficulty.construct(), &beatmap.inner) })
    }

    /// Create a [`GradualPerformance`] for a [`Beatmap`] on a specific [`GameMode`].
    #[ffi_service_ctor]
    pub fn new_with_mode(difficulty: &Difficulty, beatmap: &Beatmap, mode: Mode) -> Result<Self, Error> {
        Ok(Self { inner: rosu_pp::GradualPerformance::new_with_mode(difficulty.construct(), &beatmap.inner, mode.into())? })
    }

    /// Process the next hit object and calculate the performance attributes
    /// for the resulting score state.
    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn next(&mut self, state: ScoreState) -> FFIOption<attributes::PerformanceAttributes> {
        self.inner.next(state.into()).map(attributes::PerformanceAttributes::from).into()
    }

    /// Process all remaining hit objects and calculate the final performance
    /// attributes.
    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn last(&mut self, state: ScoreState) -> FFIOption<attributes::PerformanceAttributes> {
        self.inner.last(state.into()).map(attributes::PerformanceAttributes::from).into()
    }

    /// Process everything up to the next `n`th hitobject and calculate the
    /// performance attributes for the resulting score state.
    ///
    /// Note that the count is zero-indexed, so `n=0` will process 1 object,
    /// `n=1` will process 2, and so on.
    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn nth(&mut self, state: ScoreState, n: u32) -> FFIOption<attributes::PerformanceAttributes> {
        self.inner.nth(state.into(), n as usize).map(attributes::PerformanceAttributes::from).into()
    }

    /// Returns the amount of remaining objects.
    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn len(&self) -> u32 {
        self.inner.len() as u32
    }
}

