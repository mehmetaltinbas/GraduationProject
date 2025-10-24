from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import numpy as np
import cv2

from ..services.inference import dummy_detect

router = APIRouter()

@router.post("/predict")
async def predict(file: UploadFile = File(...)):
    if file.content_type is None or not file.content_type.startswith(("image/", "application/octet-stream")):
        raise HTTPException(status_code=400, detail="Please upload an image file.")

    # take bytes and convert to a image via opencv
    data = await file.read()
    nparr = np.frombuffer(data, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    if img is None:
        raise HTTPException(status_code=400, detail="Invalid image data.")

    # mock detection
    detections = dummy_detect(img)

    return JSONResponse(content={"detections": detections})
