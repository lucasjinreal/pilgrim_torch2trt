import os
import os.path as osp
dir_path = osp.join( os.path.expanduser('~'), "space/trt_plugin/build/lib/")

if not osp.exists(dir_path):
    if "PILGRIM_TRT_PLUGINS_LIB" in os.environ:
        dir_path = os.environ["PILGRIM_TRT_PLUGINS_LIB"]
    else:
        dir_path = os.path.dirname(os.path.realpath(__file__))