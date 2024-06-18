import os
import bpy
import numpy as np


def load_generic_model(dir: str) -> np.ndarray:
    """
    Load ict facekit's generic model

    :param dir The directory with ICTFaceKit's data.
    :return
    """
    filepath = os.path.join(dir, 'generic_neutral_mesh.obj')
    if not os.path.exists(filepath):
        print("The specified ICT directory does not contain generic_neutral_mesh.obj")
        return None
    
    bpy.ops.wm.obj_import(filepath=filepath)
