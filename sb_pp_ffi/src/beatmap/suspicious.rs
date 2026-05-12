use interoptopus::ffi_type;
use rosu_pp::model::beatmap;

impl From<TooSuspicious> for beatmap::TooSuspicious {
    fn from(value: TooSuspicious) -> Self {
        match value {
            TooSuspicious::Density => Self::Density,
            TooSuspicious::Length => Self::Length,
            TooSuspicious::ObjectCount => Self::ObjectCount,
            TooSuspicious::RedFlag => Self::RedFlag,
            TooSuspicious::SliderPositions => Self::SliderPositions,
            TooSuspicious::SliderRepeats => Self::SliderRepeats,
        }
    }
}

impl From<beatmap::TooSuspicious> for TooSuspicious {
    fn from(value: beatmap::TooSuspicious) -> Self {
        match value {
            beatmap::TooSuspicious::Density => Self::Density,
            beatmap::TooSuspicious::Length => Self::Length,
            beatmap::TooSuspicious::ObjectCount => Self::ObjectCount,
            beatmap::TooSuspicious::RedFlag => Self::RedFlag,
            beatmap::TooSuspicious::SliderPositions => Self::SliderPositions,
            beatmap::TooSuspicious::SliderRepeats => Self::SliderRepeats,
            _ => Self::default(),
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
