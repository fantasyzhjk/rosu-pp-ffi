macro_rules! finish {
    ($value:expr, direct) => {
        $value
    };
    ($value:expr, checked) => {
        $value.expect("legacy beatmap conversion failed")
    };
}

macro_rules! old_osu_difficulty_attributes {
    (osu_2021_november, $version:expr, $attrs:ident) => {
        LegacyDifficultyAttributes {
            version: $version,
            mode: Mode::Osu,
            stars: $attrs.stars,
            max_combo: $attrs.max_combo,
            aim: Some($attrs.aim_strain).into(),
            speed: Some($attrs.speed_strain).into(),
            flashlight: Some($attrs.flashlight_rating).into(),
            slider_factor: Some($attrs.slider_factor).into(),
            ar: Some($attrs.ar).into(),
            od: Some($attrs.od).into(),
            hp: Some($attrs.hp).into(),
            n_circles: Some($attrs.n_circles as u32).into(),
            n_sliders: Some($attrs.n_sliders as u32).into(),
            n_spinners: Some($attrs.n_spinners as u32).into(),
            ..Default::default()
        }
    };
    ($module:ident, $version:expr, $attrs:ident) => {
        LegacyDifficultyAttributes {
            version: $version,
            mode: Mode::Osu,
            stars: $attrs.stars,
            max_combo: $attrs.max_combo as u32,
            aim: Some($attrs.aim_strain).into(),
            speed: Some($attrs.speed_strain).into(),
            ar: Some($attrs.ar).into(),
            od: Some($attrs.od).into(),
            hp: Some($attrs.hp).into(),
            n_circles: Some($attrs.n_circles as u32).into(),
            n_sliders: Some($attrs.n_sliders as u32).into(),
            n_spinners: Some($attrs.n_spinners as u32).into(),
            ..Default::default()
        }
    };
}

macro_rules! modern_osu_difficulty_attributes {
    (osu_2022, $version:expr, $attrs:ident) => {
        LegacyDifficultyAttributes {
            version: $version,
            mode: Mode::Osu,
            stars: $attrs.stars,
            max_combo: $attrs.max_combo,
            aim: Some($attrs.aim).into(),
            speed: Some($attrs.speed).into(),
            flashlight: Some($attrs.flashlight).into(),
            slider_factor: Some($attrs.slider_factor).into(),
            speed_note_count: Some($attrs.speed_note_count).into(),
            ar: Some($attrs.ar).into(),
            od: Some($attrs.od).into(),
            hp: Some($attrs.hp).into(),
            n_circles: Some($attrs.n_circles).into(),
            n_sliders: Some($attrs.n_sliders).into(),
            n_spinners: Some($attrs.n_spinners).into(),
            ..Default::default()
        }
    };
    (osu_2024, $version:expr, $attrs:ident) => {
        LegacyDifficultyAttributes {
            version: $version,
            mode: Mode::Osu,
            stars: $attrs.stars,
            max_combo: $attrs.max_combo,
            aim: Some($attrs.aim).into(),
            speed: Some($attrs.speed).into(),
            flashlight: Some($attrs.flashlight).into(),
            slider_factor: Some($attrs.slider_factor).into(),
            speed_note_count: Some($attrs.speed_note_count).into(),
            aim_difficult_strain_count: Some($attrs.aim_difficult_strain_count).into(),
            speed_difficult_strain_count: Some($attrs.speed_difficult_strain_count).into(),
            ar: Some($attrs.ar).into(),
            od: Some($attrs.od).into(),
            hp: Some($attrs.hp).into(),
            n_circles: Some($attrs.n_circles).into(),
            n_sliders: Some($attrs.n_sliders).into(),
            n_large_ticks: Some($attrs.n_large_ticks).into(),
            n_spinners: Some($attrs.n_spinners).into(),
            ..Default::default()
        }
    };
    (osu_2025, $version:expr, $attrs:ident) => {
        LegacyDifficultyAttributes {
            version: $version,
            mode: Mode::Osu,
            stars: $attrs.stars,
            max_combo: $attrs.max_combo,
            aim: Some($attrs.aim).into(),
            aim_difficult_slider_count: Some($attrs.aim_difficult_slider_count).into(),
            speed: Some($attrs.speed).into(),
            flashlight: Some($attrs.flashlight).into(),
            slider_factor: Some($attrs.slider_factor).into(),
            speed_note_count: Some($attrs.speed_note_count).into(),
            aim_difficult_strain_count: Some($attrs.aim_difficult_strain_count).into(),
            speed_difficult_strain_count: Some($attrs.speed_difficult_strain_count).into(),
            ar: Some($attrs.ar).into(),
            od: Some($attrs.od()).into(),
            hp: Some($attrs.hp).into(),
            great_hit_window: Some($attrs.great_hit_window).into(),
            ok_hit_window: Some($attrs.ok_hit_window).into(),
            meh_hit_window: Some($attrs.meh_hit_window).into(),
            n_circles: Some($attrs.n_circles).into(),
            n_sliders: Some($attrs.n_sliders).into(),
            n_large_ticks: Some($attrs.n_large_ticks).into(),
            n_spinners: Some($attrs.n_spinners).into(),
            ..Default::default()
        }
    };
    (base, $version:expr, $attrs:ident) => {
        LegacyDifficultyAttributes {
            version: $version,
            mode: Mode::Osu,
            stars: $attrs.stars,
            max_combo: $attrs.max_combo,
            aim: Some($attrs.aim).into(),
            aim_difficult_slider_count: Some($attrs.aim_difficult_slider_count).into(),
            speed: Some($attrs.speed).into(),
            flashlight: Some($attrs.flashlight).into(),
            slider_factor: Some($attrs.slider_factor).into(),
            aim_top_weighted_slider_factor: Some($attrs.aim_top_weighted_slider_factor).into(),
            speed_top_weighted_slider_factor: Some($attrs.speed_top_weighted_slider_factor).into(),
            speed_note_count: Some($attrs.speed_note_count).into(),
            aim_difficult_strain_count: Some($attrs.aim_difficult_strain_count).into(),
            speed_difficult_strain_count: Some($attrs.speed_difficult_strain_count).into(),
            nested_score_per_object: Some($attrs.nested_score_per_object).into(),
            legacy_score_base_multiplier: Some($attrs.legacy_score_base_multiplier).into(),
            maximum_legacy_combo_score: Some($attrs.maximum_legacy_combo_score).into(),
            ar: Some($attrs.ar).into(),
            od: Some($attrs.od()).into(),
            hp: Some($attrs.hp).into(),
            great_hit_window: Some($attrs.great_hit_window).into(),
            ok_hit_window: Some($attrs.ok_hit_window).into(),
            meh_hit_window: Some($attrs.meh_hit_window).into(),
            n_circles: Some($attrs.n_circles).into(),
            n_sliders: Some($attrs.n_sliders).into(),
            n_large_ticks: Some($attrs.n_large_ticks).into(),
            n_spinners: Some($attrs.n_spinners).into(),
            ..Default::default()
        }
    };
}

