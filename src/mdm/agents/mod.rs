mod cursor;

pub use cursor::CursorInstaller;

use super::hook_installer::HookInstaller;

/// Get all available hook installers
pub fn get_all_installers() -> Vec<Box<dyn HookInstaller>> {
    vec![Box::new(CursorInstaller)]
}
