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

from .object import *
from .scene import *

class FormatData():
    @staticmethod
    def get_data() -> str:
        text = ""

        scene_units = get_scene_units()
        objects_count = get_objects_count()
        collections_count = get_collections_count()

        mesh_count = get_objects_count_by_type('MESH')
        curve_count = get_objects_count_by_type('CURVE')
        surface_count = get_objects_count_by_type('SURFACE')
        meta_count = get_objects_count_by_type('META')
        font_count = get_objects_count_by_type('FONT')
        volume_count = get_objects_count_by_type('VOLUME')
        armature_count = get_objects_count_by_type('ARMATURE')
        lattice_count = get_objects_count_by_type('LATTICE')
        empty_count = get_objects_count_by_type('EMPTY')
        gpencil_count = get_objects_count_by_type('GPENCIL')
        camera_count = get_objects_count_by_type('CAMERA')
        light_count = get_objects_count_by_type('LIGHT')
        speaker_count = get_objects_count_by_type('SPEAKER')
        light_probe_count = get_objects_count_by_type('LIGHT_PROBE')

        text += FormatData.__header__("Scene stats")

        text += "Units: " + scene_units + "\n"
        text += "Objects count: " + str(objects_count) + "\n"
        text += "Collections count: " + str(collections_count) + "\n"
        text += "Mesh count: " + str(mesh_count) + "\n"
        text += "Curve count: " + str(curve_count) + "\n"
        text += "Surface count: " + str(surface_count) + "\n"
        text += "Meta count: " + str(meta_count) + "\n"
        text += "Font count: " + str(font_count) + "\n"
        text += "Volume count: " + str(volume_count) + "\n"
        text += "Armature count: " + str(armature_count) + "\n"
        text += "Lattice count: " + str(lattice_count) + "\n"
        text += "Empty count: " + str(empty_count) + "\n"
        text += "Gpencil count: " + str(gpencil_count) + "\n"
        text += "Camera count: " + str(camera_count) + "\n"
        text += "Light count: " + str(light_count) + "\n"
        text += "Speaker count: " + str(speaker_count) + "\n"
        text += "Light probe count: " + str(light_probe_count) + "\n"
        text += "\n"

        text += FormatData.__header__("Objects")

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

        return text

    @staticmethod
    def __header__(header: str) -> str:
        frame = "============================"
        header = frame + "\n" + header + "\n" + frame + "\n\n"

        return header