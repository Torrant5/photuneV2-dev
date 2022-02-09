from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import UploadFile, File
import playlist
import os
import time

import config
AI_mode = config.USE_AI
print(AI_mode)
if AI_mode:
    print("AI mode")
    import image_pred
    import name_pred
else:
    print("random mode")

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
async def root():
    return {"message" : "Hello, Photune AI"}

    
@app.post('/api/predict')
async def predict_image(file: UploadFile = File(...)):
    if not AI_mode:
        return playlist.get_random()
        
    # img読み込み
    extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png")
    if not extension:
        return "Image must be jpg or png format!"
    image = image_pred.read_image(await file.read())
    image = image_pred.preprocess(image)

    # 物体予測 
    pred = image_pred.predict(image)
    print(pred)

    # プレイリスト予測
    text = "{}と{}に関する曲を聴きたい".format(pred[0]["class"], pred[1]["class"])
    try: 
        # data = name_pred.predict_direct(text)
        data = name_pred.predict_indirect(text)
        # print(data)
    except:
        data = playlist.get_random()
        print("Name Prediction Error")
    return data


@app.get('/api/random')
async def predict_image():
    return playlist.get_random()

@app.get('/api/sample')
async def predict_image(id: int=3):
    return playlist.get_sample(id)

@app.get('/api/text/{input_text}')
async def predict_image(input_text: str, mode: int=0):
    if not AI_mode:
        return playlist.get_random()
        
    if mode==1  :
        return name_pred.predict_direct(input_text)
    else :
        return name_pred.predict_indirect(input_text)