use std::sync::OnceLock;

use super::*;

old_osu!(Osu2014May, osu_2014_may);
old_osu!(Osu2014July, osu_2014_july);
old_osu!(Osu2015February, osu_2015_february);
old_osu!(Osu2015April, osu_2015_april);
old_osu!(Osu2018, osu_2018);
old_osu!(Osu2019, osu_2019);
old_osu!(Osu2021January, osu_2021_january);
old_osu!(Osu2021July, osu_2021_july);
old_osu!(Osu2021November, osu_2021_november);
modern_osu!(Osu2022, osu_2022, direct);
modern_osu!(Osu2024, osu_2024, direct);
modern_osu!(Osu2025, osu_2025, checked);
old_taiko_ppv1!(TaikoPpv1);
old_taiko!(Taiko2020, taiko_2020, |map, mods| {
    rosu_pp_older::taiko_2020::TaikoStars::new(map)
        .mods(mods)
        .calculate()
});
modern_taiko!(Taiko2022, taiko_2022, direct);
modern_taiko!(Taiko2024, taiko_2024, direct);
modern_taiko!(Taiko2025, taiko_2025, checked);
old_fruits!(FruitsPpv1, fruits_ppv1);
modern_fruits!(Fruits2022, fruits_2022, CatchStars, direct);
modern_fruits!(Fruits2024, fruits_2024, OsuStars, checked);
old_mania!(
    ManiaPpv1,
    mania_ppv1,
    rosu_pp_older::mania_ppv1::stars,
    accuracy
);
old_mania!(
    Mania2018,
    mania_2018,
    |map, mods| rosu_pp_older::mania_2018::ManiaStars::new(map)
        .mods(mods)
        .calculate(),
    no_accuracy
);
modern_mania!(Mania2022, mania_2022);

modern_osu!(BaseOsu, base);
modern_taiko!(BaseTaiko, base);
modern_fruits!(BaseCatch, base);
modern_mania!(BaseMania, base);

pub(super) fn find(version: LegacyVersion, mode: Mode) -> Option<&'static dyn LegacyCalculator> {
    registry()
        .iter()
        .find(|calculator| calculator.version() == version && calculator.mode() == mode)
        .map(Box::as_ref)
}

fn registry() -> &'static [Box<dyn LegacyCalculator>] {
    static REGISTRY: OnceLock<Vec<Box<dyn LegacyCalculator>>> = OnceLock::new();
    REGISTRY.get_or_init(|| {
        vec![
            Box::new(Osu2014May(LegacyVersion::Osu2014May)),
            Box::new(Osu2014July(LegacyVersion::Osu2014July)),
            Box::new(Osu2015February(LegacyVersion::Osu2015February)),
            Box::new(Osu2015April(LegacyVersion::Osu2015April)),
            Box::new(Osu2018(LegacyVersion::Osu2018)),
            Box::new(Osu2019(LegacyVersion::Osu2019)),
            Box::new(Osu2021January(LegacyVersion::Osu2021January)),
            Box::new(Osu2021July(LegacyVersion::Osu2021July)),
            Box::new(Osu2021November(LegacyVersion::Osu2021November)),
            Box::new(Osu2022(LegacyVersion::Osu2022)),
            Box::new(Osu2024(LegacyVersion::Osu2024)),
            Box::new(Osu2025(LegacyVersion::Osu2025)),
            Box::new(TaikoPpv1(LegacyVersion::TaikoPpv1)),
            Box::new(Taiko2020(LegacyVersion::Taiko2020)),
            Box::new(Taiko2022(LegacyVersion::Taiko2022)),
            Box::new(Taiko2024(LegacyVersion::Taiko2024)),
            Box::new(Taiko2025(LegacyVersion::Taiko2025)),
            Box::new(FruitsPpv1(LegacyVersion::FruitsPpv1)),
            Box::new(Fruits2022(LegacyVersion::Fruits2022)),
            Box::new(Fruits2024(LegacyVersion::Fruits2024)),
            Box::new(ManiaPpv1(LegacyVersion::ManiaPpv1)),
            Box::new(Mania2018(LegacyVersion::Mania2018)),
            Box::new(Mania2022(LegacyVersion::Mania2022)),
            Box::new(Osu2022(LegacyVersion::V2022)),
            Box::new(Taiko2022(LegacyVersion::V2022)),
            Box::new(Fruits2022(LegacyVersion::V2022)),
            Box::new(Mania2022(LegacyVersion::V2022)),
            Box::new(BaseOsu),
            Box::new(BaseTaiko),
            Box::new(BaseCatch),
            Box::new(BaseMania),
        ]
    })
}

