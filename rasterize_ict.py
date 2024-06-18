import argparse
import os
import util

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
    util.io.load_generic_model(conf.ict_dir)
    v_pos = util.mesh_props.get_vertex_positions()
    t_pos_idx = util.mesh_props.get_polygon_indices()
    print("ICT uv rasterization app terminated.")