from fastapi import FastAPI
import joblib

# Load trained model
model = joblib.load("../model/churn_model.pkl")

# Create FastAPI app
app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Customer Churn Prediction API Running"
    }

@app.post("/predict")
def predict(data: list):

    prediction = model.predict([data])

    return {
        "prediction": int(prediction[0])
    }