use interoptopus::util::NamespaceMappings;
use interoptopus::{Error, Interop};

#[test]
#[cfg_attr(miri, ignore)]
fn bindings_csharp() -> Result<(), Error> {
    use interoptopus_backend_csharp::{Config, Generator};

    Generator::new(
        Config {
            class: "Rosu".to_string(),
            dll_name: "rosu_cs".to_string(),
            namespace_mappings: NamespaceMappings::new("RosuPP"),
            ..Config::default()
        },
        rosu_cs::my_inventory(),
    )
    .write_file("./bindings/Interop.cs")?;

    Ok(())
}

// #[test]
// #[cfg_attr(miri, ignore)]
// fn bindings_c() -> Result<(), Error> {
//     use interoptopus_backend_c::{Config, Generator};

//     Generator::new(
//         Config {
//             ifndef: "example_hello_world".to_string(),
//             ..Config::default()
//         },
//         example_hello_world::my_inventory(),
//     )
//     .write_file("bindings/c/example_complex.h")?;

//     Ok(())
// }

// #[test]
// #[cfg_attr(miri, ignore)]
// fn bindings_cpython_cffi() -> Result<(), Error> {
//     use interoptopus_backend_cpython::{Config, Generator};

//     let library = example_hello_world::my_inventory();
//     Generator::new(Config::default(), library).write_file("bindings/python/example_complex.py")?;

//     Ok(())
// }