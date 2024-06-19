# ICT-FaceKit UV Space Rasterization
Just a very small package for rasterizing [ICT-Facekit](https://github.com/ICT-VGL/ICT-FaceKit) (probably could work with other .obj meshes with texture coordinate features).

## Dependencies
Just run ```pip install -r requirements.txt``` and you should be ready to go.

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
