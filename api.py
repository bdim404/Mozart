from fastapi import FastAPI, File, UploadFile
from fastapi.responses import Response
import cv2
import numpy as np
from io import BytesIO
from PIL import Image
import tempfile
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
from main import main

app = FastAPI()

@app.post("/process")
async def process_image(file: UploadFile = File(...)):
    contents = await file.read()

    image = Image.open(BytesIO(contents))
    img_array = np.array(image)

    with tempfile.TemporaryDirectory() as tmpdir:
        input_path = os.path.join(tmpdir, "input.png")
        Image.fromarray(img_array).save(input_path)

        result_img = main(input_path, output_path=None, mode='image')

        if isinstance(result_img, list):
            result_img = result_img[0]

        result_bgr = cv2.cvtColor(result_img, cv2.COLOR_RGB2BGR)
        _, img_encoded = cv2.imencode('.png', result_bgr)

        return Response(content=img_encoded.tobytes(), media_type="image/png")

@app.get("/")
async def root():
    return {"message": "Music Score Recognition API"}
