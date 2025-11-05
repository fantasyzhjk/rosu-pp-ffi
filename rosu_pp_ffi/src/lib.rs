
use interoptopus::{builtins_string, builtins_vec, builtins_wire, extra_type, function, pattern};
use interoptopus::inventory::Inventory;

mod error;
mod mode;
mod beatmap;
mod difficulty;
mod osu;
mod attributes;
mod mania;
mod fruit;
mod taiko;
mod performance;
mod state;
mod mods;
mod hitresult_priority;
mod gradual;
use error::Error;


// This will create a function `my_inventory` which can produce
// an abstract FFI representation (called `Library`) for this crate.
pub fn ffi_inventory() -> Inventory {
    Inventory::builder()
        .register(extra_type!(beatmap::pos::Pos))
        .register(extra_type!(beatmap::hitobject::HitObject))
        .register(extra_type!(beatmap::hitobject::HitObjectData))
        .register(extra_type!(beatmap::hitobject::HitObjectKind))
        .register(extra_type!(mode::Mode))
        .register(extra_type!(hitresult_priority::HitResultPriority))
        .register(extra_type!(state::OsuScoreOrigin))
        .register(extra_type!(state::ScoreState))
        .register(extra_type!(attributes::DifficultyAttributes))
        .register(extra_type!(attributes::PerformanceAttributes))
        .register(extra_type!(beatmap::attributes::BeatmapAttributes))
        .register(extra_type!(beatmap::attributes::HitWindows))
        .register(pattern!(beatmap::attributes::BeatmapAttributesBuilder))
        .register(pattern!(beatmap::Beatmap))
        .register(pattern!(difficulty::Difficulty))
        .register(pattern!(performance::Performance))
        .register(pattern!(gradual::GradualDifficulty))
        .register(pattern!(gradual::GradualPerformance))
        .register(pattern!(mods::Mods))
        .register(function!(attributes::debug_difficulty_attributes))
        .register(function!(attributes::debug_performance_attributes))
        .register(function!(state::debug_score_state))
        .register(function!(state::calculate_accuracy))
        .register(builtins_string!())
        .register(builtins_wire!())
        .register(builtins_vec!(beatmap::hitobject::HitObject))
        .validate()
        .build()
}
