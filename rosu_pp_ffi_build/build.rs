use std::path::Path;

use interoptopus::util::NamespaceMappings;
use interoptopus::{Error, Interop};

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

fn bindings_csharp(file_name: impl AsRef<Path>) -> Result<(), Error> {
    use interoptopus_backend_csharp::{Config, Generator, Unsafe};
    use interoptopus_backend_csharp::overloads::DotNet;

    Generator::new(
        Config {
            class: "RosuLibrary".to_string(),
            dll_name: "rosu_pp_ffi".to_string(),
            namespace_mappings: NamespaceMappings::new("RosuPP"),
            use_unsafe: Unsafe::UnsafePlatformMemCpy,
            ..Config::default()
        },
        rosu_pp_ffi::ffi_inventory(),
    )
    .add_overload_writer(DotNet::new())
    .write_file(file_name)?;

    Ok(())
}

fn bindings_c(file_name: impl AsRef<Path>) -> Result<(), Error> {
    use interoptopus_backend_c::{Config, Generator};

    Generator::new(
        Config {
            ifndef: "rosu_pp".to_string(),
            ..Config::default()
        },
        rosu_pp_ffi::ffi_inventory(),
    )
    .write_file(file_name)?;

    Ok(())
}

fn bindings_python(file_name: impl AsRef<Path>) -> Result<(), Error> {
    use interoptopus_backend_cpython::{Config, Generator};

    let library = rosu_pp_ffi::ffi_inventory();
    Generator::new(Config::default(), library).write_file(file_name)?;

    Ok(())
}