pub mod attributes;
pub mod hitobjects;
pub mod pos;

use crate::*;
use interoptopus::{
    ffi_service, ffi_service_ctor, ffi_service_method, ffi_type, patterns::{slice::FFISlice, string::AsciiPointer}
};
use mode::Mode;
use mods::Mods;
use rosu_pp::GameMods;

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

    /// Convert a Beatmap to the specified mode
    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn convert(&mut self, mode: Mode, mods: &Mods) -> bool {
        self.inner.convert_mut(mode.into(), &GameMods::from(mods.mods.clone())).is_ok()
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
    pub fn is_convert(&mut self) -> bool {
        self.inner.is_convert
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
}
