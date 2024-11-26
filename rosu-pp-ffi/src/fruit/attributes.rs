use interoptopus::{ffi_type, patterns::primitives::FFIBool};

/// The result of a difficulty calculation on an osu!catch map.
#[derive(Clone, Copy, Debug, Default, PartialEq)]
#[repr(C)]
#[ffi_type]
pub struct CatchDifficultyAttributes {
    /// The final star rating
    pub stars: f64,
    /// The approach rate.
    pub ar: f64,
    /// The amount of fruits.
    pub n_fruits: u32,
    /// The amount of droplets.
    pub n_droplets: u32,
    /// The amount of tiny droplets.
    pub n_tiny_droplets: u32,
    /// Whether the [`Beatmap`] was a convert i.e. an osu!standard map.
    ///
    /// [`Beatmap`]: crate::model::beatmap::Beatmap
    pub is_convert: FFIBool,
}

impl CatchDifficultyAttributes {
    /// Return the maximum combo.
    pub const fn max_combo(&self) -> u32 {
        self.n_fruits + self.n_droplets
    }

    /// Whether the [`Beatmap`] was a convert i.e. an osu!standard map.
    ///
    /// [`Beatmap`]: crate::model::beatmap::Beatmap
    pub fn is_convert(&self) -> bool {
        self.is_convert.is()
    }
}

impl From<rosu_pp::catch::CatchDifficultyAttributes> for CatchDifficultyAttributes {
    fn from(attributes: rosu_pp::catch::CatchDifficultyAttributes) -> Self {
        Self {
            stars: attributes.stars,
            ar: attributes.ar,
            n_fruits: attributes.n_fruits,
            n_droplets: attributes.n_droplets,
            n_tiny_droplets: attributes.n_tiny_droplets,
            is_convert: attributes.is_convert.into(),
        }
    }
}

impl From<CatchDifficultyAttributes> for rosu_pp::catch::CatchDifficultyAttributes {
    fn from(attributes: CatchDifficultyAttributes) -> Self {
        Self {
            stars: attributes.stars,
            ar: attributes.ar,
            n_fruits: attributes.n_fruits,
            n_droplets: attributes.n_droplets,
            n_tiny_droplets: attributes.n_tiny_droplets,
            is_convert: attributes.is_convert.is(),
        }
    }
}

/// The result of a performance calculation on an osu!catch map.
#[derive(Clone, Debug, Default, PartialEq)]
#[repr(C)]
#[ffi_type]
pub struct CatchPerformanceAttributes {
    /// The difficulty attributes that were used for the performance calculation
    pub difficulty: CatchDifficultyAttributes,
    /// The final performance points.
    pub pp: f64,
}

impl CatchPerformanceAttributes {
    /// Return the star value.
    pub const fn stars(&self) -> f64 {
        self.difficulty.stars
    }

    /// Return the performance point value.
    pub const fn pp(&self) -> f64 {
        self.pp
    }

    /// Return the maximum combo of the map.
    pub const fn max_combo(&self) -> u32 {
        self.difficulty.max_combo()
    }

    /// Whether the [`Beatmap`] was a convert i.e. an osu!standard map.
    ///
    /// [`Beatmap`]: crate::model::beatmap::Beatmap
    pub fn is_convert(&self) -> bool {
        self.difficulty.is_convert.is()
    }
}

impl From<rosu_pp::catch::CatchPerformanceAttributes> for CatchPerformanceAttributes {
    fn from(attributes: rosu_pp::catch::CatchPerformanceAttributes) -> Self {
        Self {
            difficulty: attributes.difficulty.into(),
            pp: attributes.pp,
        }
    }
}

impl From<CatchPerformanceAttributes> for rosu_pp::catch::CatchPerformanceAttributes {
    fn from(attributes: CatchPerformanceAttributes) -> Self {
        Self {
            difficulty: attributes.difficulty.into(),
            pp: attributes.pp,
        }
    }
}