macro_rules! modern_taiko_difficulty_attributes {
    (taiko_2022, $version:expr, $attrs:ident) => {
        LegacyDifficultyAttributes {
            version: $version,
            mode: Mode::Taiko,
            stars: $attrs.stars,
            max_combo: $attrs.max_combo,
            stamina: Some($attrs.stamina).into(),
            rhythm: Some($attrs.rhythm).into(),
            color: Some($attrs.color).into(),
            peak: Some($attrs.peak).into(),
            hit_window: Some($attrs.hit_window).into(),
            is_convert: Some($attrs.is_convert).into(),
            ..Default::default()
        }
    };
    (taiko_2024, $version:expr, $attrs:ident) => {
        LegacyDifficultyAttributes {
            version: $version,
            mode: Mode::Taiko,
            stars: $attrs.stars,
            max_combo: $attrs.max_combo,
            stamina: Some($attrs.stamina).into(),
            rhythm: Some($attrs.rhythm).into(),
            color: Some($attrs.color).into(),
            peak: Some($attrs.peak).into(),
            great_hit_window: Some($attrs.great_hit_window).into(),
            ok_hit_window: Some($attrs.ok_hit_window).into(),
            mono_stamina_factor: Some($attrs.mono_stamina_factor).into(),
            is_convert: Some($attrs.is_convert).into(),
            ..Default::default()
        }
    };
    (taiko_2025, $version:expr, $attrs:ident) => {
        LegacyDifficultyAttributes {
            version: $version,
            mode: Mode::Taiko,
            stars: $attrs.stars,
            max_combo: $attrs.max_combo,
            stamina: Some($attrs.stamina).into(),
            rhythm: Some($attrs.rhythm).into(),
            color: Some($attrs.color).into(),
            reading: Some($attrs.reading).into(),
            great_hit_window: Some($attrs.great_hit_window).into(),
            ok_hit_window: Some($attrs.ok_hit_window).into(),
            mono_stamina_factor: Some($attrs.mono_stamina_factor).into(),
            is_convert: Some($attrs.is_convert).into(),
            ..Default::default()
        }
    };
    (base, $version:expr, $attrs:ident) => {
        LegacyDifficultyAttributes {
            version: $version,
            mode: Mode::Taiko,
            stars: $attrs.stars,
            max_combo: $attrs.max_combo,
            stamina: Some($attrs.stamina).into(),
            rhythm: Some($attrs.rhythm).into(),
            color: Some($attrs.color).into(),
            reading: Some($attrs.reading).into(),
            great_hit_window: Some($attrs.great_hit_window).into(),
            ok_hit_window: Some($attrs.ok_hit_window).into(),
            mono_stamina_factor: Some($attrs.mono_stamina_factor).into(),
            mechanical_difficulty: Some($attrs.mechanical_difficulty).into(),
            consistency_factor: Some($attrs.consistency_factor).into(),
            is_convert: Some($attrs.is_convert).into(),
            ..Default::default()
        }
    };
}

