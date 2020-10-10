# Pilgrim Project

This project is forked from torch2trt and torch2trt_dynamic, the aiming of this project is provide a way directly convert pytorch models to TensorRT engine.

This can be fasten your project if your model was built upon pytorch, we have tested several models all works fine and we will add more test and plugins to support model complicated models.

The reason why we don't want onnx way is that:

- onnx is another middle-ware not very necessary;
- it's not easy to maintain an onnx-plugin in both converter of onnx it-self as well as converter which is onnx2trt.

## Usage

pilgrim is in early stage, the target model on our list are:

- [x] mobielentv3;
- [x] resnet50;
- [ ] yolov3;
- [ ] yolov5;
- [ ] MaskRCNN
- [ ] more...

You can check models under examples folder. For install it, simply:

```
sudo python3 setup.py build develop
```

For Highly complicated model, such as FasterRCNN, MaskRCNN, YoloV5, Centernet-DCN, you gonna need build plugins for support:

```
cd pilgrim_trt_plugins
./build.sh
```

the plugins will update every frequently, so pls make sure your repo is up to date.



## TODO

- [ ] Try converting FasterRCNN model to TensorRT with pilgrim tool;
- [ ] Try converting YoloV5 model to tensorrt with pilgrim tool;
- [ ] Try converting CenterNet-DCN to tensorrt with pilgrim tool (this will invoke DCN plugin directly mapping pytorch plugin to TensorRT plugin without any ONNX dependencies);

## Copyright

Copyright belongs to NVIDIA and all related authors.
