
pub trait GenerateStateLazer {
    fn generate_state_lazer(&self, beatmap: &crate::beatmap::Beatmap) -> crate::state::ScoreState;
}

use std::cmp;

use rosu_map::section::hit_objects::{CurveBuffers, SliderEventsIter};

use crate::hitresult_priority::HitResultPriority;

struct NoComboState {
    n300: u32,
    n100: u32,
    n50: u32,
    misses: u32,
    n_slider_ticks: u32,
    n_slider_ends: u32,
}


fn accuracy(state: NoComboState, max_slider_ticks: u32, max_slider_ends: u32) -> f64 {
    let NoComboState {
        n300,
        n100,
        n50,
        misses,
        n_slider_ticks,
        n_slider_ends,
    } = state;

    if n_slider_ticks + n_slider_ends + n300 + n100 + n50 + misses == 0 {
        return 0.0;
    }

    let numerator = 300 * n300 + 100 * n100 + 50 * n50 + 150 * n_slider_ends + 30 * n_slider_ticks;

    let denominator =
        300 * (n300 + n100 + n50 + misses) + 150 * max_slider_ends + 30 * max_slider_ticks;

    f64::from(numerator) / f64::from(denominator)
}

impl GenerateStateLazer for crate::performance::Performance {
    fn generate_state_lazer(
        &self,
        beatmap: &crate::beatmap::Beatmap,
    ) -> crate::state::ScoreState {
        let diff = rosu_pp::Difficulty::new();
        let attrs = diff.calculate(&beatmap.inner);

        if let rosu_pp::any::DifficultyAttributes::Osu(attrs) = attrs {
            let max_combo = attrs.max_combo;
            let n_objects = attrs.n_objects();
            let priority = self.hitresult_priority.into_option().unwrap_or(HitResultPriority::BestCase);

            let misses = self.misses.into_option().map_or(0, |n| cmp::min(n, n_objects));
            let n_remaining = n_objects - misses;

            let mut n300 = self.n300.into_option().map_or(0, |n: u32| cmp::min(n, n_remaining));
            let mut n100 = self.n100.into_option().map_or(0, |n| cmp::min(n, n_remaining));
            let mut n50 = self.n50.into_option().map_or(0, |n| cmp::min(n, n_remaining));

            let lazer = true;

            let (n_slider_ends, n_slider_ticks, max_slider_ends, max_slider_ticks) = if lazer {
                let n_slider_ends = self
                    .slider_end_hits
                    .into_option()
                    .map_or(attrs.n_sliders, |n| cmp::min(n, attrs.n_sliders));
                let n_slider_misses = self.slider_tick_misses.into_option().unwrap_or(0);
                let n_slider_hits = self.slider_tick_hits.into_option().unwrap_or(0);

                (
                    n_slider_ends,
                    n_slider_hits + n_slider_misses,
                    attrs.n_sliders,
                    n_slider_hits + n_slider_misses,
                )
            } else {
                (0, 0, 0, 0)
            };

            if let Some(acc) = self.accuracy.into_option().map(|acc| acc.clamp(0.0, 100.0) / 100.0) {
                let target_total =
                    acc * f64::from(30 * n_objects + 15 * max_slider_ends + 3 * max_slider_ticks);

                match (self.n300.into_option(), self.n100.into_option(), self.n50.into_option()) {
                    (Some(_), Some(_), Some(_)) => {
                        let remaining = n_objects.saturating_sub(n300 + n100 + n50 + misses);

                        
                        match priority {
                            HitResultPriority::BestCase => n300 += remaining,
                            HitResultPriority::WorstCase => n50 += remaining,
                        }
                    }
                    (Some(_), Some(_), None) => {
                        n50 = n_objects.saturating_sub(n300 + n100 + misses)
                    }
                    (Some(_), None, Some(_)) => {
                        n100 = n_objects.saturating_sub(n300 + n50 + misses)
                    }
                    (None, Some(_), Some(_)) => {
                        n300 = n_objects.saturating_sub(n100 + n50 + misses)
                    }
                    (Some(_), None, None) => {
                        let mut best_dist = f64::MAX;

                        n300 = cmp::min(n300, n_remaining);
                        let n_remaining = n_remaining - n300;

                        let raw_n100 = (target_total
                            - f64::from(
                                5 * n_remaining
                                    + 30 * n300
                                    + 15 * n_slider_ends
                                    + 3 * n_slider_ticks,
                            ))
                            / 5.0;
                        let min_n100 = cmp::min(n_remaining, raw_n100.floor() as u32);
                        let max_n100 = cmp::min(n_remaining, raw_n100.ceil() as u32);

                        for new100 in min_n100..=max_n100 {
                            let new50 = n_remaining - new100;

                            let state = NoComboState {
                                n300,
                                n100: new100,
                                n50: new50,
                                misses,
                                n_slider_ticks,
                                n_slider_ends,
                            };

                            let dist =
                                (acc - accuracy(state, max_slider_ticks, max_slider_ends)).abs();

                            if dist < best_dist {
                                best_dist = dist;
                                n100 = new100;
                                n50 = new50;
                            }
                        }
                    }
                    (None, Some(_), None) => {
                        let mut best_dist = f64::MAX;

                        n100 = cmp::min(n100, n_remaining);
                        let n_remaining = n_remaining - n100;

                        let raw_n300 = (target_total
                            - f64::from(
                                5 * n_remaining
                                    + 10 * n100
                                    + 15 * n_slider_ends
                                    + 3 * n_slider_ticks,
                            ))
                            / 25.0;
                        let min_n300 = cmp::min(n_remaining, raw_n300.floor() as u32);
                        let max_n300 = cmp::min(n_remaining, raw_n300.ceil() as u32);

                        for new300 in min_n300..=max_n300 {
                            let new50 = n_remaining - new300;

                            let state = NoComboState {
                                n300: new300,
                                n100,
                                n50: new50,
                                misses,
                                n_slider_ticks,
                                n_slider_ends,
                            };

                            let curr_dist =
                                (acc - accuracy(state, max_slider_ticks, max_slider_ends)).abs();

                            if curr_dist < best_dist {
                                best_dist = curr_dist;
                                n300 = new300;
                                n50 = new50;
                            }
                        }
                    }
                    (None, None, Some(_)) => {
                        let mut best_dist = f64::MAX;

                        n50 = cmp::min(n50, n_remaining);
                        let n_remaining = n_remaining - n50;

                        let raw_n300 = (target_total + f64::from(10 * misses + 5 * n50)
                            - f64::from(10 * n_objects + 15 * n_slider_ends + 3 * n_slider_ticks))
                            / 20.0;

                        let min_n300 = cmp::min(n_remaining, raw_n300.floor() as u32);
                        let max_n300 = cmp::min(n_remaining, raw_n300.ceil() as u32);

                        for new300 in min_n300..=max_n300 {
                            let new100 = n_remaining - new300;

                            let state = NoComboState {
                                n300: new300,
                                n100: new100,
                                n50,
                                misses,
                                n_slider_ticks,
                                n_slider_ends,
                            };

                            let curr_dist =
                                (acc - accuracy(state, max_slider_ticks, max_slider_ends)).abs();

                            if curr_dist < best_dist {
                                best_dist = curr_dist;
                                n300 = new300;
                                n100 = new100;
                            }
                        }
                    }
                    (None, None, None) => {
                        let mut best_dist = f64::MAX;

                        let raw_n300 = (target_total
                            - f64::from(5 * n_remaining + 15 * n_slider_ends + 3 * n_slider_ticks))
                            / 25.0;
                        let min_n300 = cmp::min(n_remaining, raw_n300.floor() as u32);
                        let max_n300 = cmp::min(n_remaining, raw_n300.ceil() as u32);

                        for new300 in min_n300..=max_n300 {
                            let raw_n100 = (target_total
                                - f64::from(
                                    5 * n_remaining
                                        + 25 * new300
                                        + 15 * n_slider_ends
                                        + 3 * n_slider_ticks,
                                ))
                                / 5.0;
                            let min_n100 = cmp::min(raw_n100.floor() as u32, n_remaining - new300);
                            let max_n100 = cmp::min(raw_n100.ceil() as u32, n_remaining - new300);

                            for new100 in min_n100..=max_n100 {
                                let new50 = n_remaining - new300 - new100;

                                let state = NoComboState {
                                    n300: new300,
                                    n100: new100,
                                    n50: new50,
                                    misses,
                                    n_slider_ticks,
                                    n_slider_ends,
                                };

                                let curr_dist = (acc
                                    - accuracy(state, max_slider_ticks, max_slider_ends))
                                .abs();

                                if curr_dist < best_dist {
                                    best_dist = curr_dist;
                                    n300 = new300;
                                    n100 = new100;
                                    n50 = new50;
                                }
                            }
                        }

                        match priority {
                            HitResultPriority::BestCase => {
                                // Shift n50 to n100 by sacrificing n300
                                let n = cmp::min(n300, n50 / 4);
                                n300 -= n;
                                n100 += 5 * n;
                                n50 -= 4 * n;
                            }
                            HitResultPriority::WorstCase => {
                                // Shift n100 to n50 by gaining n300
                                let n = n100 / 5;
                                n300 += n;
                                n100 -= 5 * n;
                                n50 += 4 * n;
                            }
                        }
                    }
                }
            } else {
                let remaining = n_objects.saturating_sub(n300 + n100 + n50 + misses);

                match priority {
                    HitResultPriority::BestCase => match (self.n300.into_option(), self.n100.into_option(), self.n50.into_option()) {
                        (None, ..) => n300 = remaining,
                        (_, None, _) => n100 = remaining,
                        (.., None) => n50 = remaining,
                        _ => n300 += remaining,
                    },
                    HitResultPriority::WorstCase => match (self.n50.into_option(), self.n100.into_option(), self.n300.into_option()) {
                        (None, ..) => n50 = remaining,
                        (_, None, _) => n100 = remaining,
                        (.., None) => n300 = remaining,
                        _ => n50 += remaining,
                    },
                }
            }

            let max_possible_combo = max_combo.saturating_sub(misses);

            let max_combo = self.combo.into_option().map_or(max_possible_combo, |combo| {
                cmp::min(combo, max_possible_combo)
            });

            crate::state::ScoreState {
                max_combo,
                slider_tick_hits: n_slider_ticks,
                slider_end_hits: n_slider_ends,
                n300,
                n100,
                n50,
                misses,
                n_geki: self.n_geki.into_option().unwrap_or(0),
                n_katu: self.n_katu.into_option().unwrap_or(0),
            }
        } else {
            let mut performance = self.apply(rosu_pp::Performance::new(attrs));
            performance.generate_state().into()
        }

    }
}
