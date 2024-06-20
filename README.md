# ICT-FaceKit UV Space Rasterization
Just a very small package for rasterizing [ICT-Facekit](https://github.com/ICT-VGL/ICT-FaceKit)'s vertex features onto texture maps (probably could work with other .obj meshes with texture coordinate features).


Tested on ![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white) 22.04 and CUDA 11.8. However, I can't see a reason that it won't run on Windows, or other CUDA versions.

## Dependencies
Just run ```pip install -r requirements.txt``` and you should be ready to go.

**About torch**: I always install pytorch via the provided whls. It should run
with almost, all pytorch versions.

## Usage
```
python rasterize.py --conf /path/to/configuration/file.yaml
```

Configuration files are .yaml files with the following structure:
```
output_dir: path/to/the/output/directory
ict_dir: path/to/directory/with/ict/space/FaceXModel
out_res: 1024 # the resolution of each texture map.
```
