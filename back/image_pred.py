from PIL import Image
from io import BytesIO
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications import imagenet_utils


model = None

def load_model():
    model = tf.keras.applications.MobileNetV2(weights="imagenet")
    return model

def read_image(image_encoded: Image.Image):
    pil_image = Image.open(BytesIO(image_encoded))
    # pil_image.show()
    return pil_image

def preprocess(image: Image.Image):
    image = np.asarray(image.resize((224, 224)))[..., :3]
    image = np.expand_dims(image, 0)
    image = image / 127.5 - 1.0
    return image

def predict(image: np.ndarray):
    global model
    if model is None:
        model = load_model()
    pred = imagenet_utils.decode_predictions(model.predict(image), 2)[0]

    response = []
    for i, res in enumerate(pred):
        resp = {}
        resp["class"] = res[1]
        resp["confidence"] = f"{res[2] * 100:0.2f} %"

        response.append(resp)

    return response