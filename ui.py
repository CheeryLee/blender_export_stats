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
from bpy.types import Panel
from .ops import *

class ES_PT_StatsPanel(Panel):
    bl_label = "Scene Stats"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Scene Stats"

    def draw(self, context):
        layout = self.layout
        props = bpy.context.scene.export_scene_stats

        layout.label(text = "Export stats:")
        layout.prop(props, "scene_data")
        layout.prop(props, "objects_data")
        layout.operator(ES_ExportToTextblock.bl_idname, icon = "EXPORT")

def register():
    bpy.utils.register_class(ES_PT_StatsPanel)

def unregister():
    bpy.utils.unregister_class(ES_PT_StatsPanel)