macro_rules! fruits_difficulty_attributes {
    ($version:expr, $attrs:ident) => {
        LegacyDifficultyAttributes {
            version: $version,
            mode: Mode::Catch,
            stars: $attrs.stars,
            max_combo: $attrs.max_combo(),
            ar: Some($attrs.ar).into(),
            n_fruits: Some($attrs.n_fruits).into(),
            n_droplets: Some($attrs.n_droplets).into(),
            n_tiny_droplets: Some($attrs.n_tiny_droplets).into(),
            is_convert: Some($attrs.is_convert).into(),
            ..Default::default()
        }
    };
    (base, $version:expr, $attrs:ident) => {
        LegacyDifficultyAttributes {
            version: $version,
            mode: Mode::Catch,
            stars: $attrs.stars,
            max_combo: $attrs.max_combo(),
            preempt: Some($attrs.preempt).into(),
            n_fruits: Some($attrs.n_fruits).into(),
            n_droplets: Some($attrs.n_droplets).into(),
            n_tiny_droplets: Some($attrs.n_tiny_droplets).into(),
            is_convert: Some($attrs.is_convert).into(),
            ..Default::default()
        }
    };
}

macro_rules! mania_difficulty_attributes {
    (mania_2022, $version:expr, $attrs:ident) => {
        LegacyDifficultyAttributes {
            version: $version,
            mode: Mode::Mania,
            stars: $attrs.stars,
            max_combo: $attrs.max_combo,
            hit_window: Some($attrs.hit_window).into(),
            n_objects: Some($attrs.n_objects).into(),
            is_convert: Some($attrs.is_convert).into(),
            ..Default::default()
        }
    };
    (base, $version:expr, $attrs:ident) => {
        LegacyDifficultyAttributes {
            version: $version,
            mode: Mode::Mania,
            stars: $attrs.stars,
            max_combo: $attrs.max_combo,
            n_objects: Some($attrs.n_objects).into(),
            n_hold_notes: Some($attrs.n_hold_notes).into(),
            is_convert: Some($attrs.is_convert).into(),
            ..Default::default()
        }
    };
}

macro_rules! modern_osu_performance_attributes {
    (osu_2022, $result:ident) => {
        LegacyPerformanceAttributes {
            pp: $result.pp,
            pp_acc: Some($result.pp_acc).into(),
            pp_aim: Some($result.pp_aim).into(),
            pp_speed: Some($result.pp_speed).into(),
            pp_flashlight: Some($result.pp_flashlight).into(),
            effective_miss_count: Some($result.effective_miss_count).into(),
            ..Default::default()
        }
    };
    (osu_2024, $result:ident) => {
        modern_osu_performance_attributes!(osu_2022, $result)
    };
    (osu_2025, $result:ident) => {
        LegacyPerformanceAttributes {
            pp: $result.pp,
            pp_acc: Some($result.pp_acc).into(),
            pp_aim: Some($result.pp_aim).into(),
            pp_speed: Some($result.pp_speed).into(),
            pp_flashlight: Some($result.pp_flashlight).into(),
            effective_miss_count: Some($result.effective_miss_count).into(),
            speed_deviation: $result.speed_deviation.into(),
            ..Default::default()
        }
    };
}

macro_rules! modern_taiko_performance_attributes {
    (taiko_2022, $result:ident) => {
        LegacyPerformanceAttributes {
            pp: $result.pp,
            pp_acc: Some($result.pp_acc).into(),
            pp_difficulty: Some($result.pp_difficulty).into(),
            effective_miss_count: Some($result.effective_miss_count).into(),
            ..Default::default()
        }
    };
    ($module:ident, $result:ident) => {
        LegacyPerformanceAttributes {
            pp: $result.pp,
            pp_acc: Some($result.pp_acc).into(),
            pp_difficulty: Some($result.pp_difficulty).into(),
            effective_miss_count: Some($result.effective_miss_count).into(),
            estimated_unstable_rate: $result.estimated_unstable_rate.into(),
            ..Default::default()
        }
    };
}

