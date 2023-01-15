import cv2
from .yolov5_tools import Detection

# detector_veh = Detection()
# detector_veh.weights = "resources/weights/yolov5s.pt"
# detector_veh.device = "cpu"
# detector_veh.half = False
# detector_veh.imgsz = (640, 640)
# detector_veh.conf_thres = 0.2
# detector_veh.classes = [2, 3, 5, 7]
# detector_veh.agnostic_nms = True
# detector_veh._load_model()
###########################
detector_plate = Detection()
detector_plate.weights = "resources/weights/plate_v2_256.pt"
detector_plate.device = "cpu"
detector_plate.half = False
detector_plate.imgsz = (256, 256)
detector_plate.conf_thres = 0.2
detector_plate.classes = [0]
detector_plate.agnostic_nms = True
detector_plate._load_model()
###########################
detector_digit = Detection()
detector_digit.weights = "resources/weights/digit_v6_256.pt"
detector_digit.device = "cpu"
detector_digit.half = False
detector_digit.imgsz = (256, 256)
detector_digit.conf_thres = 0.2
detector_digit.classes = None
detector_digit.agnostic_nms = True
detector_digit._load_model()


def check_square_plate(image):
    H, W = image.shape[:2]
    return W / H < 2

def process_square_plate(bboxes):
    y_sum = sum([bbox[1] for bbox in bboxes])
    y_avarage = y_sum / len(bboxes)
    bbox_1 = [bbox for bbox in bboxes if bbox[1] < y_avarage]
    bbox_2 = [bbox for bbox in bboxes if bbox[1] > y_avarage]
    if len(bbox_1) == 4:
        if 0 <= int(bbox_1[3][4]) <= 9 and int(bbox_1[2][4]) > 9:
            return 3, bbox_1 + bbox_2
    return 2, bbox_1 + bbox_2

def detect(image):
    cls_veh = ""
    bboxes_plate = detector_plate.detect(image)
    for bbox_plate in bboxes_plate:
        x1, y1, x2, y2, cls, conf = bbox_plate
        crop_plate = image[y1:y2, x1:x2]
        bbox_digit = detector_digit.detect(crop_plate)
        if not bbox_digit:
            continue
        bbox_digit = sorted(bbox_digit, key=lambda x: x[0])
        is_square_plate = check_square_plate(crop_plate)
        if is_square_plate:
            cls_veh, bbox_digit = process_square_plate(bbox_digit)
        else:
            cls_veh = 2
        lp_text = ""
        for x1, y1, x2, y2, cls, conf in bbox_digit:
            lp_text += str(detector_digit.names[int(cls)])
        if 6 <= len(lp_text) <= 9:
            return cls_veh, lp_text
    return cls_veh, ""
            
        