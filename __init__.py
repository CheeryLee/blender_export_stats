#
# Copyright (c) 2020 Alexander "CheeryLee" Pluzhnikov
# 
# This file is part of blender_export_stats.
# 
# blender_export_stats is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# blender_export_stats is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with blender_export_stats.  If not, see <http://www.gnu.org/licenses/>.
#

import bpy
from . import (
    ops,
    ui
)

bl_info = {
    "name": "Export Stats",
    "author": "Alexander Pluzhnikov",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "",
    "description": "Export scene statistics",
    "category": "System",
    }

def register():
    ops.register()
    ui.register()

    print("Export Stats tools activated")

def unregister():
    ops.unregister()
    ui.unregister()

    print("Export Stats tools deactivated")

if __name__ == "__main__":
    register()