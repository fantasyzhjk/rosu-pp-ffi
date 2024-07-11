use interoptopus::ffi_type;

/// The result of a difficulty calculation on an osu!taiko map.
#[derive(Clone, Debug, Default, PartialEq)]
#[repr(C)]
#[ffi_type]
pub struct TaikoDifficultyAttributes {
    /// The difficulty of the stamina skill.
    pub stamina: f64,
    /// The difficulty of the rhythm skill.
    pub rhythm: f64,
    /// The difficulty of the color skill.
    pub color: f64,
    /// The difficulty of the hardest parts of the map.
    pub peak: f64,
    /// The perceived hit window for an n300 inclusive of rate-adjusting mods (DT/HT/etc)
    pub hit_window: f64,
    /// The final star rating.
    pub stars: f64,
    /// The maximum combo.
    pub max_combo: u32,
    /// Whether the [`Beatmap`] was a convert i.e. an osu!standard map.
    ///
    /// [`Beatmap`]: crate::model::beatmap::Beatmap
    pub is_convert: bool,
}

impl TaikoDifficultyAttributes {
    /// Return the maximum combo.
    pub const fn max_combo(&self) -> u32 {
        self.max_combo
    }

    /// Whether the [`Beatmap`] was a convert i.e. an osu!standard map.
    ///
    /// [`Beatmap`]: crate::model::beatmap::Beatmap
    pub const fn is_convert(&self) -> bool {
        self.is_convert
    }
}

impl From<rosu_pp::taiko::TaikoDifficultyAttributes> for TaikoDifficultyAttributes {
    fn from(attributes: rosu_pp::taiko::TaikoDifficultyAttributes) -> Self {
        Self {
            stamina: attributes.stamina,
            rhythm: attributes.rhythm,
            color: attributes.color,
            peak: attributes.peak,
            hit_window: attributes.hit_window,
            stars: attributes.stars,
            max_combo: attributes.max_combo,
            is_convert: attributes.is_convert,
        }
    }
}

impl From<TaikoDifficultyAttributes> for rosu_pp::taiko::TaikoDifficultyAttributes {
    fn from(attributes: TaikoDifficultyAttributes) -> Self {
        Self {
            stamina: attributes.stamina,
            rhythm: attributes.rhythm,
            color: attributes.color,
            peak: attributes.peak,
            hit_window: attributes.hit_window,
            stars: attributes.stars,
            max_combo: attributes.max_combo,
            is_convert: attributes.is_convert,
        }
    }
}

/// The result of a performance calculation on an osu!taiko map.
#[derive(Clone, Debug, Default, PartialEq)]
#[repr(C)]
#[ffi_type]
pub struct TaikoPerformanceAttributes {
    /// The difficulty attributes that were used for the performance calculation
    pub difficulty: TaikoDifficultyAttributes,
    /// The final performance points.
    pub pp: f64,
    /// The accuracy portion of the final pp.
    pub pp_acc: f64,
    /// The strain portion of the final pp.
    pub pp_difficulty: f64,
    /// Scaled miss count based on total hits.
    pub effective_miss_count: f64,
}

impl TaikoPerformanceAttributes {
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
        self.difficulty.max_combo
    }

    /// Whether the [`Beatmap`] was a convert i.e. an osu!standard map.
    ///
    /// [`Beatmap`]: crate::model::beatmap::Beatmap
    pub const fn is_convert(&self) -> bool {
        self.difficulty.is_convert
    }
}

impl From<rosu_pp::taiko::TaikoPerformanceAttributes> for TaikoPerformanceAttributes {
    fn from(attributes: rosu_pp::taiko::TaikoPerformanceAttributes) -> Self {
        Self {
            difficulty: attributes.difficulty.into(),
            pp: attributes.pp,
            pp_acc: attributes.pp_acc,
            pp_difficulty: attributes.pp_difficulty,
            effective_miss_count: attributes.effective_miss_count,

        }
    }
}

impl From<TaikoPerformanceAttributes> for rosu_pp::taiko::TaikoPerformanceAttributes {
    fn from(attributes: TaikoPerformanceAttributes) -> Self {
        Self {
            difficulty: attributes.difficulty.into(),
            pp: attributes.pp,
            pp_acc: attributes.pp_acc,
            pp_difficulty: attributes.pp_difficulty,
            effective_miss_count: attributes.effective_miss_count,

        }
    }
}
