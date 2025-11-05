use crate::*;
use interoptopus::{
    ffi_service, ffi_type,
    pattern::option::Option as FFIOption,
    ffi::CStrPtr,
    pattern::result::{Result, result_to_ffi}
};
use mode::Mode;
use owned_string::OwnedString;
use rosu_mods::{generated_mods::UnknownMod, serde::{GameModSeed, GameModsSeed}, Acronym, GameMod};
use serde::de::DeserializeSeed;

#[ffi_type(opaque)]
#[derive(Default)]
pub struct Mods {
    pub mods: rosu_mods::GameMods,
    pub mode: Option<Mode>,
}

// Regular implementation of methods.
#[ffi_service(prefix = "mods_")]
impl Mods {
    
    pub fn new(mode: Mode) -> Result<Self, Error> {
        Result::Ok(Self {
            mods: rosu_mods::GameMods::new(),
            mode: Some(mode)
        })
    }

    
    pub fn from_acronyms(str: CStrPtr, mode: Mode) -> Result<Self, Error> {
        result_to_ffi(|| {
            Ok(Self {
                mods: rosu_mods::GameMods::from_intermode(&rosu_mods::GameModsIntermode::from_acronyms(
                    str.as_str()?,
                ), mode.into()),
                mode: Some(mode)
            })
        })
    }

    
    pub fn from_bits(bits: u32, mode: Mode) -> Result<Self, Error> {
        Result::Ok(Self {
            mods: rosu_mods::GameMods::from_intermode(&rosu_mods::GameModsIntermode::from_bits(bits), mode.into()),
            mode: Some(mode)
        })
    }


    
    pub fn from_json(str: CStrPtr, mode: Mode, deny_unknown_fields: bool) -> Result<Self, Error> {
        result_to_ffi(|| {  
            let s = str.as_str()?;
            let mut d = serde_json::Deserializer::from_str(s);
            let mods = GameModsSeed::Mode { mode: mode.into(), deny_unknown_fields }.deserialize(&mut d)?;
            Ok(Self {
                mods,
                mode: Some(mode)
            })
        })
    }
    
    
    pub fn remove_unknown_mods(&mut self) {
        self.mods = self.mods.clone().into_iter().filter(|m| m.kind() != UnknownMod::kind()).collect();
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

    
    pub fn json(&mut self, str: &mut OwnedString) {
        str.replace(serde_json::to_string_pretty(&self.mods).unwrap())
    }

    
    pub fn insert_json(&mut self, str: CStrPtr, deny_unknown_fields: bool) -> bool {
        if let Ok(s) = str.as_str() {
            let mut d = serde_json::Deserializer::from_str(s);
            let s = if let Some(mode) = self.mode { GameModSeed::Mode { mode: mode.into(), deny_unknown_fields } } else { GameModSeed::GuessMode { deny_unknown_fields } };
            if let Ok(m) = s.deserialize(&mut d) {
                self.mods.insert(m);
                return true;
            }
        }
        false
    }

    
    pub fn insert(&mut self, str: CStrPtr) -> bool {
        if let Ok(s) = str.as_str() {
            self.mods.insert(GameMod::new(s, self.mode.unwrap_or_default().into()));
            return true;
        }
        false
    }

    
    pub fn contains(&mut self, str: CStrPtr) -> bool {
        if let Ok(s) = str.as_str() {
            if let Ok(m) = s.parse::<Acronym>(){
                return self.mods.contains_acronym(m);
            }
        }
        false
    }

    
    pub fn clear(&mut self) {
        self.mods = rosu_mods::GameMods::new();
    }

    
    pub fn clock_rate(&mut self) -> FFIOption<f64> {
        self.mods.clock_rate().into()
    }
}
