use crate::mods::Mods;
use crate::*;
use beatmap::Beatmap;
use interoptopus::{
    ffi_service, ffi_service_ctor, ffi_service_method, ffi_type,
    patterns::{option::FFIOption, string::AsciiPointer},
};
use mode::Mode;
use rosu_mods::{GameMods, GameModsIntermode};

/// Summary struct for a [`Beatmap`]'s attributes.
#[derive(Clone, Debug, PartialEq)]
#[repr(C)]
#[ffi_type]
pub struct BeatmapAttributes {
    /// The approach rate.
    pub ar: f64,
    /// The overall difficulty.
    pub od: f64,
    /// The circle size.
    pub cs: f64,
    /// The health drain rate
    pub hp: f64,
    /// The clock rate with respect to mods.
    pub clock_rate: f64,
    /// The hit windows for approach rate and overall difficulty.
    pub hit_windows: HitWindows,
}

impl From<rosu_pp::model::beatmap::BeatmapAttributes> for BeatmapAttributes {
    fn from(attributes: rosu_pp::model::beatmap::BeatmapAttributes) -> Self {
        Self {
            ar: attributes.ar,
            od: attributes.od,
            cs: attributes.cs,
            hp: attributes.hp,
            clock_rate: attributes.clock_rate,
            hit_windows: attributes.hit_windows.into(),
        }
    }
}

/// AR and OD hit windows
#[derive(Copy, Clone, Debug, PartialEq)]
#[repr(C)]
#[ffi_type]
pub struct HitWindows {
    /// Hit window for approach rate i.e. `TimePreempt` in milliseconds.
    pub ar: f64,
    /// Hit window for overall difficulty i.e. time to hit a 300 ("Great") in milliseconds.
    pub od_great: f64,
    /// Hit window for overall difficulty i.e. time to hit a 100 ("Ok") in milliseconds.
    ///
    /// `None` for osu!mania.
    pub od_ok: FFIOption<f64>,
}

impl From<rosu_pp::model::beatmap::HitWindows> for HitWindows {
    fn from(attributes: rosu_pp::model::beatmap::HitWindows) -> Self {
        Self {
            ar: attributes.ar,
            od_great: attributes.od,
            od_ok: None.into(),
        }
    }
}

#[ffi_type(opaque)]
#[derive(Default)]
#[allow(non_snake_case)]
pub struct BeatmapAttributesBuilder {
    pub mode: FFIOption<Mode>,
    pub mods: FFIOption<GameMods>,
    pub mods_intermode: FFIOption<GameModsIntermode>,
    pub clock_rate: FFIOption<f64>,
    pub ar: FFIOption<f32>,
    pub cs: FFIOption<f32>,
    pub hp: FFIOption<f32>,
    pub od: FFIOption<f32>,
}

// Regular implementation of methods.
#[ffi_service(error = "FFIError", prefix = "beatmap_attributes_")]
impl BeatmapAttributesBuilder {
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

    #[ffi_service_method(on_panic = "ffi_error")]
    pub fn s_mods(&mut self, str: AsciiPointer) -> Result<(), Error> {
        self.mods_intermode = Some(GameModsIntermode::from_acronyms(
            str.as_str().map_err(|_e| Error::InvalidString(None))?,
        ))
        .into();
        Ok(())
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
    pub fn get_clock_rate(&mut self) -> f64 {
        if let Some(mods) = self.mods.as_ref() {
            return f64::from(mods.clock_rate().unwrap_or(1.0))
        }
        
        if let Some(mods_intermode) = self.mods_intermode.as_ref() {
            return f64::from(mods_intermode.legacy_clock_rate())
        }

        1.0
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn build(&self, beatmap: *const Beatmap) -> BeatmapAttributes {
        let beatmap = unsafe {
            beatmap
                .as_ref()
                .unwrap_or_else(|| panic!("beatmap: {beatmap:?}"))
        };

        let mut builder = rosu_pp::model::beatmap::BeatmapAttributesBuilder::new().map(&beatmap.inner);
        let BeatmapAttributesBuilder {
            mode,
            mods,
            mods_intermode,
            clock_rate,
            ar,
            cs,
            hp,
            od,
        } = self;

        if let Some(mode) = mode.into_option() {
            builder = builder.mode(mode.into(), beatmap.inner.is_convert);
        }

        if let Some(mods) = mods.as_ref() {
            builder = builder.mods(mods.clone());
        } else if let Some(mods_intermode) = mods_intermode.as_ref() {
            builder = builder.mods(mods_intermode);
        }

        if let Some(clock_rate) = clock_rate.into_option() {
            builder = builder.clock_rate(clock_rate);
        }

        if let Some(ar) = ar.into_option() {
            builder = builder.ar(ar, false);
        }

        if let Some(cs) = cs.into_option() {
            builder = builder.cs(cs, false);
        }

        if let Some(hp) = hp.into_option() {
            builder = builder.hp(hp, false);
        }

        if let Some(od) = od.into_option() {
            builder = builder.od(od, false);
        }

        builder.build().into()
    }
}
