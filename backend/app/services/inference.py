import numpy as np

def dummy_detect(image: np.ndarray):
    """
    fake prediction
    gives a single box and 'weapon' label depending on the incoming image's size
    """
    h, w = image.shape[:2]
    # a constant box in the middle of the image
    box_w, box_h = int(w * 0.2), int(h * 0.2)
    x1 = max(0, (w // 2) - (box_w // 2))
    y1 = max(0, (h // 2) - (box_h // 2))
    x2 = min(w - 1, x1 + box_w)
    y2 = min(h - 1, y1 + box_h)

    detections = [{
        "label": "weapon",
        "confidence": 0.85,
        "bbox": [x1, y1, x2, y2]
    }]
    return detections
