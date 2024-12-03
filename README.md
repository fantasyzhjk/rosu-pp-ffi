# rosu-pp-ffi

**rosu-pp-ffi** is a Foreign Function Interface (FFI) implementation for the [rosu-pp](https://github.com/MaxOhn/rosu-pp) library. It provides an efficient way to integrate osu! performance points calculation into other programming languages.

## Features

- Access to rosu-pp's performance points calculation methods via FFI.
- Support for integration with multiple languages.
- Simple and lightweight design for cross-platform compatibility.

## Getting Started

### Prerequisites

- Rust toolchain (for building the FFI library). Install it via [rustup](https://rustup.rs/).
- A C-compatible compiler for your platform.

### Usage

Clone and Build the library:
```bash
git clone https://github.com/fantasyzhjk/rosu-pp-ffi.git
cd rosu-pp-ffi
cargo build --release
```

Link the resulting library to your project according to your programming language’s FFI guidelines.

For detailed usage examples, refer to the official [rosu-pp documentation](https://github.com/MaxOhn/rosu-pp) and language-specific bindings.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request to suggest improvements or add new features.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
