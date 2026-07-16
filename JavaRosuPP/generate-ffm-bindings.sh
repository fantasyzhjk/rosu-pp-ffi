#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
output="$root/JavaRosuPP/src/main/java/desu/life/raw"

cargo build --manifest-path "$root/Cargo.toml" -p rosu_pp_ffi_build
rm -rf "$output"

jextract \
  --output "$root/JavaRosuPP/src/main/java" \
  --target-package desu.life.raw \
  --header-class-name RosuNative \
  --library rosu_pp_ffi \
  "$root/bindings/RosuFFI.h"

# jextract 25 emits SymbolLookup.findOrThrow, which was added after Java 22.
# Keep the generated binding on the first stable FFM release for compatibility.
perl -pi -e 's/SYMBOL_LOOKUP\.findOrThrow\(("[^"]+")\)/SYMBOL_LOOKUP.find($1).orElseThrow()/g' \
  "$output/RosuNative.java"
