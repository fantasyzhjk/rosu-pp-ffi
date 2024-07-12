use crate::*;
use interoptopus::{
    ffi_service, ffi_service_ctor, ffi_service_method, ffi_type,
    patterns::string::AsciiPointer,
};
use rosu_mods::Acronym;

#[ffi_type(opaque)]
#[derive(Default)]
pub struct Mods {
    pub inner: rosu_mods::GameModsIntermode,
}

// Regular implementation of methods.
#[ffi_service(error = "FFIError", prefix = "mods_")]
impl Mods {
    #[ffi_service_ctor]
    pub fn from_acronyms(str: AsciiPointer) -> Result<Self, Error> {
        Ok(Self {
            inner: rosu_mods::GameModsIntermode::from_acronyms(
                str.as_str().map_err(|_e| Error::InvalidString(None))?,
            ),
        })
    }

    #[ffi_service_ctor]
    pub fn from_bits(bits: u32) -> Result<Self, Error> {
        Ok(Self {
            inner: rosu_mods::GameModsIntermode::from_bits(bits),
        })
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn bits(&mut self) -> u32 {
        self.inner.bits()
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn is_empty(&mut self) -> bool {
        self.inner.is_empty()
    }

    #[ffi_service_method(on_panic = "return_default")]
    pub fn contains(&mut self, str: AsciiPointer) -> bool {
        self.inner
            .intersects(&rosu_mods::GameModsIntermode::from_acronyms(
                str.as_str().unwrap(),
            ))
    }

    #[ffi_service_method(on_panic = "return_default")]
    pub fn intersects(&mut self, str: AsciiPointer) -> bool {
        self.inner
            .contains_acronym(str.as_str().unwrap().parse::<Acronym>().unwrap())
    }

    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn legacy_clock_rate(&mut self) -> f32 {
        self.inner.legacy_clock_rate()
    }
}
