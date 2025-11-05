use std::path::Path;
use std::error::Error;

use interoptopus::lang::NamespaceMappings;

// By adding the interop generation logic into a `build.rs` that depends on
// our `core_library_ffi` we ensure that upon `cargo build` both the `.dll`
// gets built, as well as the `.cs` files.
//
// Instead, if you used to unit test trick in the other examples, you will have
// to run both `cargo build` to produce the `.dll` and `cargo test`
// to produce the bindings (since `cargo test` does not imply `cargo build`).
fn main() {
    // to c# project
    bindings_csharp("../SharpRosuPP/RosuPP/RosuFFI.cs").unwrap();

    // to bindings
    bindings_csharp("../bindings/RosuFFI.cs").unwrap();
    bindings_c("../bindings/RosuFFI.h").unwrap();
    bindings_python("../bindings/RosuFFI.py").unwrap();
}

fn bindings_csharp(file_name: impl AsRef<Path>) -> Result<(), Box<dyn Error>> {
    use interoptopus_backend_csharp::Interop;

    Interop::builder()
        .inventory(rosu_pp_ffi::ffi_inventory())
        .dll_name("rosu_pp_ffi")
        .namespace_mappings(NamespaceMappings::new("RosuPP"))
        .build()?
        .write_file(file_name)?;

    Ok(())
}

fn bindings_c(file_name: impl AsRef<Path>) -> Result<(), Box<dyn Error>> {
    use interoptopus_backend_c::Interop;

    Interop::builder()
        .inventory(rosu_pp_ffi::ffi_inventory())
        .ifndef("rosu_pp".to_string())
        .build()?
        .write_file(file_name)?;

    Ok(())
}

fn bindings_python(file_name: impl AsRef<Path>) -> Result<(), Box<dyn Error>> {
    use interoptopus_backend_cpython::Interop;

    Interop::builder()
        .inventory(rosu_pp_ffi::ffi_inventory())
        .build()?
        .write_file(file_name)?;

    Ok(())
}