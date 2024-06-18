import bpy
import numpy as np

def get_vertex_positions():
    obj = bpy.context.active_object
    if obj is not None:
        mesh = obj.data
        verts = mesh.vertices
        verts = [[v.co.x, v.co.y, v.co.z] for v in verts]
        return np.array(verts)
    return None

def get_polygon_indices():
    obj = bpy.context.active_object
    if obj is not None:
        mesh = obj.data
        polygons = mesh.polygons
        polygons = [[p.vertices[i] for p in polygons for i in range(len(p.vertices))] for _ in range(len(polygons))]
        return np.array(polygons)
    return None