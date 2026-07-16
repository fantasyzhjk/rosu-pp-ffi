use interoptopus::ffi;
use interoptopus::inventory::RustInventory;
use interoptopus::{builtins_string, builtins_wire, extra_type, function, guard, service};

mod error;
mod mode;
// mod calculator;
// mod params;
// mod result;
mod attributes;
mod beatmap;
mod difficulty;
mod fruit;
mod gradual;
mod hitresult_priority;
mod mania;
mod mods;
mod osu;
mod performance;
mod state;
mod taiko;
use error::{Error, FFIError};

pub(crate) fn ffi_result<T: interoptopus::lang::types::TypeInfo>(
    result: Result<T, Error>,
) -> ffi::Result<T, FFIError> {
    result.map_err(FFIError::from).into()
}

/// Describes every symbol exported by this FFI library.
pub fn ffi_inventory() -> RustInventory {
    RustInventory::new()
        .register(guard!(ffi_inventory))
        .register(builtins_string!())
        .register(builtins_wire!())
        .register(extra_type!(beatmap::pos::Pos))
        .register(extra_type!(mode::Mode))
        .register(extra_type!(hitresult_priority::HitResultPriority))
        .register(extra_type!(osu::attributes::OsuDifficultyAttributes))
        .register(extra_type!(osu::attributes::OsuPerformanceAttributes))
        .register(extra_type!(state::OsuScoreOrigin))
        .register(extra_type!(state::ScoreState))
        .register(extra_type!(attributes::DifficultyAttributes))
        .register(extra_type!(attributes::PerformanceAttributes))
        .register(extra_type!(beatmap::attributes::BeatmapAttributes))
        .register(extra_type!(beatmap::attributes::HitWindows))
        .register(service!(beatmap::attributes::BeatmapAttributesBuilder))
        .register(service!(beatmap::Beatmap))
        .register(service!(difficulty::Difficulty))
        .register(service!(performance::Performance))
        .register(service!(gradual::GradualDifficulty))
        .register(service!(gradual::GradualPerformance))
        .register(service!(mods::Mods))
        .register(function!(attributes::debug_difficulty_attributes))
        .register(function!(attributes::debug_performance_attributes))
        .register(function!(state::debug_score_state))
        .register(function!(state::calculate_accuacy))
        .validate()
}
