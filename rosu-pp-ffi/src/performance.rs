use crate::*;
use attributes::DifficultyAttributes;
use beatmap::Beatmap;
use hitresult_priority::HitResultPriority;
use interoptopus::{
    ffi_service, ffi_service_ctor, ffi_service_method, ffi_type,
    patterns::{option::FFIOption, primitives::FFIBool, string::AsciiPointer},
};
use mode::Mode;
use mods::Mods;
use rosu_mods::{GameMods, GameModsIntermode};
use state::ScoreState;

#[ffi_type(opaque)]
#[repr(C)]
#[derive(Clone, Default, PartialEq)]
#[allow(non_snake_case)]
pub struct Performance {
    pub mode: FFIOption<Mode>,
    pub mods: FFIOption<GameMods>,
    pub mods_intermode: FFIOption<GameModsIntermode>,
    pub passed_objects: FFIOption<u32>,
    pub clock_rate: FFIOption<f64>,
    pub ar: FFIOption<f32>,
    pub cs: FFIOption<f32>,
    pub hp: FFIOption<f32>,
    pub od: FFIOption<f32>,
    pub hardrock_offsets: FFIOption<FFIBool>,
    pub lazer: FFIOption<FFIBool>,

    pub accuracy: FFIOption<f64>,
    pub misses: FFIOption<u32>,
    pub combo: FFIOption<u32>,
    pub hitresult_priority: FFIOption<HitResultPriority>,

    pub slider_tick_hits: FFIOption<u32>,
    pub slider_end_hits: FFIOption<u32>,
    pub n300: FFIOption<u32>,
    pub n100: FFIOption<u32>,
    pub n50: FFIOption<u32>,
    pub n_katu: FFIOption<u32>,
    pub n_geki: FFIOption<u32>,
    pub state: FFIOption<ScoreState>
}

