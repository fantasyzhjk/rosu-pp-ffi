use crate::beatmap::Beatmap;
use crate::*;
use interoptopus::{
    ffi_service, ffi_service_ctor, ffi_service_method, ffi_type,
    patterns::{primitives::FFIBool, string::AsciiPointer},
};
use mods::Mods;
use rosu_mods::{GameModsIntermode, GameMods};

#[ffi_type(opaque)]
#[derive(Default)]
#[allow(non_snake_case)]
pub struct Difficulty {
    pub mods: Option<GameMods>,
    pub mods_intermode: Option<GameModsIntermode>,
    pub passed_objects: Option<u32>,
    /// Clock rate will be clamped internally between 0.01 and 100.0.
    ///
    /// Since its minimum value is 0.01, its bits are never zero.
    /// Additionally, values between 0.01 and 100 are represented sufficiently
    /// precise with 32 bits.
    ///
    /// This allows for an optimization to reduce the struct size by storing its
    /// bits as a [`NonZeroU32`].
    pub clock_rate: Option<f64>,
    pub ar: Option<f32>,
    pub cs: Option<f32>,
    pub hp: Option<f32>,
    pub od: Option<f32>,

    pub hardrock_offsets: Option<bool>,
    pub lazer: Option<bool>,
}

// Regular implementation of methods.
#[ffi_service(error = "FFIError", prefix = "difficulty_")]
impl Difficulty {
    #[ffi_service_ctor]
    pub fn new() -> Result<Self, Error> {
        Ok(Self::default())
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn p_mods(&mut self, mods: &Mods) {
        self.mods = Some(mods.mods.clone());
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn i_mods(&mut self, mods: u32) {
        self.mods_intermode = Some(GameModsIntermode::from_bits(mods));
    }

    #[ffi_service_method(on_panic = "ffi_error")]
    pub fn s_mods(&mut self, str: AsciiPointer) -> Result<(), Error> {
        self.mods_intermode = Some(GameModsIntermode::from_acronyms(
            str.as_str()?,
        ));
        Ok(())
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn passed_objects(&mut self, passed_objects: u32) {
        self.passed_objects = Some(passed_objects);
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn clock_rate(&mut self, clock_rate: f64) {
        self.clock_rate = Some(clock_rate);
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn ar(&mut self, ar: f32) {
        self.ar = Some(ar);
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn cs(&mut self, cs: f32) {
        self.cs = Some(cs);
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn hp(&mut self, hp: f32) {
        self.hp = Some(hp);
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn od(&mut self, od: f32) {
        self.od = Some(od);
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn hardrock_offsets(&mut self, hardrock_offsets: FFIBool) {
        self.hardrock_offsets = Some(hardrock_offsets.is());
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn lazer(&mut self, lazer: FFIBool) {
        self.lazer = Some(lazer.is());
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn calculate(&self, beatmap: &Beatmap) -> attributes::DifficultyAttributes {
        self.construct().calculate(&beatmap.inner).into()
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn get_clock_rate(&mut self) -> f64 {
        if let Some(mods) = self.mods.as_ref() {
            return mods.clock_rate().unwrap_or(1.0)
        }
        
        if let Some(mods_intermode) = self.mods_intermode.as_ref() {
            return mods_intermode.legacy_clock_rate()
        }

        1.0
    }
}

impl Difficulty {
    pub fn construct(&self) -> rosu_pp::Difficulty {
        let mut diff = rosu_pp::Difficulty::new();

        let Difficulty {
            mods,
            mods_intermode,
            passed_objects,
            clock_rate,
            ar,
            cs,
            hp,
            od,
            hardrock_offsets,
            lazer
        } = self;

        if let Some(mods) = mods {
            diff = diff.mods(mods.clone());
        } else if let Some(mods_intermode) = mods_intermode {
            diff = diff.mods(mods_intermode);
        }

        if let Some(passed_objects) = *passed_objects {
            diff = diff.passed_objects(passed_objects);
        }

        if let Some(clock_rate) = *clock_rate {
            diff = diff.clock_rate(clock_rate);
        }

        if let Some(ar) = *ar {
            diff = diff.ar(ar, false);
        }

        if let Some(cs) = *cs {
            diff = diff.cs(cs, false);
        }

        if let Some(hp) = *hp {
            diff = diff.hp(hp, false);
        }

        if let Some(od) = *od {
            diff = diff.od(od, false);
        }

        if let Some(hardrock_offsets) = *hardrock_offsets {
            diff = diff.hardrock_offsets(hardrock_offsets);
        }

        if let Some(lazer) = *lazer {
            diff = diff.lazer(lazer);
        }

        diff
    }
}
