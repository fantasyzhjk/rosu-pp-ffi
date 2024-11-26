pub mod attributes;

use crate::*;
use interoptopus::{
    ffi_service, ffi_service_ctor, ffi_service_method, ffi_type, patterns::{primitives::FFIBool, slice::FFISlice, string::AsciiPointer}
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
                path.as_str().map_err(|_e| Error::InvalidString(None))?,
            )?,
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
    pub fn mode(&mut self) -> Mode {
        self.inner.mode.into()
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn is_convert(&mut self) -> FFIBool {
        self.inner.is_convert.into()
    }
}
