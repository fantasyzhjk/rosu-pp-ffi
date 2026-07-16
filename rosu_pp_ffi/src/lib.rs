use interoptopus::patterns::api_guard::APIVersion;
use interoptopus::{extra_type, ffi_function, function, pattern, Inventory, InventoryBuilder};

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
mod owned_string;
mod performance;
mod state;
mod taiko;
use error::{Error, FFIError};

#[ffi_function]
#[no_mangle]
pub extern "C" fn pattern_api_guard() -> APIVersion {
    crate::ffi_inventory().into()
}

// This will create a function `my_inventory` which can produce
// an abstract FFI representation (called `Library`) for this crate.
pub fn ffi_inventory() -> Inventory {
    InventoryBuilder::new()
        .register(extra_type!(beatmap::pos::Pos))
        .register(extra_type!(beatmap::hitobjects::HitObject))
        .register(extra_type!(beatmap::hitobjects::HitObjectData))
        .register(extra_type!(beatmap::hitobjects::HitObjectKind))
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
        .register(pattern!(beatmap::attributes::BeatmapAttributesBuilder))
        .register(pattern!(beatmap::Beatmap))
        .register(pattern!(beatmap::hitobjects::HitObjects))
        .register(pattern!(difficulty::Difficulty))
        .register(pattern!(performance::Performance))
        .register(pattern!(gradual::GradualDifficulty))
        .register(pattern!(gradual::GradualPerformance))
        .register(pattern!(owned_string::OwnedString))
        .register(pattern!(mods::Mods))
        .register(function!(attributes::debug_difficylty_attributes))
        .register(function!(attributes::debug_performance_attributes))
        .register(function!(state::debug_score_state))
        .register(function!(state::calculate_accuacy))
        .inventory()
}