macro_rules! apply_base_performance_state {
    ($calculation:expr, $state:expr) => {{
        let mut calculation = $calculation;
        if let Some(value) = $state.accuracy {
            calculation = calculation.accuracy(value);
        }
        if let Some(value) = $state.combo {
            calculation = calculation.combo(value);
        }
        if let Some(value) = $state.misses {
            calculation = calculation.misses(value);
        }
        if let Some(value) = $state.n300 {
            calculation = calculation.n300(value);
        }
        if let Some(value) = $state.n100 {
            calculation = calculation.n100(value);
        }
        if let Some(value) = $state.n50 {
            calculation = calculation.n50(value);
        }
        if let Some(value) = $state.n_katu {
            calculation = calculation.n_katu(value);
        }
        if let Some(value) = $state.n_geki {
            calculation = calculation.n_geki(value);
        }
        if let Some(value) = $state.lazer {
            calculation = calculation.lazer(value);
        }
        if let Some(value) = $state.legacy_total_score {
            calculation = calculation.legacy_total_score(value);
        }
        if let Some(value) = $state.large_tick_hits {
            calculation = calculation.large_tick_hits(value);
        }
        if let Some(value) = $state.small_tick_hits {
            calculation = calculation.small_tick_hits(value);
        }
        if let Some(value) = $state.slider_end_hits {
            calculation = calculation.slider_end_hits(value);
        }
        calculation
    }};
}

/// Apply osu-specific tick/lazer fields to modern legacy `OsuPP` builders.
///
/// osu_2022 lacks these setters so the value is passed through unchanged.
macro_rules! apply_modern_osu_score_state {
    (osu_2022, $calc:expr, $state:expr) => {
        $calc
    };
    ($module:ident, $calc:expr, $state:expr) => {{
        let mut calc = $calc;
        if let Some(value) = $state.lazer {
            calc = calc.lazer(value);
        }
        if let Some(value) = $state.large_tick_hits {
            calc = calc.large_tick_hits(value);
        }
        if let Some(value) = $state.small_tick_hits {
            calc = calc.small_tick_hits(value);
        }
        if let Some(value) = $state.slider_end_hits {
            calc = calc.slider_end_hits(value);
        }
        calc
    }};
}

macro_rules! old_osu {
    ($name:ident, $module:ident) => {
        struct $name(LegacyVersion);

        impl LegacyCalculator for $name {
            fn version(&self) -> LegacyVersion {
                self.0
            }
            fn mode(&self) -> Mode {
                Mode::Osu
            }

            fn difficulty(
                &self,
                map: &rosu_pp_older_base::Beatmap,
                settings: &LegacyDifficulty,
            ) -> LegacyDifficulty {
                // Early osu modules keep their stars function and attribute type private.
                // Their public PP builder is the only way to obtain the reusable concrete attrs.
                let result = rosu_pp_older::$module::OsuPP::new(map)
                    .mods(settings.mods)
                    .calculate();
                let attrs = result.difficulty;
                let public_attrs = old_osu_difficulty_attributes!($module, self.0, attrs);
                let prepared = prepare(attrs, move |attrs, map, state| {
                    let mut calc = rosu_pp_older::$module::OsuPP::new(map)
                        .attributes((*attrs).clone())
                        .mods(state.bits());
                    if let Some(value) = state.accuracy {
                        calc = calc.accuracy(value as _);
                    }
                    if let Some(value) = state.combo {
                        calc = calc.combo(value);
                    }
                    if let Some(value) = state.misses {
                        calc = calc.misses(value);
                    }
                    if let Some(value) = state.n300 {
                        calc = calc.n300(value);
                    }
                    if let Some(value) = state.n100 {
                        calc = calc.n100(value);
                    }
                    if let Some(value) = state.n50 {
                        calc = calc.n50(value);
                    }
                    let result = calc.calculate();
                    LegacyPerformanceAttributes {
                        pp: result.pp,
                        pp_acc: Some(result.pp_acc).into(),
                        pp_aim: Some(result.pp_aim).into(),
                        pp_speed: Some(result.pp_speed).into(),
                        pp_flashlight: Some(result.pp_flashlight).into(),
                        ..Default::default()
                    }
                });
                LegacyDifficulty::new(public_attrs, prepared)
            }
        }
    };
}

macro_rules! old_taiko {
    ($name:ident, $module:ident, $difficulty:expr) => {
        struct $name(LegacyVersion);

        impl LegacyCalculator for $name {
            fn version(&self) -> LegacyVersion {
                self.0
            }
            fn mode(&self) -> Mode {
                Mode::Taiko
            }

            fn difficulty(
                &self,
                map: &rosu_pp_older_base::Beatmap,
                settings: &LegacyDifficulty,
            ) -> LegacyDifficulty {
                let attrs = $difficulty(map, settings.mods);
                let public_attrs = LegacyDifficultyAttributes {
                    version: self.0,
                    mode: self.mode(),
                    stars: attrs.stars,
                    max_combo: attrs.max_combo,
                    ..Default::default()
                };
                let prepared = prepare(attrs, move |attrs, map, state| {
                    let mut calc = rosu_pp_older::$module::TaikoPP::new(map)
                        .attributes((*attrs).clone())
                        .mods(state.bits());
                    if let Some(value) = state.accuracy {
                        calc = calc.accuracy(value as _);
                    }
                    if let Some(value) = state.combo {
                        calc = calc.combo(value);
                    }
                    if let Some(value) = state.misses {
                        calc = calc.misses(value);
                    }
                    if let Some(value) = state.n300 {
                        calc = calc.n300(value);
                    }
                    if let Some(value) = state.n100 {
                        calc = calc.n100(value);
                    }
                    let result = calc.calculate();
                    LegacyPerformanceAttributes {
                        pp: result.pp,
                        pp_acc: Some(result.pp_acc).into(),
                        pp_difficulty: Some(result.pp_strain).into(),
                        ..Default::default()
                    }
                });
                LegacyDifficulty::new(public_attrs, prepared)
            }
        }
    };
}

