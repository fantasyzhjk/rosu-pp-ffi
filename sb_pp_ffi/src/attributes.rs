use crate::{mode::Mode, owned_string::OwnedString};
use interoptopus::{
    ffi_function, ffi_type,
    patterns::option::FFIOption,
};

#[ffi_type]
#[repr(C)]
#[derive(Debug, Clone, Default)]
pub struct DifficultyAttributes {
    pub osu: FFIOption<crate::osu::attributes::OsuDifficultyAttributes>,
    pub taiko: FFIOption<crate::taiko::attributes::TaikoDifficultyAttributes>,
    pub fruit: FFIOption<crate::fruit::attributes::CatchDifficultyAttributes>,
    pub mania: FFIOption<crate::mania::attributes::ManiaDifficultyAttributes>,
    pub mode: Mode,
}

impl From<rosu_pp::any::DifficultyAttributes> for DifficultyAttributes {
    fn from(attributes: rosu_pp::any::DifficultyAttributes) -> Self {
        match attributes {
            rosu_pp::any::DifficultyAttributes::Osu(d) => Self {
                osu: FFIOption::some(d.into()),
                mode: Mode::Osu,
                ..Default::default()
            },
            rosu_pp::any::DifficultyAttributes::Taiko(d) => Self {
                taiko: FFIOption::some(d.into()),
                mode: Mode::Taiko,
                ..Default::default()
            },
            rosu_pp::any::DifficultyAttributes::Catch(d) => Self {
                fruit: FFIOption::some(d.into()),
                mode: Mode::Catch,
                ..Default::default()
            },
            rosu_pp::any::DifficultyAttributes::Mania(d) => Self {
                mania: FFIOption::some(d.into()),
                mode: Mode::Mania,
                ..Default::default()
            },
        }
    }
}

impl From<DifficultyAttributes> for rosu_pp::any::DifficultyAttributes {
    fn from(attributes: DifficultyAttributes) -> Self {
        match attributes.mode {
            Mode::Osu => rosu_pp::any::DifficultyAttributes::Osu(attributes.osu.unwrap().into()),
            Mode::Taiko => rosu_pp::any::DifficultyAttributes::Taiko(attributes.taiko.unwrap().into()),
            Mode::Catch => rosu_pp::any::DifficultyAttributes::Catch(attributes.fruit.unwrap().into()),
            Mode::Mania => rosu_pp::any::DifficultyAttributes::Mania(attributes.mania.unwrap().into()),
        }
    }
}


#[ffi_type]
#[repr(C)]
#[derive(Debug, Default)]
pub struct PerformanceAttributes {
    pub osu: FFIOption<crate::osu::attributes::OsuPerformanceAttributes>,
    pub taiko: FFIOption<crate::taiko::attributes::TaikoPerformanceAttributes>,
    pub fruit: FFIOption<crate::fruit::attributes::CatchPerformanceAttributes>,
    pub mania: FFIOption<crate::mania::attributes::ManiaPerformanceAttributes>,
    pub mode: Mode,
}

impl From<rosu_pp::any::PerformanceAttributes> for PerformanceAttributes {
    fn from(attributes: rosu_pp::any::PerformanceAttributes) -> Self {
        match attributes {
            rosu_pp::any::PerformanceAttributes::Osu(d) => Self {
                osu: FFIOption::some(d.into()),
                mode: Mode::Osu,
                ..Default::default()
            },
            rosu_pp::any::PerformanceAttributes::Taiko(d) => Self {
                taiko: FFIOption::some(d.into()),
                mode: Mode::Taiko,
                ..Default::default()
            },
            rosu_pp::any::PerformanceAttributes::Catch(d) => Self {
                fruit: FFIOption::some(d.into()),
                mode: Mode::Catch,
                ..Default::default()
            },
            rosu_pp::any::PerformanceAttributes::Mania(d) => Self {
                mania: FFIOption::some(d.into()),
                mode: Mode::Mania,
                ..Default::default()
            },
        }
    }
}

impl From<PerformanceAttributes> for rosu_pp::any::PerformanceAttributes {
    fn from(attributes: PerformanceAttributes) -> Self {
        match attributes.mode {
            Mode::Osu => rosu_pp::any::PerformanceAttributes::Osu(attributes.osu.unwrap().into()),
            Mode::Taiko => rosu_pp::any::PerformanceAttributes::Taiko(attributes.taiko.unwrap().into()),
            Mode::Catch => rosu_pp::any::PerformanceAttributes::Catch(attributes.fruit.unwrap().into()),
            Mode::Mania => rosu_pp::any::PerformanceAttributes::Mania(attributes.mania.unwrap().into()),
        }
    }
}


#[ffi_function]
#[no_mangle]
pub extern "C" fn debug_difficylty_attributes(res: &DifficultyAttributes, str: &mut OwnedString) {
    str.replace(match res.mode {
        Mode::Osu => format!("{:#?}", res.osu.as_ref().unwrap()),
        Mode::Taiko => format!("{:#?}", res.taiko.as_ref().unwrap()),
        Mode::Catch => format!("{:#?}", res.fruit.as_ref().unwrap()),
        Mode::Mania => format!("{:#?}", res.mania.as_ref().unwrap()),
    })
}

#[ffi_function]
#[no_mangle]
pub extern "C" fn debug_performance_attributes(res: &PerformanceAttributes, str: &mut OwnedString) {
    str.replace(match res.mode {
        Mode::Osu => format!("{:#?}", res.osu.as_ref().unwrap()),
        Mode::Taiko => format!("{:#?}", res.taiko.as_ref().unwrap()),
        Mode::Catch => format!("{:#?}", res.fruit.as_ref().unwrap()),
        Mode::Mania => format!("{:#?}", res.mania.as_ref().unwrap()),
    })
}
