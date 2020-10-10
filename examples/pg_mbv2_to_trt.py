"""

this using Pilgrim convert MobileNetV3 to TensorRT engine

"""
from torch2trt.torch2trt import torch2trt
import torch
from torch import nn
from torchvision.models.resnet import resnet50
from torchvision.models.mobilenet import mobilenet_v2

# create some regular pytorch model...
model = mobilenet_v2().cuda().eval()

# create example data
x = torch.ones((1, 3, 224, 224)).cuda()

# convert to TensorRT feeding sample data as input
opt_shape_param = [
    [
        [1, 3, 128, 128],   # min
        [1, 3, 256, 256],   # opt
        [1, 3, 512, 512]    # max
    ]
]
model_trt = torch2trt(model, [x], fp16_mode=False)

print('serialize engine...')
engine_path = 'mbv2.trt'
with open(engine_path, "wb") as f:
    f.write(model_trt.engine.serialize())

print('Done.')