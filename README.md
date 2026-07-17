# rosu-pp-ffi

**rosu-pp-ffi** is a Foreign Function Interface (FFI) implementation for the [rosu-pp](https://github.com/MaxOhn/rosu-pp) library. It provides an efficient way to integrate osu! performance points calculation into other programming languages.

## Features

- Access to rosu-pp's performance points calculation methods via FFI.
- First-class C# bindings generated with Interoptopus 0.16.3.
- Java 22 FFM bindings generated with jextract and exposed through a
  lifecycle-safe Java facade.
- Simple and lightweight design for cross-platform compatibility.

## Getting Started

### Prerequisites

- Rust 1.93 or newer (required by Interoptopus 0.16.3). Install it via [rustup](https://rustup.rs/).
- A C-compatible compiler for your platform.

### Usage

Clone and Build the library:

```bash
git clone https://github.com/fantasyzhjk/rosu-pp-ffi.git
cd rosu-pp-ffi
cargo build --release
```

Link the resulting library to your project according to your programming language’s FFI guidelines.

### C# Usage

To use this library in a C# project, you can add it as a Git submodule and reference the `RosuPP.csproj` directly in your `.csproj` file:

1. Add the repository as a Git submodule:

    ```bash
    git submodule add https://github.com/fantasyzhjk/rosu-pp-ffi.git
    git submodule update --init --recursive
    ```

2. In your .csproj file, add the following reference to include the library as a dependency:

    ```xml
    <ItemGroup>
        <ProjectReference Include="./rosu-pp-ffi/SharpRosuPP/RosuPP/RosuPP.csproj" />
    </ItemGroup>
    ```

For detailed usage examples, refer to the official [rosu-pp documentation](https://docs.rs/rosu-pp/) and language-specific bindings.

Interoptopus 0.16 features used by the C# API include:

- Payload enums for difficulty, performance, and hit-object variants. Use generated members such as `IsOsu` / `AsOsu()` and `IsSlider` / `AsSlider()`.
- `Wire<Vec<HitObject>>` for bulk hit-object transfer. Dispose the wire after calling `Unwire()`.
- Owned UTF-8 strings at the native boundary, with regular C# `string` overloads provided by `Rosu.cs`.
- Services for stateful native objects such as beatmaps, calculators, mods, builders, and gradual calculation.

The Java binding exposes the same payload-enum, owned UTF-8 string, wire, and
service concepts. The public facade is
`JavaRosuPP/src/main/java/desu/life/RosuFFI.java`; running
`rosu_pp_ffi_build` synchronizes it to `bindings/RosuFFI.java`. Set the
`rosu.pp.ffi.library` system property to override the native library path.
Packaged JARs otherwise select and extract the matching native library from
`native/<rid>/` automatically, falling back to the platform library search path
when no packaged resource is available.
Applications should enable native access for the binding module, or use
`--enable-native-access=ALL-UNNAMED` when running from the class path.
Native service and wire instances implement `AutoCloseable` and should be used
with try-with-resources. Individual service and wire instances are not safe for
concurrent use.

The current C header is generated from `ffi_inventory()` by
`rosu_pp_ffi_build`, rather than being a legacy checked-in ABI description.
Run `JavaRosuPP/generate-ffm-bindings.sh` with `jextract` available to regenerate
the Java 22 FFM raw layer under `desu.life.raw`. This generated layer is kept
separate from the public facade so memory ownership and service lifetimes stay
explicit.

### Binding backend status

Interoptopus 0.16 currently provides a functional C# generator. Its published C
and CPython crates are placeholders and are marked as suspended upstream, so
this repository contains a small inventory-driven C header writer. The header
feeds `jextract`; `rosu_pp_ffi_build` also generates C# and synchronizes the
maintained Java facade.

Any legacy Python artifact from Interoptopus 0.14 is not ABI-compatible with
the current 0.16 native library.

## Learn More

- [rosu-pp](https://github.com/MaxOhn/rosu-pp)
- [interoptopus](https://github.com/ralfbiedert/interoptopus)

## Contributing

Contributions are welcome! Please open an issue or submit a pull request to suggest improvements or add new features.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
