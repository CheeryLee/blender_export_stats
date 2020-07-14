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

class ES_ExportToTextblock(bpy.types.Operator):
    bl_label = "Export Scene Stats"
    bl_description = "Exports all scene stats to a new text block"
    bl_idname = "es.export_to_textblock"
    
    def execute(self, context):
        text_block = bpy.data.texts.new('Scene stats')
        text_block.write(FormatData.get_data())
        self.report({ 'INFO' }, 'Scene stats has been exported to a new text block')

        return {'FINISHED'}

    def invoke(self, context, event):
        return self.execute(context)

def register():
    bpy.utils.register_class(ES_ExportToTextblock)

def unregister():
    bpy.utils.unregister_class(ES_ExportToTextblock)