use interoptopus::{Error, Interop};

#[test]
#[cfg_attr(miri, ignore)]
fn bindings_c() -> Result<(), Error> {
    use interoptopus_backend_c::{Config, Generator};

    Generator::new(
        Config {
            ifndef: "sb_pp".to_string(),
            ..Config::default()
        },
        sb_pp_ffi::ffi_inventory(),
    )
    .write_file("bindings/bindings.h")?;

    Ok(())
}
