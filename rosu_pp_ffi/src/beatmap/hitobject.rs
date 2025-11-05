use interoptopus::{
    ffi::Option as FFIOption,
    ffi_type,
};

use super::pos::Pos;

#[ffi_type]
#[derive(Copy, Clone, Debug, Hash, PartialEq, Eq, Default)]
pub enum HitObjectKind {
    #[default]
    Circle,
    Slider,
    Spinner,
    Hold,
}

#[ffi_type]
#[derive(Debug, Clone, Default)]
pub struct HitObjectData {
    pub kind: HitObjectKind,
    // for slider
    pub repeats: u32,
    pub expected_dist: FFIOption<f64>,
    // for spinner and hold
    pub duration: f64,
}

impl From<&rosu_pp::model::hit_object::HitObjectKind> for HitObjectData {
    fn from(kind: &rosu_pp::model::hit_object::HitObjectKind) -> Self {
        match *kind {
            rosu_pp::model::hit_object::HitObjectKind::Circle => Self {
                kind: HitObjectKind::Circle,
                ..Default::default()
            },
            rosu_pp::model::hit_object::HitObjectKind::Slider(
                rosu_pp::model::hit_object::Slider {
                    repeats,
                    expected_dist,
                    ..
                },
            ) => Self {
                kind: HitObjectKind::Slider,
                repeats: repeats as u32,
                expected_dist: expected_dist.into(),
                ..Default::default()
            },
            rosu_pp::model::hit_object::HitObjectKind::Spinner(
                rosu_pp::model::hit_object::Spinner { duration, .. },
            ) => Self {
                kind: HitObjectKind::Spinner,
                duration,
                ..Default::default()
            },
            rosu_pp::model::hit_object::HitObjectKind::Hold(
                rosu_pp::model::hit_object::HoldNote { duration, .. },
            ) => Self {
                kind: HitObjectKind::Hold,
                duration,
                ..Default::default()
            },
        }
    }
}

#[ffi_type]
#[derive(Debug, Clone, Default)]
pub struct HitObject {
    pub pos: Pos,
    pub start_time: f64,
    pub data: HitObjectData,
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
