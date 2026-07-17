use interoptopus::{ffi, ffi::Option as FFIOption};

use crate::mode::Mode;

use super::LegacyVersion;

#[ffi]
#[repr(C)]
#[derive(Copy, Clone, Debug, Default, PartialEq)]
pub struct LegacyDifficultyAttributes {
    pub version: LegacyVersion,
    pub mode: Mode,
    pub stars: f64,
    pub max_combo: u32,
    pub aim: FFIOption<f64>,
    pub aim_difficult_slider_count: FFIOption<f64>,
    pub speed: FFIOption<f64>,
    pub flashlight: FFIOption<f64>,
    pub slider_factor: FFIOption<f64>,
    pub aim_top_weighted_slider_factor: FFIOption<f64>,
    pub speed_top_weighted_slider_factor: FFIOption<f64>,
    pub speed_note_count: FFIOption<f64>,
    pub aim_difficult_strain_count: FFIOption<f64>,
    pub speed_difficult_strain_count: FFIOption<f64>,
    pub nested_score_per_object: FFIOption<f64>,
    pub legacy_score_base_multiplier: FFIOption<f64>,
    pub maximum_legacy_combo_score: FFIOption<f64>,
    pub stamina: FFIOption<f64>,
    pub rhythm: FFIOption<f64>,
    pub color: FFIOption<f64>,
    pub reading: FFIOption<f64>,
    pub peak: FFIOption<f64>,
    pub mechanical_difficulty: FFIOption<f64>,
    pub consistency_factor: FFIOption<f64>,
    pub ar: FFIOption<f64>,
    pub od: FFIOption<f64>,
    pub hp: FFIOption<f64>,
    pub hit_window: FFIOption<f64>,
    pub great_hit_window: FFIOption<f64>,
    pub ok_hit_window: FFIOption<f64>,
    pub meh_hit_window: FFIOption<f64>,
    pub preempt: FFIOption<f64>,
    pub mono_stamina_factor: FFIOption<f64>,
    pub n_circles: FFIOption<u32>,
    pub n_sliders: FFIOption<u32>,
    pub n_large_ticks: FFIOption<u32>,
    pub n_spinners: FFIOption<u32>,
    pub n_fruits: FFIOption<u32>,
    pub n_droplets: FFIOption<u32>,
    pub n_tiny_droplets: FFIOption<u32>,
    pub n_objects: FFIOption<u32>,
    pub n_hold_notes: FFIOption<u32>,
    pub is_convert: FFIOption<bool>,
}

#[ffi]
#[repr(C)]
#[derive(Copy, Clone, Debug, Default, PartialEq)]
pub struct LegacyPerformanceAttributes {
    pub difficulty: LegacyDifficultyAttributes,
    pub pp: f64,
    pub pp_acc: FFIOption<f64>,
    pub pp_aim: FFIOption<f64>,
    pub pp_speed: FFIOption<f64>,
    pub pp_flashlight: FFIOption<f64>,
    pub pp_difficulty: FFIOption<f64>,
    pub effective_miss_count: FFIOption<f64>,
    pub estimated_unstable_rate: FFIOption<f64>,
    pub speed_deviation: FFIOption<f64>,
    pub combo_based_estimated_miss_count: FFIOption<f64>,
    pub score_based_estimated_miss_count: FFIOption<f64>,
    pub aim_estimated_slider_breaks: FFIOption<f64>,
    pub speed_estimated_slider_breaks: FFIOption<f64>,
}
