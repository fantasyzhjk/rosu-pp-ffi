use crate::mods::Mods;
use crate::*;
use beatmap::Beatmap;
use interoptopus::{
    ffi,
    ffi::{Option as FFIOption, String as FFIString},
};
use mode::Mode;
use rosu_mods::{GameMods, GameModsIntermode};

/// Summary struct for a [`Beatmap`]'s attributes.
#[derive(Clone, Debug, PartialEq)]
#[repr(C)]
#[ffi]
pub struct BeatmapAttributes {
    /// The approach rate.
    pub ar: f64,
    /// The overall difficulty.
    pub od: f64,
    /// The circle size.
    pub cs: f32,
    /// The health drain rate
    pub hp: f32,
    /// The clock rate with respect to mods.
    pub clock_rate: f64,
    /// The hit windows for approach rate and overall difficulty.
    pub hit_windows: HitWindows,
}

impl From<rosu_pp::model::beatmap::BeatmapAttributes> for BeatmapAttributes {
    fn from(attributes: rosu_pp::model::beatmap::BeatmapAttributes) -> Self {
        let ajustedbeatmaptrributes = attributes.apply_clock_rate();
        Self {
            ar: ajustedbeatmaptrributes.ar,
            od: ajustedbeatmaptrributes.od,
            cs: ajustedbeatmaptrributes.cs,
            hp: ajustedbeatmaptrributes.hp,
            clock_rate: attributes.clock_rate(),
            hit_windows: attributes.hit_windows().into(),
        }
    }
}

/// AR and OD hit windows
#[derive(Copy, Clone, Debug, PartialEq)]
#[repr(C)]
#[ffi]
pub struct HitWindows {
    /// Hit window for approach rate i.e. `TimePreempt` in milliseconds.
    pub ar: FFIOption<f64>,
    /// Hit window for overall difficulty i.e. time to hit a "Perfect" in milliseconds.
    pub od_perfect: FFIOption<f64>,
    /// Hit window for overall difficulty i.e. time to hit a 300 ("Great") in milliseconds.
    pub od_great: FFIOption<f64>,
    /// Hit window for overall difficulty i.e. time to hit a "Good" in milliseconds.
    pub od_good: FFIOption<f64>,
    /// Hit window for overall difficulty i.e. time to hit a 100 ("Ok") in milliseconds.
    pub od_ok: FFIOption<f64>,
    /// Hit window for overall difficulty i.e. time to hit a 50 ("Meh") in milliseconds.
    pub od_meh: FFIOption<f64>,
}

impl From<rosu_pp::model::beatmap::HitWindows> for HitWindows {
    fn from(attributes: rosu_pp::model::beatmap::HitWindows) -> Self {
        Self {
            ar: attributes.ar.into(),
            od_perfect: attributes.od_perfect.into(),
            od_great: attributes.od_great.into(),
            od_good: attributes.od_good.into(),
            od_ok: attributes.od_ok.into(),
            od_meh: attributes.od_meh.into(),
        }
    }
}

#[ffi(service)]
#[derive(Default)]
#[allow(non_snake_case)]
pub struct BeatmapAttributesBuilder {
    pub mode: Option<Mode>,
    pub mods: Option<GameMods>,
    pub mods_intermode: Option<GameModsIntermode>,
    pub clock_rate: Option<f64>,
    pub ar: Option<f32>,
    pub cs: Option<f32>,
    pub hp: Option<f32>,
    pub od: Option<f32>,
}

// Regular implementation of methods.
#[ffi]
impl BeatmapAttributesBuilder {
    pub fn create() -> ffi::Result<Self, FFIError> {
        ffi_result(Ok(Self::default()))
    }

    pub fn mode(&mut self, mode: Mode) {
        self.mode = Some(mode);
    }

    pub fn p_mods(&mut self, mods: &Mods) {
        self.mods = Some(mods.mods.clone());
    }

    pub fn i_mods(&mut self, mods: u32) {
        self.mods_intermode = Some(GameModsIntermode::from_bits(mods));
    }

    pub fn s_mods(&mut self, str: FFIString) {
        self.mods_intermode = Some(GameModsIntermode::from_acronyms(str.as_str()));
    }

    pub fn clock_rate(&mut self, clock_rate: f64) {
        self.clock_rate = Some(clock_rate);
    }

    pub fn ar(&mut self, ar: f32) {
        self.ar = Some(ar);
    }

    pub fn cs(&mut self, cs: f32) {
        self.cs = Some(cs);
    }

    pub fn hp(&mut self, hp: f32) {
        self.hp = Some(hp);
    }

    pub fn od(&mut self, od: f32) {
        self.od = Some(od);
    }

    pub fn get_clock_rate(&mut self) -> f64 {
        if let Some(mods) = self.mods.as_ref() {
            return mods.clock_rate().unwrap_or(1.0);
        }

        if let Some(mods_intermode) = self.mods_intermode.as_ref() {
            return mods_intermode.legacy_clock_rate();
        }

        1.0
    }

    pub fn build(&self, beatmap: &Beatmap) -> BeatmapAttributes {
        let mut builder_binding = rosu_pp::model::beatmap::BeatmapAttributesBuilder::new();
        let mut builder = builder_binding.map(&beatmap.inner);
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

        if let Some(mode) = *mode {
            builder = builder.mode(mode.into(), beatmap.inner.is_convert);
        }

        if let Some(mods) = mods {
            builder = builder.mods(mods.clone());
        } else if let Some(mods_intermode) = mods_intermode {
            builder = builder.mods(mods_intermode);
        }

        if let Some(clock_rate) = *clock_rate {
            builder = builder.clock_rate(clock_rate);
        }

        if let Some(ar) = *ar {
            builder = builder.ar(ar, false);
        }

        if let Some(cs) = *cs {
            builder = builder.cs(cs, false);
        }

        if let Some(hp) = *hp {
            builder = builder.hp(hp, false);
        }

        if let Some(od) = *od {
            builder = builder.od(od, false);
        }

        builder.build().into()
    }
}
