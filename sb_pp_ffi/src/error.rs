use interoptopus::ffi_type;

// This file may look complex but the Interoptopus parts are actually really simple,
// with some Rust best practices making up most of the code.

// This is the FFI error enum you want your users to see. You are free to name and implement this
// almost any way you want.
#[ffi_type(patterns(ffi_error))]
#[repr(C)]
pub enum FFIError {
    Ok = 0,
    Null = 100,
    Panic = 200,
    IoError = 300,
    Utf8Error = 400,
    InvalidString = 500,
    SerializeError = 600,
    ConvertError = 700,
    Unknown = 1000
}

// Implement Default so we know what the "good" case is.
impl Default for FFIError {
    fn default() -> Self {
        Self::Ok
    }
}

// Implement Interoptopus' `FFIError` trait for your FFIError enum.
// Here you must map 3 "well known" variants to your enum.
impl interoptopus::patterns::result::FFIError for FFIError {
    const SUCCESS: Self = Self::Ok;
    const NULL: Self = Self::Null;
    const PANIC: Self = Self::Panic;
}


use thiserror::Error;
#[derive(Error, Debug)]
pub enum Error {
    #[error("UnknownError")]
    Unknown,
    #[error("NullPointer")]
    Null,
    #[error("ParseError")]
    IO(#[from] std::io::Error),
    #[error("InvalidCString")]
    InvalidString,
    #[error("Utf8Error")]
    UTF8(#[from] std::str::Utf8Error),
    #[error("SerializeError")]
    Serialize(#[from] serde_json::Error),
    #[error("ConvertError")]
    Convert(#[from] rosu_pp::model::mode::ConvertError),

}

impl Default for Error {
    fn default() -> Self {
        Self::Unknown
    }
}

/// Provide a mapping how your Rust error enums translate
/// to your FFI error enums.
impl From<Error> for FFIError {
    fn from(x: Error) -> Self {
        match x {
            Error::Unknown => Self::Unknown,
            Error::Null => Self::Null,
            Error::IO(_) => Self::IoError,
            Error::InvalidString => Self::InvalidString,
            Error::UTF8(_) => Self::Utf8Error,
            Error::Serialize(_) => Self::SerializeError,
            Error::Convert(_) => Self::ConvertError
        }
    }
}

impl From<interoptopus::Error> for Error {
    fn from(x: interoptopus::Error) -> Self {
        match x {
            interoptopus::Error::Null => Self::Null,
            interoptopus::Error::Ascii => Self::InvalidString,
            interoptopus::Error::Format(_) => Self::InvalidString,
            interoptopus::Error::IO(e) => Self::IO(e),
            interoptopus::Error::UTF8(e) => Self::UTF8(e),
            interoptopus::Error::FromUtf8(e) => Self::UTF8(e.utf8_error()),
            _ => Self::Unknown
        }
    }
}