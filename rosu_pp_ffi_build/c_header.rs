use interoptopus::inventory::{RustInventory, TypeId};
use interoptopus::lang::types::{Primitive, Type, TypeKind, TypePattern, VariantKind};
use std::collections::HashSet;
use std::error::Error;
use std::fmt::Write;
use std::path::Path;

pub fn write(inventory: &RustInventory, path: impl AsRef<Path>) -> Result<(), Box<dyn Error>> {
    let mut out = String::new();
    writeln!(
        out,
        "/* Automatically generated from rosu_pp_ffi::ffi_inventory(). */"
    )?;
    writeln!(out, "#ifndef ROSU_PP_FFI_H")?;
    writeln!(out, "#define ROSU_PP_FFI_H")?;
    writeln!(out, "#include <stdbool.h>")?;
    writeln!(out, "#include <stddef.h>")?;
    writeln!(out, "#include <stdint.h>")?;
    writeln!(out, "#ifdef __cplusplus\nextern \"C\" {{\n#endif\n")?;

    let mut forward_names = HashSet::new();
    for ty in inventory.types.values() {
        match &ty.kind {
            TypeKind::Struct(_)
            | TypeKind::Service
            | TypeKind::Opaque
            | TypeKind::TypePattern(
                TypePattern::Utf8String
                | TypePattern::Slice(_)
                | TypePattern::SliceMut(_)
                | TypePattern::Option(_)
                | TypePattern::Result(_, _)
                | TypePattern::Vec(_)
                | TypePattern::Wire(_)
                | TypePattern::TaskHandle,
            ) => {
                let name = c_name(ty);
                if forward_names.insert(name.clone()) {
                    writeln!(out, "typedef struct {0} {0};", name)?;
                }
            }
            TypeKind::Enum(e)
                if e.variants
                    .iter()
                    .any(|v| matches!(v.kind, VariantKind::Tuple(_))) =>
            {
                let name = c_name(ty);
                if forward_names.insert(name.clone()) {
                    writeln!(out, "typedef struct {0} {0};", name)?;
                }
            }
            _ => {}
        }
    }
    writeln!(out)?;

    let mut emitted = HashSet::new();
    let mut emitted_names = HashSet::new();
    let mut pending = inventory.types.iter().collect::<Vec<_>>();
    while !pending.is_empty() {
        let before = pending.len();
        let mut next = Vec::new();
        for (id, ty) in pending {
            if !ready(inventory, ty, &emitted) {
                next.push((id, ty));
                continue;
            }
            let name = c_name(ty);
            if !emitted_names.insert(name.clone()) {
                emitted.insert(*id);
                continue;
            }
            match &ty.kind {
                TypeKind::Primitive(_)
                | TypeKind::ReadPointer(_)
                | TypeKind::ReadWritePointer(_)
                | TypeKind::Array(_)
                | TypeKind::FnPointer(_)
                | TypeKind::WireOnly(_) => {}
                TypeKind::Service | TypeKind::Opaque => {}
                TypeKind::Struct(s) => {
                    writeln!(out, "struct {} {{", name)?;
                    for field in &s.fields {
                        writeln!(
                            out,
                            "    {};",
                            declaration(inventory, field.ty, &field.name)?
                        )?;
                    }
                    writeln!(out, "}};\n")?;
                }
                TypeKind::Enum(e) => {
                    if e.variants
                        .iter()
                        .all(|v| matches!(v.kind, VariantKind::Unit(_)))
                    {
                        writeln!(out, "typedef enum {} {{", name)?;
                        for variant in &e.variants {
                            let VariantKind::Unit(value) = variant.kind else {
                                unreachable!()
                            };
                            writeln!(
                                out,
                                "    {}_{} = {},",
                                upper(&name),
                                upper(&variant.name),
                                value
                            )?;
                        }
                        writeln!(out, "}} {};\n", name)?;
                    } else {
                        writeln!(out, "struct {} {{", name)?;
                        writeln!(out, "    uint32_t variant;")?;
                        writeln!(out, "    union {{")?;
                        for variant in &e.variants {
                            if let VariantKind::Tuple(payload) = variant.kind {
                                writeln!(
                                    out,
                                    "        {};",
                                    declaration(inventory, payload, &lower(&variant.name))?
                                )?;
                            }
                        }
                        writeln!(out, "    }} payload;")?;
                        writeln!(out, "}};\n")?;
                    }
                }
                TypeKind::TypePattern(pattern) => {
                    emit_pattern(&mut out, inventory, *id, &name, pattern)?
                }
            }
            emitted.insert(*id);
        }
        if next.len() == before {
            return Err(format!(
                "cyclic or unsupported value-type dependency: {:?}",
                next.iter().map(|(_, t)| &t.name).collect::<Vec<_>>()
            )
            .into());
        }
        pending = next;
    }

    for function in inventory.functions.values() {
        let rval = type_name(inventory, function.signature.rval)?;
        let args = function
            .signature
            .arguments
            .iter()
            .map(|x| declaration(inventory, x.ty, &x.name))
            .collect::<Result<Vec<_>, _>>()?;
        writeln!(
            out,
            "{} {}({});",
            rval,
            function.name,
            if args.is_empty() {
                "void".to_string()
            } else {
                args.join(", ")
            }
        )?;
    }

    writeln!(out, "\n#ifdef __cplusplus\n}}\n#endif")?;
    writeln!(out, "#endif")?;
    std::fs::write(path, out)?;
    Ok(())
}