fn base_performance_attributes(
    attributes: rosu_pp_older_base::any::PerformanceAttributes,
) -> LegacyPerformanceAttributes {
    use rosu_pp_older_base::any::PerformanceAttributes::*;

    match attributes {
        Osu(attrs) => LegacyPerformanceAttributes {
            pp: attrs.pp,
            pp_acc: Some(attrs.pp_acc).into(),
            pp_aim: Some(attrs.pp_aim).into(),
            pp_speed: Some(attrs.pp_speed).into(),
            pp_flashlight: Some(attrs.pp_flashlight).into(),
            effective_miss_count: Some(attrs.effective_miss_count).into(),
            speed_deviation: attrs.speed_deviation.into(),
            combo_based_estimated_miss_count: Some(attrs.combo_based_estimated_miss_count).into(),
            score_based_estimated_miss_count: attrs.score_based_estimated_miss_count.into(),
            aim_estimated_slider_breaks: Some(attrs.aim_estimated_slider_breaks).into(),
            speed_estimated_slider_breaks: Some(attrs.speed_estimated_slider_breaks).into(),
            ..Default::default()
        },
        Taiko(attrs) => LegacyPerformanceAttributes {
            pp: attrs.pp,
            pp_acc: Some(attrs.pp_acc).into(),
            pp_difficulty: Some(attrs.pp_difficulty).into(),
            estimated_unstable_rate: attrs.estimated_unstable_rate.into(),
            ..Default::default()
        },
        Catch(attrs) => LegacyPerformanceAttributes {
            pp: attrs.pp,
            ..Default::default()
        },
        Mania(attrs) => LegacyPerformanceAttributes {
            pp: attrs.pp,
            pp_difficulty: Some(attrs.pp_difficulty).into(),
            ..Default::default()
        },
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn calculates_difficulty_then_performance_for_every_registered_version() {
        let map = rosu_pp_older_base::Beatmap::from_bytes(include_bytes!(
            "../../../SharpRosuPP/RosuPP.Tests/resources/657916.osu"
        ))
        .unwrap();
        let difficulty = LegacyDifficulty::default();
        let performance = LegacyPerformance {
            accuracy: Some(100.0),
            ..Default::default()
        };

        for calculator in registry() {
            let attrs = calculator.difficulty(&map, &difficulty);
            let result = calculator.performance(&map, &attrs, &performance);
            assert_eq!(result.difficulty.mode, calculator.mode());
            assert!(result.difficulty.stars > 0.0);
            assert!(result.difficulty.max_combo > 0);
            assert!(attrs.stars() > 0.0, "{:?}", calculator.version());
            assert!(attrs.max_combo() > 0, "{:?}", calculator.version());
            assert!(result.pp > 0.0, "{:?}", calculator.version());

            match (calculator.version(), calculator.mode()) {
                (LegacyVersion::RosuPpOlderBase, Mode::Osu) => {
                    assert!(result.difficulty.aim_difficult_slider_count.is_some());
                    assert!(result.difficulty.aim_top_weighted_slider_factor.is_some());
                    assert!(result.difficulty.maximum_legacy_combo_score.is_some());
                    assert!(result.difficulty.n_large_ticks.is_some());
                }
                (LegacyVersion::RosuPpOlderBase, Mode::Taiko) => {
                    assert!(result.difficulty.reading.is_some());
                    assert!(result.difficulty.mechanical_difficulty.is_some());
                    assert!(result.difficulty.consistency_factor.is_some());
                }
                (LegacyVersion::RosuPpOlderBase, Mode::Catch) => {
                    assert!(result.difficulty.preempt.is_some());
                    assert!(result.difficulty.n_fruits.is_some());
                }
                (LegacyVersion::RosuPpOlderBase, Mode::Mania) => {
                    assert!(result.difficulty.n_objects.is_some());
                    assert!(result.difficulty.n_hold_notes.is_some());
                }
                (LegacyVersion::Osu2021November, Mode::Osu) => {
                    assert!(result.difficulty.flashlight.is_some());
                    assert!(result.difficulty.slider_factor.is_some());
                }
                (
                    LegacyVersion::Osu2014May
                    | LegacyVersion::Osu2014July
                    | LegacyVersion::Osu2015February
                    | LegacyVersion::Osu2015April
                    | LegacyVersion::Osu2018
                    | LegacyVersion::Osu2019
                    | LegacyVersion::Osu2021January
                    | LegacyVersion::Osu2021July,
                    Mode::Osu,
                ) => {
                    assert!(result.difficulty.aim.is_some());
                    assert!(result.difficulty.speed.is_some());
                    assert!(result.difficulty.ar.is_some());
                    assert!(result.difficulty.od.is_some());
                    assert!(result.difficulty.hp.is_some());
                    assert!(result.difficulty.n_circles.is_some());
                    assert!(result.difficulty.n_sliders.is_some());
                    assert!(result.difficulty.n_spinners.is_some());
                }
                (LegacyVersion::Osu2024, Mode::Osu) => {
                    assert!(result.difficulty.aim_difficult_strain_count.is_some());
                    assert!(result.difficulty.speed_difficult_strain_count.is_some());
                    assert!(result.difficulty.n_large_ticks.is_some());
                }
                (LegacyVersion::Osu2025, Mode::Osu) => {
                    assert!(result.difficulty.aim_difficult_slider_count.is_some());
                    assert!(result.difficulty.great_hit_window.is_some());
                    assert!(result.speed_deviation.is_some());
                }
                (LegacyVersion::Taiko2022, Mode::Taiko) => {
                    assert!(result.difficulty.peak.is_some());
                    assert!(result.difficulty.hit_window.is_some());
                    assert!(result.effective_miss_count.is_some());
                }
                (LegacyVersion::Taiko2024, Mode::Taiko) => {
                    assert!(result.difficulty.peak.is_some());
                    assert!(result.difficulty.mono_stamina_factor.is_some());
                    assert!(result.estimated_unstable_rate.is_some());
                }
                (LegacyVersion::Taiko2025, Mode::Taiko) => {
                    assert!(result.difficulty.reading.is_some());
                    assert!(result.difficulty.mono_stamina_factor.is_some());
                    assert!(result.estimated_unstable_rate.is_some());
                }
                (LegacyVersion::FruitsPpv1, Mode::Catch) => {
                    assert!(result.difficulty.preempt.is_some());
                    assert!(result.difficulty.n_fruits.is_some());
                }
                (LegacyVersion::Fruits2022 | LegacyVersion::Fruits2024, Mode::Catch) => {
                    assert!(result.difficulty.ar.is_some());
                    assert!(result.difficulty.n_fruits.is_some());
                    assert!(result.difficulty.is_convert.is_some());
                }
                (LegacyVersion::Mania2022, Mode::Mania) => {
                    assert!(result.difficulty.hit_window.is_some());
                    assert!(result.difficulty.n_objects.is_some());
                    assert!(result.difficulty.is_convert.is_some());
                }
                _ => {}
            }
        }

        let beatmap = LegacyBeatmap { inner: map };
        let mut unsupported = LegacyDifficulty::default();
        unsupported.set_mode(Mode::Catch);
        assert!(unsupported
            .calculate(&beatmap, LegacyVersion::Osu2014May)
            .is_none());
    }
}