macro_rules! old_taiko_ppv1 {
    ($name:ident) => {
        struct $name(LegacyVersion);

        impl LegacyCalculator for $name {
            fn version(&self) -> LegacyVersion {
                self.0
            }
            fn mode(&self) -> Mode {
                Mode::Taiko
            }

            fn difficulty(
                &self,
                map: &rosu_pp_older_base::Beatmap,
                settings: &LegacyDifficulty,
            ) -> LegacyDifficulty {
                let attrs = rosu_pp_older::taiko_ppv1::stars(map, settings.mods);
                let stars = attrs.stars;
                let public_attrs = LegacyDifficultyAttributes {
                    version: self.0,
                    mode: self.mode(),
                    stars,
                    max_combo: attrs.max_combo,
                    ..Default::default()
                };
                let prepared = prepare(stars as f32, move |stars_attr, map, state| {
                    let mut calc = rosu_pp_older::taiko_ppv1::TaikoPP::new(map)
                        .attributes(*stars_attr)
                        .mods(state.bits());
                    if let Some(value) = state.accuracy {
                        calc = calc.accuracy(value as _);
                    }
                    if let Some(value) = state.combo {
                        calc = calc.combo(value);
                    }
                    if let Some(value) = state.misses {
                        calc = calc.misses(value);
                    }
                    if let Some(value) = state.n300 {
                        calc = calc.n300(value);
                    }
                    if let Some(value) = state.n100 {
                        calc = calc.n100(value);
                    }
                    let result = calc.calculate();
                    LegacyPerformanceAttributes {
                        pp: result.pp,
                        pp_acc: Some(result.pp_acc).into(),
                        pp_difficulty: Some(result.pp_strain).into(),
                        ..Default::default()
                    }
                });
                LegacyDifficulty::new(public_attrs, prepared)
            }
        }
    };
}

macro_rules! old_fruits {
    ($name:ident, $module:ident) => {
        struct $name(LegacyVersion);

        impl LegacyCalculator for $name {
            fn version(&self) -> LegacyVersion {
                self.0
            }
            fn mode(&self) -> Mode {
                Mode::Catch
            }

            fn difficulty(
                &self,
                map: &rosu_pp_older_base::Beatmap,
                settings: &LegacyDifficulty,
            ) -> LegacyDifficulty {
                let attrs = rosu_pp_older::$module::stars(map, settings.mods);
                let public_attrs = fruits_difficulty_attributes!(base, self.0, attrs);
                let prepared = prepare(attrs, move |attrs, map, state| {
                    let mut calc = rosu_pp_older::$module::FruitsPP::new(map)
                        .attributes((*attrs).clone())
                        .mods(state.bits());
                    if let Some(value) = state.accuracy {
                        calc = calc.accuracy(value as _);
                    }
                    if let Some(value) = state.combo {
                        calc = calc.combo(value);
                    }
                    if let Some(value) = state.misses {
                        calc = calc.misses(value);
                    }
                    if let Some(value) = state.n300 {
                        calc = calc.fruits(value);
                    }
                    if let Some(value) = state.n100 {
                        calc = calc.droplets(value);
                    }
                    if let Some(value) = state.n50 {
                        calc = calc.tiny_droplets(value);
                    }
                    if let Some(value) = state.n_katu {
                        calc = calc.tiny_droplet_misses(value);
                    }
                    let result = calc.calculate();
                    LegacyPerformanceAttributes {
                        pp: result.pp,
                        ..Default::default()
                    }
                });
                LegacyDifficulty::new(public_attrs, prepared)
            }
        }
    };
}

macro_rules! old_mania {
    ($name:ident, $module:ident, $difficulty:expr, $accuracy:ident) => {
        struct $name(LegacyVersion);

        impl LegacyCalculator for $name {
            fn version(&self) -> LegacyVersion {
                self.0
            }
            fn mode(&self) -> Mode {
                Mode::Mania
            }

            fn difficulty(
                &self,
                map: &rosu_pp_older_base::Beatmap,
                settings: &LegacyDifficulty,
            ) -> LegacyDifficulty {
                let attrs = $difficulty(map, settings.mods);
                let stars = attrs.stars;
                let max_combo = map.hit_objects.len() as u32;
                let public_attrs = LegacyDifficultyAttributes {
                    version: self.0,
                    mode: self.mode(),
                    stars,
                    max_combo,
                    ..Default::default()
                };
                let reusable = mania_reusable!(attrs, $accuracy);
                let prepared = prepare(reusable, move |attrs, map, state| {
                    let calc = rosu_pp_older::$module::ManiaPP::new(map)
                        .attributes(*attrs)
                        .mods(state.bits());
                    let calc = apply_mania_score!(calc, state, $accuracy);
                    let result = calc.calculate();
                    LegacyPerformanceAttributes {
                        pp: result.pp,
                        pp_acc: Some(result.pp_acc).into(),
                        pp_difficulty: Some(result.pp_strain).into(),
                        ..Default::default()
                    }
                });
                LegacyDifficulty::new(public_attrs, prepared)
            }
        }
    };
}

