pub mod attributes;
pub mod hitobject;
pub mod pos;

use crate::*;
use interoptopus::{
    ffi::CStrPtr,
    ffi::Slice as FFISlice,
    ffi_service, ffi_type,
    ffi,
    pattern::result::{result_to_ffi, Result},
    ffi::Vec
};
use mode::Mode;
use mods::Mods;
use rosu_pp::GameMods;
use hitobject::HitObject;

#[ffi_type(opaque)]
#[derive(Default)]
pub struct Beatmap {
    pub inner: rosu_pp::Beatmap,
}

// Regular implementation of methods.
#[ffi_service(prefix = "beatmap_")]
impl Beatmap {
    pub fn from_bytes(data: FFISlice<u8>) -> Result<Self, Error> {
        result_to_ffi(|| {
            Ok(Self {
                inner: rosu_pp::Beatmap::from_bytes(data.as_slice())?,
            })
        })
    }

    pub fn from_path(path: CStrPtr) -> Result<Self, Error> {
        result_to_ffi(|| {
            Ok(Self {
                inner: rosu_pp::Beatmap::from_path(path.as_str()?)?,
            })
        })
    }

    /// Convert a Beatmap to the specified mode
    pub fn convert(&mut self, mode: Mode, mods: &Mods) -> bool {
        self.inner
            .convert_mut(mode.into(), &GameMods::from(mods.mods.clone()))
            .is_ok()
    }

    pub fn bpm(&mut self) -> f64 {
        self.inner.bpm()
    }

    pub fn total_break_time(&mut self) -> f64 {
        self.inner.total_break_time()
    }

    pub fn version(&mut self) -> i32 {
        self.inner.version
    }

    pub fn is_convert(&mut self) -> bool {
        self.inner.is_convert
    }

    // General
    pub fn stack_leniency(&mut self) -> f32 {
        self.inner.stack_leniency
    }

    pub fn mode(&mut self) -> Mode {
        self.inner.mode.into()
    }

    // Difficulty
    pub fn ar(&mut self) -> f32 {
        self.inner.ar
    }

    pub fn cs(&mut self) -> f32 {
        self.inner.ar
    }

    pub fn hp(&mut self) -> f32 {
        self.inner.ar
    }

    pub fn od(&mut self) -> f32 {
        self.inner.ar
    }

    pub fn slider_multiplier(&mut self) -> f64 {
        self.inner.slider_multiplier
    }

    pub fn slider_tick_rate(&mut self) -> f64 {
        self.inner.slider_tick_rate
    }

    pub fn hit_objects(&self) -> Vec<HitObject> {
        Vec::from_vec(std::vec::Vec::from_iter(
            self.inner.hit_objects.iter().map(HitObject::from),
        ))
    }
}
