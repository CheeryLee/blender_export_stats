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
import bmesh
import mathutils

def get_object_name(ob: bpy.types.Object) -> str:
    return ob.name

def get_object_dimensions(mesh: bpy.types.Object) -> mathutils.Vector:
    return mesh.dimensions

def get_vertices_count(mesh: bpy.types.Object) -> int:
    return len(mesh.data.vertices)
    
def get_vertices_with_links_count(mesh: bpy.types.Object, count: int, strict_comparison: bool) -> int:
    c = 0
    bm = bmesh.new()

    bm.from_mesh(mesh.data)
    bm.verts.ensure_lookup_table()
    
    for v in bm.verts:
        if strict_comparison:
            if len(v.link_edges) >= count:
                c += 1
        else:
            if len(v.link_edges) == count:
                c += 1
            
    return c

def get_faces_count(mesh: bpy.types.Object) -> int:
    return len(mesh.data.polygons)

def get_faces_with_vertices_count(mesh: bpy.types.Object, count: int) -> int:
    c = 0

    for p in mesh.data.polygons:
        if len(p.vertices) == count:
            c += 1
    
    return c

def get_triangles_count(mesh: bpy.types.Object) -> int:
    c = 0

    for p in mesh.data.polygons:
        c += len(p.vertices) - 2

    return c

def get_edges_count(mesh: bpy.types.Object) -> int:
    return len(mesh.data.edges)

def get_materials_count(mesh: bpy.types.Object) -> int:
    return len(bpy.context.active_object.material_slots)