macro_rules! mania_reusable {
    ($attrs:expr, accuracy) => {
        $attrs.stars as f32
    };
    ($attrs:expr, no_accuracy) => {
        $attrs.stars
    };
    ($attrs:expr, score) => {
        $attrs.stars
    };
}

macro_rules! apply_mania_score {
    ($calc:expr, $state:expr, accuracy) => {
        match $state.accuracy {
            Some(value) => $calc.accuracy(value as _),
            None => $calc,
        }
    };
    ($calc:expr, $state:expr, score) => {
        match $state.score {
            Some(value) => $calc.score(value),
            None => $calc,
        }
    };
}

macro_rules! modern_osu {
    ($name:ident, $module:ident, $finish:ident) => {
        struct $name(LegacyVersion);

        impl LegacyCalculator for $name {
            fn version(&self) -> LegacyVersion {
                self.0
            }
            fn mode(&self) -> Mode {
                Mode::Osu
            }

            fn difficulty(
                &self,
                map: &rosu_pp_older_base::Beatmap,
                settings: &LegacyDifficulty,
            ) -> LegacyDifficulty {
                let mut calc = rosu_pp_older::$module::OsuStars::new().mods(settings.mods);
                if let Some(value) = settings.passed_objects {
                    calc = calc.passed_objects(value);
                }
                if let Some(value) = settings.clock_rate {
                    calc = calc.clock_rate(value);
                }
                let attrs = calc.calculate(map);
                let public_attrs = modern_osu_difficulty_attributes!($module, self.0, attrs);
                let prepared = prepare(attrs, move |attrs, map, state| {
                    let mut calc = rosu_pp_older::$module::OsuPP::new(map)
                        .attributes((*attrs).clone())
                        .mods(state.bits());
                    if let Some(value) = state.accuracy {
                        calc = calc.accuracy(value);
                    }
                    if let Some(value) = state.combo {
                        calc = calc.combo(value);
                    }
                    if let Some(value) = state.misses {
                        calc = calc.misses(value);
                    }
                    if let Some(value) = state.n300 {
                        calc = calc.n300(value);
                    }
                    if let Some(value) = state.n100 {
                        calc = calc.n100(value);
                    }
                    if let Some(value) = state.n50 {
                        calc = calc.n50(value);
                    }
                    let calc = apply_modern_osu_score_state!($module, calc, state);
                    let result = finish!(calc.calculate(), $finish);
                    modern_osu_performance_attributes!($module, result)
                });
                LegacyDifficulty::new(public_attrs, prepared)
            }
        }
    };
    ($name:ident, base) => {
        struct $name;

        impl LegacyCalculator for $name {
            fn version(&self) -> LegacyVersion {
                LegacyVersion::RosuPpOlderBase
            }

            fn mode(&self) -> Mode {
                Mode::Osu
            }

            fn difficulty(
                &self,
                map: &rosu_pp_older_base::Beatmap,
                settings: &LegacyDifficulty,
            ) -> LegacyDifficulty {
                let mut calculation = rosu_pp_older_base::Difficulty::new().mods(settings.mods);
                if let Some(value) = settings.passed_objects {
                    calculation = calculation.passed_objects(value);
                }
                if let Some(value) = settings.clock_rate {
                    calculation = calculation.clock_rate(value);
                }
                let attrs = calculation
                    .calculate_for_mode::<rosu_pp_older_base::osu::Osu>(map)
                    .expect("legacy beatmap conversion failed");
                let public_attrs = modern_osu_difficulty_attributes!(base, self.version(), attrs);
                let attrs = rosu_pp_older_base::any::DifficultyAttributes::Osu(attrs);
                let prepared = prepare(attrs, move |attrs, _map, state| {
                    let calculation = apply_base_performance_state!(
                        attrs.clone().performance().mods(state.bits()),
                        state
                    );
                    base_performance_attributes(calculation.calculate())
                });

                LegacyDifficulty::new(public_attrs, prepared)
            }
        }
    };
}