fn emit_pattern(
    out: &mut String,
    inv: &RustInventory,
    _id: TypeId,
    name: &str,
    p: &TypePattern,
) -> Result<(), Box<dyn Error>> {
    match p {
        TypePattern::Bool => writeln!(out, "typedef uint8_t {};\n", name)?,
        TypePattern::CChar => writeln!(out, "typedef char {};\n", name)?,
        TypePattern::CVoid => {}
        TypePattern::Version => writeln!(out, "typedef uint64_t {};\n", name)?,
        TypePattern::CStrPointer => writeln!(out, "typedef const char *{};\n", name)?,
        TypePattern::Utf8String => {
            writeln!(
                out,
                "struct {} {{ uint8_t *ptr; uintptr_t len; uintptr_t capacity; }};\n",
                name
            )?;
        }
        TypePattern::Slice(t) => {
            writeln!(
                out,
                "struct {} {{ const {} *data; uintptr_t len; }};\n",
                name,
                type_name(inv, *t)?
            )?;
        }
        TypePattern::SliceMut(t) => {
            writeln!(
                out,
                "struct {} {{ {} *data; uintptr_t len; }};\n",
                name,
                type_name(inv, *t)?
            )?;
        }
        TypePattern::Option(t) => {
            writeln!(
                out,
                "struct {} {{ uint32_t variant; {} some; }};\n",
                name,
                type_name(inv, *t)?
            )?;
        }
        TypePattern::Result(_, _) => {
            writeln!(
                out,
                "struct {} {{ uint32_t variant; union {{ void *ok; uint32_t err; }} payload; }};\n",
                name
            )?;
        }
        TypePattern::Vec(t) => {
            writeln!(
                out,
                "struct {} {{ {} *data; uintptr_t len; uintptr_t capacity; }};\n",
                name,
                type_name(inv, *t)?
            )?;
        }
        TypePattern::Wire(_) => {
            writeln!(
                out,
                "struct {} {{ uint8_t *data; uint32_t len; uint32_t capacity; }};\n",
                name
            )?;
        }
        TypePattern::TaskHandle => writeln!(out, "struct {} {{ void *context; }};\n", name)?,
        TypePattern::NamedCallback(_) | TypePattern::AsyncCallback(_) => {}
    }
    Ok(())
}

