use interoptopus::ffi_type;

impl From<TooSuspicious> for rosu_pp::model::beatmap::TooSuspicious {
    fn from(value: TooSuspicious) -> Self {
        match value {
            TooSuspicious::Density => rosu_pp::model::beatmap::TooSuspicious::Density,
            TooSuspicious::Length => rosu_pp::model::beatmap::TooSuspicious::Length,
            TooSuspicious::ObjectCount => rosu_pp::model::beatmap::TooSuspicious::ObjectCount,
            TooSuspicious::RedFlag => rosu_pp::model::beatmap::TooSuspicious::RedFlag,
            TooSuspicious::SliderPositions => rosu_pp::model::beatmap::TooSuspicious::SliderPositions,
            TooSuspicious::SliderRepeats => rosu_pp::model::beatmap::TooSuspicious::SliderRepeats,
        }
    }
}

impl From<rosu_pp::model::beatmap::TooSuspicious> for TooSuspicious {
    fn from(value: rosu_pp::model::beatmap::TooSuspicious) -> Self {
        match value {
            rosu_pp::model::beatmap::TooSuspicious::Density => TooSuspicious::Density,
            rosu_pp::model::beatmap::TooSuspicious::Length => TooSuspicious::Length,
            rosu_pp::model::beatmap::TooSuspicious::ObjectCount => TooSuspicious::ObjectCount,
            rosu_pp::model::beatmap::TooSuspicious::RedFlag => TooSuspicious::RedFlag,
            rosu_pp::model::beatmap::TooSuspicious::SliderPositions => TooSuspicious::SliderPositions,
            rosu_pp::model::beatmap::TooSuspicious::SliderRepeats => TooSuspicious::SliderRepeats,
            _ => TooSuspicious::RedFlag,
        }
    }
}

#[ffi_type]
#[repr(C)]
#[derive(Copy, Clone, Debug, Hash, PartialEq, Eq, Default)]
pub enum TooSuspicious {
    /// Notes are too dense time-wise.
    Density,
    /// The map seems too long.
    Length,
    /// Too many objects.
    ObjectCount,
    /// General red flag.
    #[default]
    RedFlag,
    /// Too many sliders' positions were suspicious.
    SliderPositions,
    /// Too many sliders had a very high amount of repeats.
    SliderRepeats,
}

impl std::fmt::Display for TooSuspicious {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        f.write_fmt(format_args!("{self:?}"))
    }
}
