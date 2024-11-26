use interoptopus::util::NamespaceMappings;
use interoptopus::{Error, Interop};
use interoptopus_backend_csharp::{ParamSliceType, Unsafe};

#[test]
#[cfg_attr(miri, ignore)]
fn bindings_csharp() -> Result<(), Error> {
    use interoptopus_backend_csharp::{Config, Generator};

    Generator::new(
        Config {
            class: "Rosu".to_string(),
            dll_name: "rosu_pp_ffi".to_string(),
            namespace_mappings: NamespaceMappings::new("RosuPP"),
            use_unsafe: Unsafe::UnsafePlatformMemCpy,
            param_slice_type: ParamSliceType::Array,
            ..Config::default()
        },
        rosu_pp_ffi::ffi_inventory(),
    )
    .write_file("./bindings/bindings.cs")?;

    Ok(())
}
