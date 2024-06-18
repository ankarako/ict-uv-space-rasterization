from typing import Tuple
import os
import tinyobjloader as tinyobj
import torch


def load_generic_model(dir: str) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
    """
    Load ict facekit's generic model

    :param dir The directory with ICTFaceKit's data.
    :return
    """
    reader = tinyobj.ObjReader()
    filepath = os.path.join(dir, 'generic_neutral_mesh.obj')
    if not os.path.exists(filepath):
        print("The specified ICT directory does not contain generic_neutral_mesh.obj")
        return None
    obj = reader.ParseFromFile(filepath)
    attrib = reader.GetAttrib()
    materials = reader.GetMaterials()
    shapes = reader.GetShapes()

    v_pos = torch.tensor(list(attrib.vertices), dtype=torch.float32).reshape(-1, 3)
    v_uvs = torch.tensor(list(attrib.texcoords), dtype=torch.float32).reshape(-1, 3)
    shape = shapes[-1] # we probably know that we expect a single shape

    t_pos_idx = []
    t_uvs_idx = []
    for idx_entry in shape.mesh.indices:
        t_pos_idx += [idx_entry.vertex_index]
        t_uvs_idx += [idx_entry.texcoord_index]
    t_pos_idx = torch.tensor(t_pos_idx, dtype=torch.long).reshape(-1, 4)
    t_uvs_idx = torch.tensor(t_uvs_idx, dtype=torch.long).reshape(-1, 4)
    return v_pos, v_uvs, t_pos_idx, t_uvs_idx


