use interoptopus::ffi_type;

#[ffi_type]
#[repr(C)]
#[derive(Debug, Clone, Default)]
pub struct Pos {
    /// Position on the x-axis.
    pub x: f32,
    /// Position on the y-axis.
    pub y: f32,
}

impl From<rosu_map::util::Pos> for Pos {
    fn from(pos: rosu_map::util::Pos) -> Self {
        Self { x: pos.x, y: pos.y }
    }
}