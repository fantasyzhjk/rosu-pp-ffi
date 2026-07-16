use interoptopus::ffi;

use super::pos::Pos;

#[ffi]
#[derive(Copy, Clone, Debug, Default)]
pub enum ExpectedDistance {
    Some(f64),
    #[default]
    None,
}

impl From<Option<f64>> for ExpectedDistance {
    fn from(value: Option<f64>) -> Self {
        match value {
            Some(value) => Self::Some(value),
            None => Self::None,
        }
    }
}

#[ffi]
#[derive(Copy, Clone, Debug, Default)]
pub struct SliderData {
    pub repeats: u32,
    pub expected_dist: ExpectedDistance,
}

#[ffi]
#[derive(Copy, Clone, Debug, Default)]
pub struct DurationData {
    pub duration: f64,
}

#[ffi]
#[derive(Copy, Clone, Debug)]
pub enum HitObjectData {
    Circle,
    Slider(SliderData),
    Spinner(DurationData),
    Hold(DurationData),
}

impl Default for HitObjectData {
    fn default() -> Self {
        Self::Circle
    }
}

impl From<&rosu_pp::model::hit_object::HitObjectKind> for HitObjectData {
    fn from(kind: &rosu_pp::model::hit_object::HitObjectKind) -> Self {
        match *kind {
            rosu_pp::model::hit_object::HitObjectKind::Circle => Self::Circle,
            rosu_pp::model::hit_object::HitObjectKind::Slider(
                rosu_pp::model::hit_object::Slider {
                    repeats,
                    expected_dist,
                    ..
                },
            ) => Self::Slider(SliderData {
                repeats: repeats as u32,
                expected_dist: expected_dist.into(),
            }),
            rosu_pp::model::hit_object::HitObjectKind::Spinner(
                rosu_pp::model::hit_object::Spinner { duration, .. },
            ) => Self::Spinner(DurationData { duration }),
            rosu_pp::model::hit_object::HitObjectKind::Hold(
                rosu_pp::model::hit_object::HoldNote { duration, .. },
            ) => Self::Hold(DurationData { duration }),
        }
    }
}

#[ffi]
#[derive(Clone, Debug, Default)]
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
