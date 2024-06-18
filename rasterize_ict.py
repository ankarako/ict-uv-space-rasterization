import argparse
import os
import util
import rasterization as raster

import torch
import numpy as np
import cv2
from tqdm import tqdm

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Rasterize ICT UV space")
    parser.add_argument("--conf", type=str, help="The path to the configuration file to load.")
    args = parser.parse_args()

    print("Starting ICT uv rasterization app")
    # read configuration file
    conf = util.conf.read_conf(args.conf)

    # create output dir
    if not os.path.exists(conf.output_dir):
        os.mkdir(conf.output_dir)
    
    # import generic neutral mesh
    print("loading generic neurtral mesh...")
    v_pos, v_uvs, t_pos_idx, t_uvs_idx = util.io.load_generic_model(conf.ict_dir)


    output_texture = torch.zeros([512, 512, 3], dtype=torch.float32).cuda()
    for idx, (t_pos_i, t_uvs_i) in tqdm(enumerate(zip(t_pos_idx, t_uvs_idx)), total=len(t_pos_idx), desc="Rasterizing triangles"):
        output_texture = raster.rasterize_triangle(v_pos[t_pos_i], v_uvs[t_uvs_i], v_pos[t_pos_i], output_texture)

    # save a png image
    min_val = output_texture.reshape(-1, 3).min(dim=0).values
    max_val = output_texture.reshape(-1, 3).max(dim=0).values
    filepath = os.path.join(conf.output_dir, 'output.png')
    output_texture = (output_texture - min_val) / (max_val - min_val)
    output_texture = (output_texture * 255).cpu().numpy().astype(np.uint8)
    cv2.imwrite(filepath, output_texture)

    print("ICT uv rasterization app terminated.")