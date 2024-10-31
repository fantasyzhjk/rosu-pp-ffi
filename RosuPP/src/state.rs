use interoptopus::{ffi_function, ffi_type};

use crate::{mode::Mode, owned_string::OwnedString};


/// Aggregation for a score's current state.
#[derive(Clone, Debug, Eq, PartialEq)]
#[repr(C)]
#[ffi_type]
pub struct ScoreState {
    /// Maximum combo that the score has had so far. **Not** the maximum
    /// possible combo of the map so far.
    ///
    /// Note that for osu!catch only fruits and droplets are considered for
    /// combo.
    ///
    /// Irrelevant for osu!mania.
    pub max_combo: u32,
    /// Amount of successfully hit slider ticks and repeats.
    ///
    /// Only relevant for osu!standard in lazer.
    pub slider_tick_hits: u32,
    /// Amount of successfully hit slider ends.
    ///
    /// Only relevant for osu!standard in lazer.
    pub slider_end_hits: u32,
    /// Amount of current gekis (n320 for osu!mania).
    pub n_geki: u32,
    /// Amount of current katus (tiny droplet misses for osu!catch / n200 for
    /// osu!mania).
    pub n_katu: u32,
    /// Amount of current 300s (fruits for osu!catch).
    pub n300: u32,
    /// Amount of current 100s (droplets for osu!catch).
    pub n100: u32,
    /// Amount of current 50s (tiny droplets for osu!catch).
    pub n50: u32,
    /// Amount of current misses (fruits + droplets for osu!catch).
    pub misses: u32,
}

impl ScoreState {
    /// Return the total amount of hits by adding everything up based on the
    /// mode.
    pub fn total_hits(&self, mode: Mode) -> u32 {
        let mut amount = self.n300 + self.n100 + self.misses;

        if mode != Mode::Taiko {
            amount += self.n50;

            if mode != Mode::Osu {
                amount += self.n_katu;
                amount += u32::from(mode != Mode::Catch) * self.n_geki;
            }
        }

        amount
    }
}

impl From<rosu_pp::any::ScoreState> for ScoreState {
    fn from(value: rosu_pp::any::ScoreState) -> Self {
        Self {
            max_combo: value.max_combo,
            slider_tick_hits: 0,
            slider_end_hits: 0,
            n_geki: value.n_geki,
            n_katu: value.n_katu,
            n300: value.n300,
            n100: value.n100,
            n50: value.n50,
            misses: value.misses,
        }
    }
}

impl From<ScoreState> for rosu_pp::any::ScoreState {
    fn from(value: ScoreState) -> Self {
        Self {
            max_combo: value.max_combo,
            n_geki: value.n_geki,
            n_katu: value.n_katu,
            n300: value.n300,
            n100: value.n100,
            n50: value.n50,
            misses: value.misses,
        }
    }
}

#[ffi_function]
#[no_mangle]
pub extern "C" fn debug_score_state(res: &ScoreState, str: &mut OwnedString) {
    str.replace(format!("{:#?}", res))
}
