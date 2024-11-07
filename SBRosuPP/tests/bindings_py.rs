use interoptopus::{Error, Interop};

#[test]
#[cfg_attr(miri, ignore)]
fn bindings_cpython_cffi() -> Result<(), Error> {
    use interoptopus_backend_cpython::{Config, Generator};

    let library = sb_pp_ffi::ffi_inventory();
    Generator::new(Config::default(), library).write_file("bindings/bindings.py")?;

    Ok(())
}