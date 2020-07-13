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
from .object import *
from .scene import *

class ES_ExportToTextblock(bpy.types.Operator):
    bl_label = "Export Scene Stats"
    bl_description = "Exports all scene stats to a new text block"
    bl_idname = "es.export_to_textblock"
    
    def execute(self, context):
        text_block = bpy.data.texts.new('Scene stats')
        text = ""

        text += "=======\nScene stats\n=======\n\n"

        scene_units = get_scene_units()
        objects_count = get_objects_count()
        mesh_count = get_objects_count_by_type('MESH')

        text += "Units: " + scene_units + "\n"
        text += "Objects count: " + str(objects_count) + "\n"
        text += "Mesh count: " + str(mesh_count) + "\n"
        text += "\n"

        text += "=======\nObjects\n=======\n\n"

        for ob in bpy.context.scene.objects:
            if ob.type == 'MESH':
                name = get_object_name(ob)
                dim = get_object_dimensions(ob)
                verts = get_vertices_count(ob)
                verts_5_edges = get_vertices_with_links_count(ob, 5, False)
                edges = get_edges_count(ob)
                faces = get_faces_count(ob)
                tris = get_triangles_count(ob)

                text += "Name: " + str(name) + "\n"
                text += "Dimensions: " + str(dim) + "\n"
                text += "Vertices count: " + str(verts) + "\n"
                text += "Vertices with more than 5 edges: " + str(verts_5_edges) + "\n"
                text += "Edges: " + str(edges) + "\n"
                text += "Faces: " + str(faces) + "\n"
                text += "Triangles: " + str(tris) + "\n"
                text += "\n"

        text_block.write(text)

        self.report({ 'INFO' }, 'Scene stats has been exported to a new text block')

        return {'FINISHED'}

    def invoke(self, context, event):
        return self.execute(context)

def register():
    bpy.utils.register_class(ES_ExportToTextblock)

def unregister():
    bpy.utils.unregister_class(ES_ExportToTextblock)