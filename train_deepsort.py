from detect_sort import *
from yolov5.utils.general import check_requirements

check_requirements(exclude=('tensorboard', 'thop'))
detect(weights='yolov5s.pt', imgsz=640, source='pedestrian.mp4')

# python detect_sort.py --weights yolov5s.pt  --img 640  --source pedestrian.mp4