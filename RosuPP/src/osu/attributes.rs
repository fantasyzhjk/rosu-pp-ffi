use interoptopus::ffi_type;

/// The result of a difficulty calculation on an osu!standard map.
#[derive(Clone, Debug, Default, PartialEq)]
#[repr(C)]
#[ffi_type]
pub struct OsuDifficultyAttributes {
    /// The difficulty of the aim skill.
    pub aim: f64,
    /// The difficulty of the speed skill.
    pub speed: f64,
    /// The difficulty of the flashlight skill.
    pub flashlight: f64,
    /// The ratio of the aim strain with and without considering sliders
    pub slider_factor: f64,
    /// The number of clickable objects weighted by difficulty.
    pub speed_note_count: f64,
    /// Weighted sum of aim strains.
    pub aim_difficult_strain_count: f64,
    /// Weighted sum of speed strains.
    pub speed_difficult_strain_count: f64,
    /// The approach rate.
    pub ar: f64,
    /// The overall difficulty
    pub od: f64,
    /// The health drain rate.
    pub hp: f64,
    /// The amount of circles.
    pub n_circles: u32,
    /// The amount of sliders.
    pub n_sliders: u32,
    /// The amount of slider ticks and repeat points.
    pub n_slider_ticks: u32,
    /// The amount of spinners.
    pub n_spinners: u32,
    /// The final star rating
    pub stars: f64,
    /// The maximum combo.
    pub max_combo: u32,
}

impl OsuDifficultyAttributes {
    /// Return the maximum combo.
    pub const fn max_combo(&self) -> u32 {
        self.max_combo
    }

    /// Return the amount of hitobjects.
    pub const fn n_objects(&self) -> u32 {
        self.n_circles + self.n_sliders + self.n_spinners
    }
}

impl From<rosu_pp::osu::OsuDifficultyAttributes> for OsuDifficultyAttributes {
    fn from(attributes: rosu_pp::osu::OsuDifficultyAttributes) -> Self {
        Self {
            aim: attributes.aim,
            speed: attributes.speed,
            flashlight: attributes.flashlight,
            slider_factor: attributes.slider_factor,
            speed_note_count: attributes.speed_note_count,
            aim_difficult_strain_count: 0.0,
            speed_difficult_strain_count: 0.0,
            ar: attributes.ar,
            od: attributes.od,
            hp: attributes.hp,
            n_circles: attributes.n_circles,
            n_sliders: attributes.n_sliders,
            n_slider_ticks: 0,
            n_spinners: attributes.n_spinners,
            stars: attributes.stars,
            max_combo: attributes.max_combo,
        }
    }
}

impl From<OsuDifficultyAttributes> for rosu_pp::osu::OsuDifficultyAttributes {
    fn from(attributes: OsuDifficultyAttributes) -> Self {
        Self {
            aim: attributes.aim,
            speed: attributes.speed,
            flashlight: attributes.flashlight,
            slider_factor: attributes.slider_factor,
            speed_note_count: attributes.speed_note_count,
            ar: attributes.ar,
            od: attributes.od,
            hp: attributes.hp,
            n_circles: attributes.n_circles,
            n_sliders: attributes.n_sliders,
            n_spinners: attributes.n_spinners,
            stars: attributes.stars,
            max_combo: attributes.max_combo,
        }
    }
}

/// The result of a performance calculation on an osu!standard map.
#[derive(Clone, Debug, Default, PartialEq)]
#[repr(C)]
#[ffi_type]
pub struct OsuPerformanceAttributes {
    /// The difficulty attributes that were used for the performance calculation
    pub difficulty: OsuDifficultyAttributes,
    /// The final performance points.
    pub pp: f64,
    /// The accuracy portion of the final pp.
    pub pp_acc: f64,
    /// The aim portion of the final pp.
    pub pp_aim: f64,
    /// The flashlight portion of the final pp.
    pub pp_flashlight: f64,
    /// The speed portion of the final pp.
    pub pp_speed: f64,
    /// Misses including an approximated amount of slider breaks
    pub effective_miss_count: f64,
}

impl OsuPerformanceAttributes {
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
    /// Return the amount of hitobjects.
    pub const fn n_objects(&self) -> u32 {
        self.difficulty.n_objects()
    }
}

impl From<rosu_pp::osu::OsuPerformanceAttributes> for OsuPerformanceAttributes {
    fn from(attributes: rosu_pp::osu::OsuPerformanceAttributes) -> Self {
        Self {
            difficulty: attributes.difficulty.into(),
            pp: attributes.pp,
            pp_acc: attributes.pp_acc,
            pp_aim: attributes.pp_aim,
            pp_flashlight: attributes.pp_flashlight,
            pp_speed: attributes.pp_speed,
            effective_miss_count: attributes.effective_miss_count,
        }
    }
}

impl From<OsuPerformanceAttributes> for rosu_pp::osu::OsuPerformanceAttributes {
    fn from(attributes: OsuPerformanceAttributes) -> Self {
        Self {
            difficulty: attributes.difficulty.into(),
            pp: attributes.pp,
            pp_acc: attributes.pp_acc,
            pp_aim: attributes.pp_aim,
            pp_flashlight: attributes.pp_flashlight,
            pp_speed: attributes.pp_speed,
            effective_miss_count: attributes.effective_miss_count,
        }
    }
}
