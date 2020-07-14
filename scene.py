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

def get_scene_units() -> str:
    system = bpy.context.scene.unit_settings.system
    system_name = ""

    if system == 'NONE':
        system_name = "None"
    elif system == 'METRIC':
        system_name = "Metric"
    elif system == 'IMPERIAL':
        system_name = "Imperial"
        
    return system_name

def get_objects_count() -> int:
    return len(bpy.context.scene.objects)

def get_collections_count() -> int:
    return len(bpy.data.collections)

def get_objects_count_by_type(ob_type: str) -> int:
    c = 0

    for ob in bpy.context.scene.objects:
        if ob_type == ob.type:
            c += 1

    return c