fn declaration(inv: &RustInventory, id: TypeId, name: &str) -> Result<String, Box<dyn Error>> {
    let ty = inv.types.get(&id).ok_or("missing inventory type")?;
    if let TypeKind::Array(a) = &ty.kind {
        return Ok(format!("{} {}[{}]", type_name(inv, a.ty)?, name, a.len));
    }
    Ok(format!("{} {}", type_name(inv, id)?, name))
}

fn type_name(inv: &RustInventory, id: TypeId) -> Result<String, Box<dyn Error>> {
    let ty = inv.types.get(&id).ok_or("missing inventory type")?;
    Ok(match &ty.kind {
        TypeKind::Primitive(p) => primitive(*p).to_string(),
        TypeKind::ReadPointer(t) => format!("const {} *", type_name(inv, *t)?),
        TypeKind::ReadWritePointer(t) => format!("{} *", type_name(inv, *t)?),
        TypeKind::Array(a) => type_name(inv, a.ty)?,
        TypeKind::FnPointer(_) => "void *".into(),
        TypeKind::WireOnly(_) => return Err("wire-only type escaped into the raw ABI".into()),
        TypeKind::TypePattern(TypePattern::Bool) => "uint8_t".into(),
        TypeKind::TypePattern(TypePattern::CChar) => "char".into(),
        TypeKind::TypePattern(TypePattern::CVoid) => "void".into(),
        _ => c_name(ty),
    })
}

fn primitive(p: Primitive) -> &'static str {
    match p {
        Primitive::Void => "void",
        Primitive::Bool => "bool",
        Primitive::U8 => "uint8_t",
        Primitive::U16 => "uint16_t",
        Primitive::U32 => "uint32_t",
        Primitive::U64 => "uint64_t",
        Primitive::Usize => "uintptr_t",
        Primitive::I8 => "int8_t",
        Primitive::I16 => "int16_t",
        Primitive::I32 => "int32_t",
        Primitive::I64 => "int64_t",
        Primitive::Isize => "intptr_t",
        Primitive::F32 => "float",
        Primitive::F64 => "double",
    }
}

fn upper(value: &str) -> String {
    value
        .chars()
        .map(|c| {
            if c.is_ascii_alphanumeric() {
                c.to_ascii_uppercase()
            } else {
                '_'
            }
        })
        .collect()
}
fn lower(value: &str) -> String {
    value.chars().flat_map(char::to_lowercase).collect()
}

fn c_name(ty: &Type) -> String {
    if matches!(ty.kind, TypeKind::TypePattern(TypePattern::Result(_, _))) {
        return "ResultPtrFFIError".into();
    }
    let mut value = String::new();
    for c in ty.name.chars() {
        if c.is_ascii_alphanumeric() || c == '_' {
            value.push(c);
        } else {
            value.push('_');
        }
    }
    while value.contains("__") {
        value = value.replace("__", "_");
    }
    value.trim_matches('_').to_string()
}

fn ready(inv: &RustInventory, ty: &Type, emitted: &HashSet<TypeId>) -> bool {
    let is_ready = |id: &TypeId| {
        inv.types.get(id).is_none_or(|dep| match dep.kind {
            TypeKind::Primitive(_)
            | TypeKind::ReadPointer(_)
            | TypeKind::ReadWritePointer(_)
            | TypeKind::Service
            | TypeKind::Opaque => true,
            _ => emitted.contains(id),
        })
    };
    match &ty.kind {
        TypeKind::Struct(s) => s.fields.iter().all(|f| is_ready(&f.ty)),
        TypeKind::Enum(e) => e.variants.iter().all(|v| match &v.kind {
            VariantKind::Unit(_) => true,
            VariantKind::Tuple(id) => is_ready(id),
        }),
        TypeKind::Array(a) => is_ready(&a.ty),
        TypeKind::TypePattern(TypePattern::Option(id) | TypePattern::Vec(id)) => is_ready(id),
        TypeKind::TypePattern(TypePattern::Result(_, _)) => true,
        _ => true,
    }
}