// Regular implementation of methods.
#[ffi_service(error = "FFIError", prefix = "performance_")]
impl Performance {
    #[ffi_service_ctor]
    pub fn new() -> Result<Self, Error> {
        Ok(Self::default())
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn mode(&mut self, mode: Mode) {
        self.mode = Some(mode).into();
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn p_mods(&mut self, mods: &Mods) {
        self.mods = Some(mods.mods.clone()).into();
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn i_mods(&mut self, mods: u32) {
        self.mods_intermode = Some(GameModsIntermode::from_bits(mods)).into();
    }

    pub fn s_mods(&mut self, str: AsciiPointer) -> Result<(), Error> {
        self.mods_intermode = Some(GameModsIntermode::from_acronyms(
            str.as_str()?,
        ))
        .into();
        Ok(())
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn passed_objects(&mut self, passed_objects: u32) {
        self.passed_objects = Some(passed_objects).into();
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn clock_rate(&mut self, clock_rate: f64) {
        self.clock_rate = Some(clock_rate).into();
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn ar(&mut self, ar: f32) {
        self.ar = Some(ar).into();
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn cs(&mut self, cs: f32) {
        self.cs = Some(cs).into();
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn hp(&mut self, hp: f32) {
        self.hp = Some(hp).into();
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn od(&mut self, od: f32) {
        self.od = Some(od).into();
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn hardrock_offsets(&mut self, hardrock_offsets: FFIBool) {
        self.hardrock_offsets = Some(hardrock_offsets).into();
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn state(&mut self, state: ScoreState) {
        self.state = Some(state).into();
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn accuracy(&mut self, accuracy: f64) {
        self.accuracy = Some(accuracy).into();
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn misses(&mut self, misses: u32) {
        self.misses = Some(misses).into();
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn combo(&mut self, combo: u32) {
        self.combo = Some(combo).into();
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn hitresult_priority(&mut self, hitresult_priority: HitResultPriority) {
        self.hitresult_priority = Some(hitresult_priority).into();
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn lazer(&mut self, lazer: FFIBool) {
        self.lazer = Some(lazer).into();
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn slider_tick_hits(&mut self, slider_tick_hits: u32) {
        self.slider_tick_hits = Some(slider_tick_hits).into();
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn slider_end_hits(&mut self, slider_end_hits: u32) {
        self.slider_end_hits = Some(slider_end_hits).into();
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn n300(&mut self, n300: u32) {
        self.n300 = Some(n300).into();
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn n100(&mut self, n100: u32) {
        self.n100 = Some(n100).into();
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn n50(&mut self, n50: u32) {
        self.n50 = Some(n50).into();
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn n_katu(&mut self, n_katu: u32) {
        self.n_katu = Some(n_katu).into();
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn n_geki(&mut self, n_geki: u32) {
        self.n_geki = Some(n_geki).into();
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn generate_state(&self, beatmap: &Beatmap) -> state::ScoreState {
        let mut performance = self.apply(rosu_pp::Performance::new(&beatmap.inner));
        performance.generate_state().into()
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn generate_state_from_difficulty(
        &self,
        difficulty_attr: DifficultyAttributes,
    ) -> state::ScoreState {
        let mut performance = self.apply(rosu_pp::Performance::new(
            rosu_pp::any::DifficultyAttributes::from(difficulty_attr),
        ));
        performance.generate_state().into()
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn calculate(&self, beatmap: &Beatmap) -> attributes::PerformanceAttributes {
        let performance = self.apply(rosu_pp::Performance::new(&beatmap.inner));
        performance.calculate().into()
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn calculate_from_difficulty(
        &self,
        difficulty_attr: DifficultyAttributes,
    ) -> attributes::PerformanceAttributes {
        let performance = self.apply(rosu_pp::Performance::new(
            rosu_pp::any::DifficultyAttributes::from(difficulty_attr),
        ));
        performance.calculate().into()
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn get_clock_rate(&mut self) -> f64 {
        if let Some(mods) = self.mods.as_ref() {
            return mods.clock_rate().unwrap_or(1.0);
        }

        if let Some(mods_intermode) = self.mods_intermode.as_ref() {
            return mods_intermode.legacy_clock_rate();
        }

        1.0
    }
}

impl Performance {
    pub fn apply<'a>(&self, mut perf: rosu_pp::Performance<'a>) -> rosu_pp::Performance<'a> {
        let Performance {
            mode,
            mods,
            mods_intermode,
            passed_objects,
            clock_rate,
            ar,
            cs,
            hp,
            od,
            hardrock_offsets,
            accuracy,
            misses,
            combo,
            hitresult_priority,
            lazer,
            slider_tick_hits,
            slider_end_hits,
            n300,
            n100,
            n50,
            n_katu,
            n_geki,
            state
        } = self;

        if let Some(mode) = mode.into_option() {
            perf = perf.mode_or_ignore(mode.into());
        }

        if let Some(mods) = mods.as_ref() {
            perf = perf.mods(mods.clone());
        } else if let Some(mods_intermode) = mods_intermode.as_ref() {
            perf = perf.mods(mods_intermode);
        }

        if let Some(passed_objects) = passed_objects.into_option() {
            perf = perf.passed_objects(passed_objects);
        }

        if let Some(clock_rate) = clock_rate.into_option() {
            perf = perf.clock_rate(clock_rate);
        }

        if let Some(ar) = ar.into_option() {
            perf = perf.ar(ar, false);
        }

        if let Some(cs) = cs.into_option() {
            perf = perf.cs(cs, false);
        }

        if let Some(hp) = hp.into_option() {
            perf = perf.hp(hp, false);
        }

        if let Some(od) = od.into_option() {
            perf = perf.od(od, false);
        }

        if let Some(hardrock_offsets) = hardrock_offsets.into_option() {
            perf = perf.hardrock_offsets(hardrock_offsets.is());
        }

        if let Some(state) = state.into_option() {
            perf = perf.state(state.into());
        }

        if let Some(accuracy) = accuracy.into_option() {
            perf = perf.accuracy(accuracy);
        }

        if let Some(misses) = misses.into_option() {
            perf = perf.misses(misses);
        }

        if let Some(combo) = combo.into_option() {
            perf = perf.combo(combo);
        }

        if let Some(hitresult_priority) = hitresult_priority.into_option() {
            perf = perf.hitresult_priority(hitresult_priority.into());
        }

        if let Some(lazer) = lazer.into_option() {
            perf = perf.lazer(lazer.is());
        }

        if let Some(slider_tick_hits) = slider_tick_hits.into_option() {
            perf = if let rosu_pp::Performance::Osu(o) = perf {
                rosu_pp::Performance::Osu(o.n_large_ticks(slider_tick_hits))
            } else {
                perf
            };
        }

        if let Some(slider_end_hits) = slider_end_hits.into_option() {
            perf = if let rosu_pp::Performance::Osu(o) = perf {
                rosu_pp::Performance::Osu(o.n_slider_ends(slider_end_hits))
            } else {
                perf
            };
        }

        if let Some(n300) = n300.into_option() {
            perf = perf.n300(n300);
        }

        if let Some(n100) = n100.into_option() {
            perf = perf.n100(n100);
        }

        if let Some(n50) = n50.into_option() {
            perf = perf.n50(n50);
        }

        if let Some(n_katu) = n_katu.into_option() {
            perf = perf.n_katu(n_katu);
        }

        if let Some(n_geki) = n_geki.into_option() {
            perf = perf.n_geki(n_geki);
        }

        perf
    }
}
