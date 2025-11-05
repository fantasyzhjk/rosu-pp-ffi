use interoptopus::ffi_type;
use thiserror::Error;

#[derive(Error, Debug)]
#[ffi_type]
pub enum Error {
    #[error("UnknownError")]
    Unknown,
    #[error("NullPointer")]
    Null,
    #[error("ParseError")]
    IO,
    #[error("InvalidCString")]
    InvalidString,
    #[error("Utf8Error")]
    UTF8,
    #[error("SerializeError")]
    Serialize,
    #[error("ConvertError")]
    Convert,
}

impl Default for Error {
    fn default() -> Self {
        Self::Unknown
    }
}

impl From<interoptopus::Error> for Error {
    fn from(x: interoptopus::Error) -> Self {
        match x {
            interoptopus::Error::Null => Self::Null,
            interoptopus::Error::NulTerminated => Self::InvalidString,
            interoptopus::Error::Format(_) => Self::InvalidString,
            interoptopus::Error::Utf8(_) => Self::UTF8,
            interoptopus::Error::FromUtf8(_) => Self::UTF8,
        }
    }
}

impl From<std::io::Error> for Error {
    fn from(_: std::io::Error) -> Self {
        Error::IO
    }
}

impl From<std::str::Utf8Error> for Error {
    fn from(_: std::str::Utf8Error) -> Self {
        Error::UTF8
    }
}

impl From<serde_json::Error> for Error {
    fn from(_: serde_json::Error) -> Self {
        Error::Serialize
    }
}

impl From<rosu_pp::model::mode::ConvertError> for Error {
    fn from(_: rosu_pp::model::mode::ConvertError) -> Self {
        Error::Convert
    }
}