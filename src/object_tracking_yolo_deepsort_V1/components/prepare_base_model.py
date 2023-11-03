from pathlib import Path
# import pre-trained python
from object_tracking_yolo_deepsort_V1.entity.detect_sort import *
# Check requirements
from object_tracking_yolo_deepsort_V1.entity.yolov5.utils.general import check_requirements

# Excluding tensorboard and thop
check_requirements(exclude=('tensorboard', 'thop'))

##Calling object detection
detect(weights="yolov5s.pt", imgsz=640, source='pedestrian.mp4')