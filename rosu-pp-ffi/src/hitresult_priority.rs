use interoptopus::ffi_type;

impl From<HitResultPriority> for rosu_pp::any::HitResultPriority {
    fn from(value: HitResultPriority) -> Self {
        match value {
            HitResultPriority::BestCase => rosu_pp::any::HitResultPriority::BestCase,
            HitResultPriority::WorstCase => rosu_pp::any::HitResultPriority::WorstCase,
        }
    }
}

#[ffi_type]
#[repr(C)]
#[derive(Copy, Clone, Debug, Hash, PartialEq, Eq, Default)]
pub enum HitResultPriority {
    #[default]
    BestCase = 0,
    WorstCase = 1,
}

impl std::fmt::Display for HitResultPriority {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        f.write_fmt(format_args!("{self:?}"))
    }
}
