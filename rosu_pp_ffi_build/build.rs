use std::error::Error;
use std::path::Path;

use interoptopus_csharp::dispatch::Dispatch;
use interoptopus_csharp::output::Target;
use interoptopus_csharp::RustLibrary;

mod c_header;

fn main() -> Result<(), Box<dyn Error>> {
    let workspace = Path::new(env!("CARGO_MANIFEST_DIR"))
        .parent()
        .ok_or("binding crate must be located inside the workspace")?;

    let java_binding = workspace.join("JavaRosuPP/src/main/java/desu/life/RosuFFI.java");
    println!("cargo:rerun-if-changed={}", java_binding.display());

    bindings_csharp(workspace.join("SharpRosuPP/RosuPP/RosuFFI.cs"))?;
    bindings_csharp(workspace.join("bindings/RosuFFI.cs"))?;
    c_header::write(
        &rosu_pp_ffi::ffi_inventory(),
        workspace.join("bindings/RosuFFI.h"),
    )?;
    sync_java_binding(java_binding, workspace.join("bindings/RosuFFI.java"))?;

    // Interoptopus 0.16 ships a suspended, empty C backend. The local header
    // writer consumes the same inventory as the C# generator.
    println!("cargo:warning=C header generated from the Interoptopus 0.16 inventory");
    println!("cargo:warning=Java JNA binding synchronized from JavaRosuPP");

    Ok(())
}

fn sync_java_binding(
    source: impl AsRef<Path>,
    target: impl AsRef<Path>,
) -> Result<(), Box<dyn Error>> {
    let source = std::fs::read_to_string(source)?;
    let normalized = source
        .lines()
        .map(str::trim_end)
        .collect::<Vec<_>>()
        .join("\n")
        + "\n";

    std::fs::write(target, normalized)?;

    Ok(())
}

fn bindings_csharp(file_name: impl AsRef<Path>) -> Result<(), Box<dyn Error>> {
    let file_name = file_name.as_ref();
    let output_name = file_name
        .file_name()
        .and_then(|name| name.to_str())
        .ok_or("binding path must end in a valid UTF-8 file name")?
        .to_owned();
    let dispatch_name = output_name.clone();

    let output = RustLibrary::builder(rosu_pp_ffi::ffi_inventory())
        .dll_name("rosu_pp_ffi")
        .dispatch(Dispatch::custom(move |_, _| {
            Target::new(&dispatch_name, "RosuPP")
        }))
        .build()
        .process()?;
    let generated = output
        .buffer(&output_name)
        .ok_or("C# generator did not produce the requested output file")?;
    let normalized = generated
        .lines()
        .map(str::trim_end)
        .collect::<Vec<_>>()
        .join("\n")
        + "\n";

    std::fs::write(file_name, normalized)?;

    Ok(())
}
