pub mod attributes;
pub mod too_suspicious;

use crate::*;
use interoptopus::{
    ffi_service, ffi_service_ctor, ffi_service_method, ffi_type, patterns::{option::FFIOption, primitives::FFIBool, slice::FFISlice, string::AsciiPointer}
};
use mode::Mode;
use mods::Mods;
use rosu_pp::GameMods;
use too_suspicious::TooSuspicious;

#[ffi_type(opaque)]
#[derive(Default)]
pub struct Beatmap {
    pub inner: rosu_pp::Beatmap,
}

// Regular implementation of methods.
#[ffi_service(error = "FFIError", prefix = "beatmap_")]
impl Beatmap {
    #[ffi_service_ctor]
    pub fn from_bytes(data: FFISlice<u8>) -> Result<Self, Error> {
        Ok(Self {
            inner: rosu_pp::Beatmap::from_bytes(data.as_slice())?,
        })
    }

    #[ffi_service_ctor]
    pub fn from_path(path: AsciiPointer) -> Result<Self, Error> {
        Ok(Self {
            inner: rosu_pp::Beatmap::from_path(
                path.as_str()?,
            )?,
        })
    }

    #[ffi_service_ctor]
    pub fn from_clone(beatmap: &Beatmap) -> Result<Self, Error> {
        Ok(Self {
            inner: beatmap.inner.clone(),
        })
    }

    /// Convert a Beatmap to the specified mode
    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn convert(&mut self, mode: Mode, mods: &Mods) -> FFIBool {
        self.inner.convert_mut(mode.into(), &GameMods::from(mods.mods.clone())).is_ok().into()
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn bpm(&mut self) -> f64 {
        self.inner.bpm()
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn total_break_time(&mut self) -> f64 {
        self.inner.total_break_time()
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn version(&mut self) -> i32 {
        self.inner.version
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn is_convert(&mut self) -> FFIBool {
        self.inner.is_convert.into()
    }

    // General
    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn stack_leniency(&mut self) -> f32 {
        self.inner.stack_leniency
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn mode(&mut self) -> Mode {
        self.inner.mode.into()
    }

    // Difficulty
    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn ar(&mut self) -> f32 {
        self.inner.ar
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn cs(&mut self) -> f32 {
        self.inner.ar
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn hp(&mut self) -> f32 {
        self.inner.ar
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn od(&mut self) -> f32 {
        self.inner.ar
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn slider_multiplier(&mut self) -> f64 {
        self.inner.slider_multiplier
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn slider_tick_rate(&mut self) -> f64 {
        self.inner.slider_tick_rate
    }

    /// Check whether hitobjects appear too suspicious for further calculation.
    ///
    /// Sometimes a [`Beatmap`] isn't created for gameplay but rather to test
    /// the limits of osu! itself. Difficulty- and/or performance calculation
    /// should likely be avoided on these maps due to potential performance
    /// issues.
    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn check_suspicion(&mut self) -> FFIOption<TooSuspicious> {
        self.inner.check_suspicion().map_err(Into::into).err().into()
    }
}
