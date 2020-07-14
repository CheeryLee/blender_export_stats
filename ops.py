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
from .format import *

class ExportProps(bpy.types.PropertyGroup):
    scene_data: bpy.props.BoolProperty(
        name = "Scene data",
        description = "Export scene data",
        default = True
    )

    objects_data: bpy.props.BoolProperty(
        name = "Objects data",
        description = "Export objects data",
        default = True
    )

class ES_ExportToTextblock(bpy.types.Operator):
    bl_label = "Export Scene Stats"
    bl_description = "Exports all scene stats to a new text block"
    bl_idname = "es.export_to_textblock"
    
    def execute(self, context):
        props = bpy.context.scene.export_scene_stats

        if not props.scene_data and not props.objects_data:
            self.report({ 'INFO' }, 'Nothing to export')
            return {'CANCELLED'}
        else:
            text_block = bpy.data.texts.new('Scene stats')
            text = ""

            if props.scene_data:
                text += FormatData.get_scene_data()
            if props.objects_data:
                text += FormatData.get_objects_data()

            text_block.write(text)
            self.report({ 'INFO' }, 'Scene stats has been exported to a new text block')

            return {'FINISHED'}

    def invoke(self, context, event):
        return self.execute(context)

def register():
    bpy.utils.register_class(ExportProps)
    bpy.utils.register_class(ES_ExportToTextblock)

    bpy.types.Scene.export_scene_stats = bpy.props.PointerProperty(type = ExportProps)

def unregister():
    bpy.utils.unregister_class(ExportProps)
    bpy.utils.unregister_class(ES_ExportToTextblock)

    del(bpy.types.Scene.export_scene_stats)