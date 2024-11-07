use interoptopus::util::NamespaceMappings;
use interoptopus::{Error, Interop};

#[test]
#[cfg_attr(miri, ignore)]
fn bindings_csharp() -> Result<(), Error> {
    use interoptopus_backend_csharp::{Config, Generator};

    Generator::new(
        Config {
            class: "SBRosu".to_string(),
            dll_name: "sb_pp_ffi".to_string(),
            namespace_mappings: NamespaceMappings::new("SBRosuPP"),
            ..Config::default()
        },
        sb_pp_ffi::ffi_inventory(),
    )
    .write_file("./bindings/bindings.cs")?;

    Ok(())
}
