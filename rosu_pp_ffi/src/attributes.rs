use crate::owned_string::OwnedString;
use interoptopus::{
    ffi_function, ffi_type,
};

#[ffi_type]
#[derive(Debug, Clone)]
pub enum DifficultyAttributes {
    Osu(crate::osu::attributes::OsuDifficultyAttributes),
    Taiko(crate::taiko::attributes::TaikoDifficultyAttributes),
    Catch(crate::fruit::attributes::CatchDifficultyAttributes),
    Mania(crate::mania::attributes::ManiaDifficultyAttributes),
}

impl From<rosu_pp::any::DifficultyAttributes> for DifficultyAttributes {
    fn from(attributes: rosu_pp::any::DifficultyAttributes) -> Self {
        match attributes {
            rosu_pp::any::DifficultyAttributes::Osu(d) => Self::Osu(d.into()),
            rosu_pp::any::DifficultyAttributes::Taiko(d) => Self::Taiko(d.into()),
            rosu_pp::any::DifficultyAttributes::Catch(d) => Self::Catch(d.into()),
            rosu_pp::any::DifficultyAttributes::Mania(d) => Self::Mania(d.into()),
        }
    }
}

impl From<DifficultyAttributes> for rosu_pp::any::DifficultyAttributes {
    fn from(attributes: DifficultyAttributes) -> Self {
        match attributes {
            DifficultyAttributes::Osu(d) => rosu_pp::any::DifficultyAttributes::Osu(d.into()),
            DifficultyAttributes::Taiko(d) => rosu_pp::any::DifficultyAttributes::Taiko(d.into()),
            DifficultyAttributes::Catch(d) => rosu_pp::any::DifficultyAttributes::Catch(d.into()),
            DifficultyAttributes::Mania(d) => rosu_pp::any::DifficultyAttributes::Mania(d.into()),
        }
    }
}


#[ffi_type]
#[derive(Debug, Clone)]
pub enum PerformanceAttributes {
    Osu(crate::osu::attributes::OsuPerformanceAttributes),
    Taiko(crate::taiko::attributes::TaikoPerformanceAttributes),
    Catch(crate::fruit::attributes::CatchPerformanceAttributes),
    Mania(crate::mania::attributes::ManiaPerformanceAttributes),
}

impl From<rosu_pp::any::PerformanceAttributes> for PerformanceAttributes {
    fn from(attributes: rosu_pp::any::PerformanceAttributes) -> Self {
        match attributes {
            rosu_pp::any::PerformanceAttributes::Osu(d) => Self::Osu(d.into()),
            rosu_pp::any::PerformanceAttributes::Taiko(d) => Self::Taiko(d.into()),
            rosu_pp::any::PerformanceAttributes::Catch(d) => Self::Catch(d.into()),
            rosu_pp::any::PerformanceAttributes::Mania(d) => Self::Mania(d.into()),
        }
    }
}

impl From<PerformanceAttributes> for rosu_pp::any::PerformanceAttributes {
    fn from(attributes: PerformanceAttributes) -> Self {
        match attributes {
            PerformanceAttributes::Osu(d) => rosu_pp::any::PerformanceAttributes::Osu(d.into()),
            PerformanceAttributes::Taiko(d) => rosu_pp::any::PerformanceAttributes::Taiko(d.into()),
            PerformanceAttributes::Catch(d) => rosu_pp::any::PerformanceAttributes::Catch(d.into()),
            PerformanceAttributes::Mania(d) => rosu_pp::any::PerformanceAttributes::Mania(d.into()),
        }
    }
}


#[ffi_function]
pub fn debug_difficulty_attributes(res: &DifficultyAttributes, str: &mut OwnedString) {
    str.replace(format!("{res:#?}"))
}

#[ffi_function]
pub fn debug_performance_attributes(res: &PerformanceAttributes, str: &mut OwnedString) {
    str.replace(format!("{res:#?}"))
}