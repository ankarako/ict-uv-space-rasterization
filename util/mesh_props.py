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

def get_vertex_uvs():
    obj = bpy.context.active_object
    if obj is not None:
        mesh = obj.data
        uv_layer = mesh.uv_layers.active.data
        uvs = []
        for poly in mesh.polygons:
            for loop_index in poly.loop_indices:
                uv_coords = uv_layer[loop_index].uv
                uvs += [np.array(uv_coords)]
        return np.array(uvs)
    return None


def get_polygon_indices():
    obj = bpy.context.active_object
    if obj is not None:
        mesh = obj.data
        polygons = mesh.polygons
        indices = []
        for poly in polygons:
            idx = []
            for i in poly.vertices:
                idx += [i]
            idx = np.array(idx)
            indices += [idx]
        return np.stack(indices).astype(np.uint64)
    return None