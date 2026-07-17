pub mod attributes;
pub mod hitobjects;
pub mod pos;
pub mod suspicious;

use crate::{beatmap::suspicious::TooSuspicious, *};
use interoptopus::{
    ffi,
    ffi::{Option as FFIOption, Slice, String as FFIString},
    wire::Wire,
};
use mode::Mode;
use mods::Mods;
use rosu_pp::GameMods;

#[ffi(service)]
#[derive(Default)]
pub struct Beatmap {
    pub inner: rosu_pp::Beatmap,
}

// Regular implementation of methods.
#[ffi(prefix = "beatmap_")]
impl Beatmap {
    pub fn from_bytes(data: Slice<u8>) -> ffi::Result<Self, FFIError> {
        ffi_result(
            rosu_pp::Beatmap::from_bytes(data.as_slice())
                .map(|inner| Self { inner })
                .map_err(Error::from),
        )
    }

    pub fn from_path(path: FFIString) -> ffi::Result<Self, FFIError> {
        ffi_result(
            rosu_pp::Beatmap::from_path(path.as_str())
                .map(|inner| Self { inner })
                .map_err(Error::from),
        )
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
        self.inner.cs
    }

    pub fn hp(&mut self) -> f32 {
        self.inner.hp
    }

    pub fn od(&mut self) -> f32 {
        self.inner.od
    }

    pub fn slider_multiplier(&mut self) -> f64 {
        self.inner.slider_multiplier
    }

    pub fn slider_tick_rate(&mut self) -> f64 {
        self.inner.slider_tick_rate
    }

    pub fn check_suspicious(&mut self) -> FFIOption<TooSuspicious> {
        self.inner
            .check_suspicion()
            .err()
            .map(TooSuspicious::from)
            .into()
    }

    pub fn hit_object_end_time(&self, index: u32) -> FFIOption<f64> {
        self.inner
            .hit_objects
            .get(index as usize)
            .map(|hit_object| {
                let duration = match &hit_object.kind {
                    rosu_pp::model::hit_object::HitObjectKind::Spinner(spinner) => spinner.duration,
                    rosu_pp::model::hit_object::HitObjectKind::Hold(hold) => hold.duration,
                    _ => 0.0,
                };

                hit_object.start_time + duration
            })
            .into()
    }

    /// Return all hit objects as one owned, serialized transfer.
    pub fn hit_objects(&self) -> Wire<Vec<hitobjects::HitObject>> {
        Wire::from(
            self.inner
                .hit_objects
                .iter()
                .map(hitobjects::HitObject::from)
                .collect(),
        )
    }
}
