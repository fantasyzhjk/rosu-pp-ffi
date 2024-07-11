use crate::*;
use attributes::DifficultyAttributes;
use beatmap::Beatmap;
use interoptopus::{
    ffi_service, ffi_service_ctor, ffi_service_method, ffi_type,
    patterns::option::FFIOption,
};

#[ffi_type(opaque)]
#[repr(C)]
#[derive(Clone, Default, PartialEq)]
#[allow(non_snake_case)]
pub struct Performance {
    pub mode: FFIOption<Mode>,
    pub mods: FFIOption<u32>,
    pub passed_objects: FFIOption<u32>,
    pub clock_rate: FFIOption<f64>,
    pub ar: FFIOption<f32>,
    pub cs: FFIOption<f32>,
    pub hp: FFIOption<f32>,
    pub od: FFIOption<f32>,
    pub hardrock_offsets: FFIOption<bool>,
    
    pub accuracy: FFIOption<f64>,
    pub misses: FFIOption<u32>,
    pub combo: FFIOption<u32>,
    // todo: pub hitresult_priority: some_enum
    
    pub n300: FFIOption<u32>,
    pub n100: FFIOption<u32>,
    pub n50: FFIOption<u32>,
    pub n_katu: FFIOption<u32>,
    pub n_geki: FFIOption<u32>,
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
    pub fn mods(&mut self, mods: u32) {
        self.mods = Some(mods).into();
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
    pub fn generate_state(&self, beatmap: *const Beatmap) -> state::ScoreState {
        let beatmap = unsafe {
            beatmap.as_ref().unwrap_or_else(|| {
                panic!("beatmap: {beatmap:?}")
            })
        };
        
        let mut performance = self.apply(rosu_pp::Performance::new(&beatmap.inner));
        performance.generate_state().into()
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn calculate(&self, beatmap: *const Beatmap) -> attributes::PerformanceAttributes {
        let beatmap = unsafe {
            beatmap.as_ref().unwrap_or_else(|| {
                panic!("beatmap: {beatmap:?}")
            })
        };
        
        let performance = self.apply(rosu_pp::Performance::new(&beatmap.inner));
        performance.calculate().into()
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn calculate_from_difficulty(&self, difficulty_attr: DifficultyAttributes) -> attributes::PerformanceAttributes {
        let performance = self.apply(rosu_pp::Performance::new(rosu_pp::any::DifficultyAttributes::from(difficulty_attr)));
        performance.calculate().into()
    }


}

impl Performance {
    pub fn apply<'a>(&self, mut perf: rosu_pp::Performance<'a>) -> rosu_pp::Performance<'a> {
        let Performance {
            mode,
            mods,
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
            n300,
            n100,
            n50,
            n_katu,
            n_geki,
        } = self;

        if let Some(mode) = mode.into_option() {
            perf = perf.mode_or_ignore(mode.into());
        }

        if let Some(mods) = mods.into_option() {
            perf = perf.mods(mods);
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
            perf = perf.hardrock_offsets(hardrock_offsets);
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
