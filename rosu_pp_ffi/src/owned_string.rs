use std::{ffi::CString, mem::MaybeUninit};

use crate::*;
use interoptopus::{
    ffi_service, ffi_type,
    ffi::CStrPtr,
    pattern::result::{Result, result_to_ffi}
};

#[ffi_type(opaque)]
pub struct OwnedString {
    pub inner: MaybeUninit<CString>,
    pub is_init: bool
}

// Regular implementation of methods.
#[ffi_service(prefix = "string_")]
impl OwnedString {
    pub fn from_c_str(str: CStrPtr) -> Result<Self, Error> {
        result_to_ffi(|| {
        Ok(Self {
            inner: MaybeUninit::new(str.as_c_str().ok_or(Error::Null)?.to_owned()),
            is_init: true
        })
        })
    }

    pub fn empty() -> Result<Self, Error> {
        Result::Ok(Self {
            inner: MaybeUninit::uninit(),
            is_init: false
        })
    }

    pub fn is_init(&self) -> bool {
       self.is_init
    }

    pub fn to_cstr(&self) -> CStrPtr<'_> {
        CStrPtr::from_cstr(unsafe { self.inner.assume_init_ref() })
    }
}

impl OwnedString {
    pub fn replace(&mut self, str: String) {
        if self.is_init { unsafe { self.inner.assume_init_drop(); } }
        self.inner.write(CString::new(str).unwrap());
        self.is_init = true;
    }
}

impl Drop for OwnedString {
    fn drop(&mut self) {
        if self.is_init { unsafe { self.inner.assume_init_drop(); } }
    }
}