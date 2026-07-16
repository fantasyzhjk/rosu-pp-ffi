use interoptopus::{ffi, ffi::String as FFIString};

#[ffi]
#[derive(Debug, Clone)]
pub enum DifficultyAttributes {
    Osu(crate::osu::attributes::OsuDifficultyAttributes),
    Taiko(crate::taiko::attributes::TaikoDifficultyAttributes),
    Catch(crate::fruit::attributes::CatchDifficultyAttributes),
    Mania(crate::mania::attributes::ManiaDifficultyAttributes),
}

impl Default for DifficultyAttributes {
    fn default() -> Self {
        Self::Osu(Default::default())
    }
}

impl From<rosu_pp::any::DifficultyAttributes> for DifficultyAttributes {
    fn from(attributes: rosu_pp::any::DifficultyAttributes) -> Self {
        match attributes {
            rosu_pp::any::DifficultyAttributes::Osu(value) => Self::Osu(value.into()),
            rosu_pp::any::DifficultyAttributes::Taiko(value) => Self::Taiko(value.into()),
            rosu_pp::any::DifficultyAttributes::Catch(value) => Self::Catch(value.into()),
            rosu_pp::any::DifficultyAttributes::Mania(value) => Self::Mania(value.into()),
        }
    }
}

impl From<DifficultyAttributes> for rosu_pp::any::DifficultyAttributes {
    fn from(attributes: DifficultyAttributes) -> Self {
        match attributes {
            DifficultyAttributes::Osu(value) => Self::Osu(value.into()),
            DifficultyAttributes::Taiko(value) => Self::Taiko(value.into()),
            DifficultyAttributes::Catch(value) => Self::Catch(value.into()),
            DifficultyAttributes::Mania(value) => Self::Mania(value.into()),
        }
    }
}

#[ffi]
#[derive(Debug, Clone)]
pub enum PerformanceAttributes {
    Osu(crate::osu::attributes::OsuPerformanceAttributes),
    Taiko(crate::taiko::attributes::TaikoPerformanceAttributes),
    Catch(crate::fruit::attributes::CatchPerformanceAttributes),
    Mania(crate::mania::attributes::ManiaPerformanceAttributes),
}

impl Default for PerformanceAttributes {
    fn default() -> Self {
        Self::Osu(Default::default())
    }
}

impl From<rosu_pp::any::PerformanceAttributes> for PerformanceAttributes {
    fn from(attributes: rosu_pp::any::PerformanceAttributes) -> Self {
        match attributes {
            rosu_pp::any::PerformanceAttributes::Osu(value) => Self::Osu(value.into()),
            rosu_pp::any::PerformanceAttributes::Taiko(value) => Self::Taiko(value.into()),
            rosu_pp::any::PerformanceAttributes::Catch(value) => Self::Catch(value.into()),
            rosu_pp::any::PerformanceAttributes::Mania(value) => Self::Mania(value.into()),
        }
    }
}

impl From<PerformanceAttributes> for rosu_pp::any::PerformanceAttributes {
    fn from(attributes: PerformanceAttributes) -> Self {
        match attributes {
            PerformanceAttributes::Osu(value) => Self::Osu(value.into()),
            PerformanceAttributes::Taiko(value) => Self::Taiko(value.into()),
            PerformanceAttributes::Catch(value) => Self::Catch(value.into()),
            PerformanceAttributes::Mania(value) => Self::Mania(value.into()),
        }
    }
}

#[ffi]
pub fn debug_difficulty_attributes(res: &DifficultyAttributes) -> FFIString {
    match res {
        DifficultyAttributes::Osu(value) => format!("{value:#?}"),
        DifficultyAttributes::Taiko(value) => format!("{value:#?}"),
        DifficultyAttributes::Catch(value) => format!("{value:#?}"),
        DifficultyAttributes::Mania(value) => format!("{value:#?}"),
    }
    .into()
}

#[ffi]
pub fn debug_performance_attributes(res: &PerformanceAttributes) -> FFIString {
    match res {
        PerformanceAttributes::Osu(value) => format!("{value:#?}"),
        PerformanceAttributes::Taiko(value) => format!("{value:#?}"),
        PerformanceAttributes::Catch(value) => format!("{value:#?}"),
        PerformanceAttributes::Mania(value) => format!("{value:#?}"),
    }
    .into()
}