macro_rules! modern_taiko {
    ($name:ident, $module:ident, $finish:ident) => {
        struct $name(LegacyVersion);

        impl LegacyCalculator for $name {
            fn version(&self) -> LegacyVersion {
                self.0
            }
            fn mode(&self) -> Mode {
                Mode::Taiko
            }

            fn difficulty(
                &self,
                map: &rosu_pp_older_base::Beatmap,
                settings: &LegacyDifficulty,
            ) -> LegacyDifficulty {
                let mut calc = rosu_pp_older::$module::TaikoStars::new().mods(settings.mods);
                if let Some(value) = settings.passed_objects {
                    calc = calc.passed_objects(value);
                }
                if let Some(value) = settings.clock_rate {
                    calc = calc.clock_rate(value);
                }
                let attrs = calc.calculate(map);
                let public_attrs = modern_taiko_difficulty_attributes!($module, self.0, attrs);
                let prepared = prepare(attrs, move |attrs, map, state| {
                    let mut calc = rosu_pp_older::$module::TaikoPP::new(map)
                        .attributes((*attrs).clone())
                        .mods(state.bits());
                    if let Some(value) = state.accuracy {
                        calc = calc.accuracy(value);
                    }
                    if let Some(value) = state.combo {
                        calc = calc.combo(value);
                    }
                    if let Some(value) = state.misses {
                        calc = calc.misses(value);
                    }
                    if let Some(value) = state.n300 {
                        calc = calc.n300(value);
                    }
                    if let Some(value) = state.n100 {
                        calc = calc.n100(value);
                    }
                    let result = finish!(calc.calculate(), $finish);
                    modern_taiko_performance_attributes!($module, result)
                });
                LegacyDifficulty::new(public_attrs, prepared)
            }
        }
    };
    ($name:ident, base) => {
        struct $name;

        impl LegacyCalculator for $name {
            fn version(&self) -> LegacyVersion {
                LegacyVersion::RosuPpOlderBase
            }

            fn mode(&self) -> Mode {
                Mode::Taiko
            }

            fn difficulty(
                &self,
                map: &rosu_pp_older_base::Beatmap,
                settings: &LegacyDifficulty,
            ) -> LegacyDifficulty {
                let mut calculation = rosu_pp_older_base::Difficulty::new().mods(settings.mods);
                if let Some(value) = settings.passed_objects {
                    calculation = calculation.passed_objects(value);
                }
                if let Some(value) = settings.clock_rate {
                    calculation = calculation.clock_rate(value);
                }
                let attrs = calculation
                    .calculate_for_mode::<rosu_pp_older_base::taiko::Taiko>(map)
                    .expect("legacy beatmap conversion failed");
                let public_attrs = modern_taiko_difficulty_attributes!(base, self.version(), attrs);
                let attrs = rosu_pp_older_base::any::DifficultyAttributes::Taiko(attrs);
                let prepared = prepare(attrs, move |attrs, _map, state| {
                    let calculation = apply_base_performance_state!(
                        attrs.clone().performance().mods(state.bits()),
                        state
                    );
                    base_performance_attributes(calculation.calculate())
                });

                LegacyDifficulty::new(public_attrs, prepared)
            }
        }
    };
}

macro_rules! modern_fruits {
    ($name:ident, $module:ident, $stars_type:ident, $finish:ident) => {
        struct $name(LegacyVersion);

        impl LegacyCalculator for $name {
            fn version(&self) -> LegacyVersion {
                self.0
            }
            fn mode(&self) -> Mode {
                Mode::Catch
            }

            fn difficulty(
                &self,
                map: &rosu_pp_older_base::Beatmap,
                settings: &LegacyDifficulty,
            ) -> LegacyDifficulty {
                let mut calc = rosu_pp_older::$module::$stars_type::new().mods(settings.mods);
                if let Some(value) = settings.passed_objects {
                    calc = calc.passed_objects(value);
                }
                if let Some(value) = settings.clock_rate {
                    calc = calc.clock_rate(value);
                }
                let attrs = calc.calculate(map);
                let public_attrs = fruits_difficulty_attributes!(self.0, attrs);
                let prepared = prepare(attrs, move |attrs, map, state| {
                    let mut calc = rosu_pp_older::$module::FruitsPP::new(map)
                        .attributes((*attrs).clone())
                        .mods(state.bits());
                    if let Some(value) = state.accuracy {
                        calc = calc.accuracy(value);
                    }
                    if let Some(value) = state.combo {
                        calc = calc.combo(value);
                    }
                    if let Some(value) = state.misses {
                        calc = calc.misses(value);
                    }
                    if let Some(value) = state.n300 {
                        calc = calc.fruits(value);
                    }
                    if let Some(value) = state.n100 {
                        calc = calc.droplets(value);
                    }
                    if let Some(value) = state.n50 {
                        calc = calc.tiny_droplets(value);
                    }
                    if let Some(value) = state.n_katu {
                        calc = calc.tiny_droplet_misses(value);
                    }
                    let result = finish!(calc.calculate(), $finish);
                    LegacyPerformanceAttributes {
                        pp: result.pp,
                        ..Default::default()
                    }
                });
                LegacyDifficulty::new(public_attrs, prepared)
            }
        }
    };
    ($name:ident, base) => {
        struct $name;

        impl LegacyCalculator for $name {
            fn version(&self) -> LegacyVersion {
                LegacyVersion::RosuPpOlderBase
            }

            fn mode(&self) -> Mode {
                Mode::Catch
            }

            fn difficulty(
                &self,
                map: &rosu_pp_older_base::Beatmap,
                settings: &LegacyDifficulty,
            ) -> LegacyDifficulty {
                let mut calculation = rosu_pp_older_base::Difficulty::new().mods(settings.mods);
                if let Some(value) = settings.passed_objects {
                    calculation = calculation.passed_objects(value);
                }
                if let Some(value) = settings.clock_rate {
                    calculation = calculation.clock_rate(value);
                }
                let attrs = calculation
                    .calculate_for_mode::<rosu_pp_older_base::catch::Catch>(map)
                    .expect("legacy beatmap conversion failed");
                let public_attrs = fruits_difficulty_attributes!(base, self.version(), attrs);
                let attrs = rosu_pp_older_base::any::DifficultyAttributes::Catch(attrs);
                let prepared = prepare(attrs, move |attrs, _map, state| {
                    let calculation = apply_base_performance_state!(
                        attrs.clone().performance().mods(state.bits()),
                        state
                    );
                    base_performance_attributes(calculation.calculate())
                });

                LegacyDifficulty::new(public_attrs, prepared)
            }
        }
    };
}

