use crate::beatmap::Beatmap;
use crate::*;
use interoptopus::{
    ffi_service, ffi_service_ctor, ffi_service_method, ffi_type,
    patterns::{option::FFIOption, string::AsciiPointer},
};
use mods::Mods;
use rosu_mods::{GameModsIntermode, GameMods};

#[ffi_type(opaque)]
#[derive(Default)]
#[allow(non_snake_case)]
pub struct Difficulty {
    pub mods: FFIOption<GameMods>,
    pub mods_intermode: FFIOption<GameModsIntermode>,
    pub passed_objects: FFIOption<u32>,
    /// Clock rate will be clamped internally between 0.01 and 100.0.
    ///
    /// Since its minimum value is 0.01, its bits are never zero.
    /// Additionally, values between 0.01 and 100 are represented sufficiently
    /// precise with 32 bits.
    ///
    /// This allows for an optimization to reduce the struct size by storing its
    /// bits as a [`NonZeroU32`].
    pub clock_rate: FFIOption<f64>,
    pub ar: FFIOption<f32>,
    pub cs: FFIOption<f32>,
    pub hp: FFIOption<f32>,
    pub od: FFIOption<f32>,

    pub hardrock_offsets: FFIOption<bool>,
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
        self.mods = Some(mods.mods.clone()).into();
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn i_mods(&mut self, mods: u32) {
        self.mods_intermode = Some(GameModsIntermode::from_bits(mods)).into();
    }

    #[ffi_service_method(on_panic = "ffi_error")]
    pub fn s_mods(&mut self, str: AsciiPointer) -> Result<(), Error> {
        self.mods_intermode = Some(GameModsIntermode::from_acronyms(
            str.as_str().map_err(|_e| Error::InvalidString(None))?,
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
    pub fn hardrock_offsets(&mut self, hardrock_offsets: bool) {
        self.hardrock_offsets = Some(hardrock_offsets).into();
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn calculate(&self, beatmap: *const Beatmap) -> attributes::DifficultyAttributes {
        let beatmap = unsafe {
            beatmap
                .as_ref()
                .unwrap_or_else(|| panic!("beatmap: {beatmap:?}"))
        };

        self.construct().calculate(&beatmap.inner).into()
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn get_clock_rate(&mut self) -> f64 {
        if let Some(mods) = self.mods.as_ref() {
            return f64::from(mods.clock_rate().unwrap_or(1.0))
        }
        
        if let Some(mods_intermode) = self.mods_intermode.as_ref() {
            return f64::from(mods_intermode.legacy_clock_rate())
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
        } = self;

        if let Some(mods) = mods.as_ref() {
            diff = diff.mods(mods.bits());
        } else if let Some(mods_intermode) = mods_intermode.as_ref() {
            diff = diff.mods(mods_intermode.bits());
        }

        if let Some(passed_objects) = passed_objects.into_option() {
            diff = diff.passed_objects(passed_objects);
        }

        if let Some(clock_rate) = clock_rate.into_option() {
            diff = diff.clock_rate(clock_rate);
        }

        if let Some(ar) = ar.into_option() {
            diff = diff.ar(ar, false);
        }

        if let Some(cs) = cs.into_option() {
            diff = diff.cs(cs, false);
        }

        if let Some(hp) = hp.into_option() {
            diff = diff.hp(hp, false);
        }

        if let Some(od) = od.into_option() {
            diff = diff.od(od, false);
        }

        if let Some(hardrock_offsets) = hardrock_offsets.into_option() {
            diff = diff.hardrock_offsets(hardrock_offsets);
        }

        diff
    }
}
