# ICT-FaceKit UV Space Rasterization
Just a very small package for rasterizing [ICT-Facekit](https://github.com/ICT-VGL/ICT-FaceKit)'s vertex features onto texture maps (probably could work with other .obj meshes with texture coordinate features).

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