macro_rules! modern_mania {
    ($name:ident, mania_2022) => {
        struct $name(LegacyVersion);

        impl LegacyCalculator for $name {
            fn version(&self) -> LegacyVersion {
                self.0
            }
            fn mode(&self) -> Mode {
                Mode::Mania
            }

            fn difficulty(
                &self,
                map: &rosu_pp_older_base::Beatmap,
                settings: &LegacyDifficulty,
            ) -> LegacyDifficulty {
                let mut calc = rosu_pp_older::mania_2022::ManiaStars::new().mods(settings.mods);
                if let Some(value) = settings.passed_objects {
                    calc = calc.passed_objects(value);
                }
                if let Some(value) = settings.clock_rate {
                    calc = calc.clock_rate(value);
                }
                let attrs = calc.calculate(map);
                let public_attrs = mania_difficulty_attributes!(mania_2022, self.0, attrs);
                let prepared = prepare(attrs, move |attrs, map, state| {
                    let mut calc = rosu_pp_older::mania_2022::ManiaPP::new(map)
                        .attributes((*attrs).clone())
                        .mods(state.bits());
                    if let Some(value) = state.accuracy {
                        calc = calc.accuracy(value);
                    }
                    if let Some(value) = state.misses {
                        calc = calc.misses(value);
                    }
                    if let Some(value) = state.n_geki {
                        calc = calc.n320(value);
                    }
                    if let Some(value) = state.n300 {
                        calc = calc.n300(value);
                    }
                    if let Some(value) = state.n_katu {
                        calc = calc.n200(value);
                    }
                    if let Some(value) = state.n100 {
                        calc = calc.n100(value);
                    }
                    if let Some(value) = state.n50 {
                        calc = calc.n50(value);
                    }
                    let result = calc.calculate();
                    LegacyPerformanceAttributes {
                        pp: result.pp,
                        pp_difficulty: Some(result.pp_difficulty).into(),
                        ..Default::default()
                    }
                });
                LegacyDifficulty::new(public_attrs, prepared)
            }
        }
    };
    ($name:ident, base) => {
        struct $name;

        impl LegacyCalculator for $name {
            fn version(&self) -> LegacyVersion {
                LegacyVersion::RosuPpOlderBase
            }

            fn mode(&self) -> Mode {
                Mode::Mania
            }

            fn difficulty(
                &self,
                map: &rosu_pp_older_base::Beatmap,
                settings: &LegacyDifficulty,
            ) -> LegacyDifficulty {
                let mut calculation = rosu_pp_older_base::Difficulty::new().mods(settings.mods);
                if let Some(value) = settings.passed_objects {
                    calculation = calculation.passed_objects(value);
                }
                if let Some(value) = settings.clock_rate {
                    calculation = calculation.clock_rate(value);
                }
                let attrs = calculation
                    .calculate_for_mode::<rosu_pp_older_base::mania::Mania>(map)
                    .expect("legacy beatmap conversion failed");
                let public_attrs = mania_difficulty_attributes!(base, self.version(), attrs);
                let attrs = rosu_pp_older_base::any::DifficultyAttributes::Mania(attrs);
                let prepared = prepare(attrs, move |attrs, _map, state| {
                    let calculation = apply_base_performance_state!(
                        attrs.clone().performance().mods(state.bits()),
                        state
                    );
                    base_performance_attributes(calculation.calculate())
                });

                LegacyDifficulty::new(public_attrs, prepared)
            }
        }
    };
}
