use crate::*;
use interoptopus::{
    ffi,
    ffi::{Option as FFIOption, String as FFIString},
};
use mode::Mode;
use rosu_mods::{
    generated_mods::UnknownMod,
    serde::{GameModSeed, GameModsSeed},
    Acronym, GameMod,
};
use serde::de::DeserializeSeed;

#[ffi(service)]
#[derive(Default)]
pub struct Mods {
    pub mods: rosu_mods::GameMods,
    pub mode: Option<Mode>,
}

// Regular implementation of methods.
#[ffi(prefix = "mods_")]
impl Mods {
    pub fn create(mode: Mode) -> ffi::Result<Self, FFIError> {
        ffi_result(Ok(Self {
            mods: rosu_mods::GameMods::new(),
            mode: Some(mode),
        }))
    }

    pub fn from_acronyms(str: FFIString, mode: Mode) -> ffi::Result<Self, FFIError> {
        ffi_result(Ok(Self {
            mods: rosu_mods::GameMods::from_intermode(
                &rosu_mods::GameModsIntermode::from_acronyms(str.as_str()),
                mode.into(),
            ),
            mode: Some(mode),
        }))
    }

    pub fn from_bits(bits: u32, mode: Mode) -> ffi::Result<Self, FFIError> {
        ffi_result(Ok(Self {
            mods: rosu_mods::GameMods::from_intermode(
                &rosu_mods::GameModsIntermode::from_bits(bits),
                mode.into(),
            ),
            mode: Some(mode),
        }))
    }

    pub fn from_json(
        str: FFIString,
        mode: Mode,
        deny_unknown_fields: bool,
    ) -> ffi::Result<Self, FFIError> {
        ffi_result((|| {
            let mut d = serde_json::Deserializer::from_str(str.as_str());
            let mods = GameModsSeed::Mode {
                mode: mode.into(),
                deny_unknown_fields,
            }
            .deserialize(&mut d)?;

            Ok(Self {
                mods,
                mode: Some(mode),
            })
        })())
    }

    pub fn remove_unknown_mods(&mut self) {
        self.mods = self
            .mods
            .clone()
            .into_iter()
            .filter(|m| m.kind() != UnknownMod::kind())
            .collect();
    }

    pub fn sanitize(&mut self) {
        self.mods.sanitize();
    }

    pub fn bits(&mut self) -> u32 {
        self.mods.bits()
    }

    pub fn len(&mut self) -> u32 {
        self.mods.len() as u32
    }

    pub fn json(&self) -> FFIString {
        serde_json::to_string_pretty(&self.mods).unwrap().into()
    }

    pub fn insert_json(&mut self, str: FFIString, deny_unknown_fields: bool) -> bool {
        let mut d = serde_json::Deserializer::from_str(str.as_str());
        let seed = if let Some(mode) = self.mode {
            GameModSeed::Mode {
                mode: mode.into(),
                deny_unknown_fields,
            }
        } else {
            GameModSeed::GuessMode {
                deny_unknown_fields,
            }
        };
        if let Ok(m) = seed.deserialize(&mut d) {
            self.mods.insert(m);
            return true;
        }

        false
    }

    pub fn insert(&mut self, str: FFIString) {
        self.mods.insert(GameMod::new(
            str.as_str(),
            self.mode.unwrap_or_default().into(),
        ));
    }

    pub fn contains(&self, str: FFIString) -> bool {
        str.as_str()
            .parse::<Acronym>()
            .is_ok_and(|m| self.mods.contains_acronym(m))
    }

    pub fn clear(&mut self) {
        self.mods = rosu_mods::GameMods::new();
    }

    pub fn clock_rate(&mut self) -> FFIOption<f64> {
        self.mods.clock_rate().into()
    }
}
