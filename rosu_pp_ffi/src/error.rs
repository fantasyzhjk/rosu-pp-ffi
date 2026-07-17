use interoptopus::ffi;

// This file may look complex but the Interoptopus parts are actually really simple,
// with some Rust best practices making up most of the code.

// This is the FFI error enum you want your users to see. You are free to name and implement this
// almost any way you want.
#[ffi]
#[repr(C)]
#[derive(Debug, Default, Copy, Clone, PartialEq, Eq)]
pub enum FFIError {
    #[default]
    Ok = 0,
    Null = 100,
    Panic = 200,
    IoError = 300,
    SerializeError = 600,
    ConvertError = 700,
    Unknown = 1000,
}

use thiserror::Error;
#[derive(Error, Debug, Default)]
pub enum Error {
    #[error("UnknownError")]
    #[default]
    Unknown,
    #[error("ParseError")]
    IO(#[from] std::io::Error),
    #[error("SerializeError")]
    Serialize(#[from] serde_json::Error),
    #[error("ConvertError")]
    Convert(#[from] rosu_pp::model::mode::ConvertError),
}

/// Provide a mapping how your Rust error enums translate
/// to your FFI error enums.
impl From<Error> for FFIError {
    fn from(x: Error) -> Self {
        match x {
            Error::Unknown => Self::Unknown,
            Error::IO(_) => Self::IoError,
            Error::Serialize(_) => Self::SerializeError,
            Error::Convert(_) => Self::ConvertError,
        }
    }
}
