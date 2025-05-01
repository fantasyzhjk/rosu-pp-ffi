use crate::*;
use interoptopus::{
    ffi_service, ffi_service_ctor, ffi_service_method, ffi_type, patterns::option::FFIOption
};

use super::{pos::Pos, Beatmap};

#[ffi_type]
#[repr(C)]
#[derive(Copy, Clone, Debug, Hash, PartialEq, Eq, Default)]
pub enum HitObjectKind {
    #[default]
    Circle,
    Slider,
    Spinner,
    Hold,
}

#[ffi_type]
#[repr(C)]
#[derive(Debug, Clone, Default)]
pub struct HitObjectData {
    pub kind: HitObjectKind,
    // for slider
    pub repeats: u32,
    pub expected_dist: FFIOption<f64>,
    // for spinner and hold
    pub duration: f64
}

impl From<&rosu_pp::model::hit_object::HitObjectKind> for HitObjectData {
    fn from(kind: &rosu_pp::model::hit_object::HitObjectKind) -> Self {
        match *kind {
            rosu_pp::model::hit_object::HitObjectKind::Circle => {
                Self {
                    kind: HitObjectKind::Circle,
                    ..Default::default()
                }
            },
            rosu_pp::model::hit_object::HitObjectKind::Slider(rosu_pp::model::hit_object::Slider {
                repeats,
                expected_dist,
                ..
            }) => {
                Self {
                    kind: HitObjectKind::Slider,
                    repeats: repeats as u32,
                    expected_dist: expected_dist.into(),
                    ..Default::default()
                }
            },
            rosu_pp::model::hit_object::HitObjectKind::Spinner(rosu_pp::model::hit_object::Spinner {
                duration,
                ..
            }) => {
                Self {
                    kind: HitObjectKind::Spinner,
                    duration,
                    ..Default::default()
                }
            },
            rosu_pp::model::hit_object::HitObjectKind::Hold(rosu_pp::model::hit_object::HoldNote {
                duration,
                ..
            }) => {
                Self {
                    kind: HitObjectKind::Spinner,
                    duration,
                    ..Default::default()
                }
            },
        }
    }
}



#[ffi_type]
#[repr(C)]
#[derive(Debug, Clone, Default)]
pub struct HitObject {
    pub pos: Pos,
    pub start_time: f64,
    pub data: HitObjectData
}

impl From<&rosu_pp::model::hit_object::HitObject> for HitObject {
    fn from(hit_object: &rosu_pp::model::hit_object::HitObject) -> Self {
        Self {
            pos: hit_object.pos.into(),
            start_time: hit_object.start_time,
            data: HitObjectData::from(&hit_object.kind),
        }
    }
}

#[ffi_type(opaque)]
#[derive(Default)]
pub struct HitObjects<'a> {
    pub inner: &'a [rosu_pp::model::hit_object::HitObject],
    pub index: u32,
    pub len: u32
}

// Regular implementation of methods.
#[ffi_service(error = "FFIError", prefix = "hitobjects_")]
impl<'a> HitObjects<'a> {
    #[ffi_service_ctor]
    pub fn new(beatmap: &'a Beatmap) -> Result<Self, Error> {
        Ok(Self {
            inner: &beatmap.inner.hit_objects,
            index: 0,
            len: beatmap.inner.hit_objects.len() as u32,
        })
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn len(&mut self) -> u32 {
        self.len
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn get(&mut self, index: u32) -> FFIOption<HitObject> {
        if index < self.len {
            FFIOption::some(unsafe { self.get_unchecked(index) })
        } else {
            FFIOption::none()
        }
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn next(&mut self) -> FFIOption<HitObject> {
        if self.index < self.len {
            self.index += 1;
            FFIOption::some(unsafe { self.get_unchecked(self.index - 1) })
        } else {
            FFIOption::none()
        }
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn prev(&mut self) -> FFIOption<HitObject> {
        if self.index > 0 {
            self.index -= 1;
            FFIOption::some(unsafe { self.get_unchecked(self.index) })
        } else {
            FFIOption::none()
        }
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn reset(&mut self) {
        self.index = 0;
    }

    unsafe fn get_unchecked(&mut self, index: u32) -> HitObject {
        self.inner.get_unchecked(index as usize).into()
    }
}

