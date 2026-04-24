from fastapi import FastAPI, File, UploadFile
import tensorflow as tf
import numpy as np
from PIL import Image
import io
from fastapi import HTTPException

app = FastAPI()

# 🔥 Model load (server start hote hi load ho jayega)
model = tf.keras.models.load_model("best_model.keras")

# ⚠️ same class order hona chahiye
class_names = ['Pepper__bell___Bacterial_spot', 'Pepper__bell___healthy',
               'Potato___Early_blight', 'Potato___healthy', 'Potato___Late_blight',
               'Tomato_Bacterial_spot', 'Tomato_Early_blight',
               'Tomato_Late_blight', 'Tomato_Leaf_Mold',
               'Tomato_Septoria_leaf_spot',
               'Tomato_Spider_mites_Two_spotted_spider_mite',
               'Tomato__Target_Spot', 'Tomato__Tomato_mosaic_virus',
               'Tomato__Tomato_YellowLeaf__Curl_Virus',
               'Tomato_healthy']


#  Image preprocess function
def preprocess_image(image):
    image = image.resize((224, 224))
    img_array = np.array(image)
    img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

#home
@app.get("/")
def home():
    return {"Message": "Welcome to Plant disease Classifier APi"}

#health check

@app.get("/health")
def health():
    return {"status": "API is running"}


# 🚀 API endpoint
@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents)).convert("RGB")

        # preprocess
        img_array = preprocess_image(image)

        # prediction
        preds = model.predict(img_array , verbose=0)
        idx = np.argmax(preds)

        result = {
            "class": class_names[idx],
            "confidence": float(np.max(preds))
        }

        return result
    except Exception as e:
            raise HTTPException(status_code=400, detail="Invalid image file")
