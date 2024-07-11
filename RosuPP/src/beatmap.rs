use crate::*;
use interoptopus::{
    ffi_service, ffi_service_ctor, ffi_type, ffi_service_method,
    patterns::{slice::FFISlice, string::AsciiPointer},
};

#[ffi_type(opaque)]
#[derive(Default)]
pub struct Beatmap {
    pub inner: rosu_pp::Beatmap,
}

// Regular implementation of methods.
#[ffi_service(error = "FFIError", prefix = "beatmap_")]
impl Beatmap {
    #[ffi_service_ctor]
    pub fn from_bytes(data: FFISlice<u8>) -> Result<Self, Error> {
        Ok(Self {
            inner: rosu_pp::Beatmap::from_bytes(data.as_slice())?,
        })
    }

    #[ffi_service_ctor]
    pub fn from_path(path: AsciiPointer) -> Result<Self, Error> {
        Ok(Self {
            inner: rosu_pp::Beatmap::from_path(
                path.as_str().map_err(|_e| Error::InvalidString(None))?,
            )?,
        })
    }

    /// Convert a Beatmap to the specified mode
    #[ffi_service_method(on_panic = "undefined_behavior")]
    pub fn convert(&mut self, mode: Mode) -> bool {
        self.inner.convert_in_place(mode.into()).success()
    }
}
