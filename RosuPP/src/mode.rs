use interoptopus::ffi_type;
use rosu_pp::model::mode::GameMode;

impl From<Mode> for GameMode {
    fn from(value: Mode) -> Self {
        match value {
            Mode::Osu => GameMode::Osu,
            Mode::Taiko => GameMode::Taiko,
            Mode::Catch => GameMode::Catch,
            Mode::Mania => GameMode::Mania,
        }
    }
}

impl From<GameMode> for Mode {
    fn from(value: GameMode) -> Self {
        match value {
            GameMode::Osu => Mode::Osu,
            GameMode::Taiko => Mode::Taiko,
            GameMode::Catch => Mode::Catch,
            GameMode::Mania => Mode::Mania,
        }
    }
}

impl From<Mode> for rosu_mods::GameMode {
    fn from(value: Mode) -> Self {
        match value {
            Mode::Osu => rosu_mods::GameMode::Osu,
            Mode::Taiko => rosu_mods::GameMode::Taiko,
            Mode::Catch => rosu_mods::GameMode::Catch,
            Mode::Mania => rosu_mods::GameMode::Mania,
        }
    }
}


impl From<rosu_mods::GameMode> for Mode {
    fn from(value: rosu_mods::GameMode) -> Self {
        match value {
            rosu_mods::GameMode::Osu => Mode::Osu,
            rosu_mods::GameMode::Taiko => Mode::Taiko,
            rosu_mods::GameMode::Catch => Mode::Catch,
            rosu_mods::GameMode::Mania => Mode::Mania,
        }
    }
}

#[ffi_type]
#[repr(C)]
#[derive(Copy, Clone, Debug, Hash, PartialEq, Eq, Default)]
pub enum Mode {
    /// osu!standard
    #[default]
    Osu = 0,
    /// osu!taiko
    Taiko = 1,
    /// osu!catch
    Catch = 2,
    /// osu!mania
    Mania = 3,
}

impl std::fmt::Display for Mode {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        f.write_fmt(format_args!("{self:?}"))
    }
}
