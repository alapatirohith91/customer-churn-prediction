from fastapi import FastAPI
import joblib
import pandas as pd

# Load trained model
model = joblib.load("../model/churn_model.pkl")

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Customer Churn Prediction API Running"
    }

@app.get("/test")
def test():

    sample_data = pd.DataFrame([{
        "gender": "Male",
        "SeniorCitizen": 0,
        "Partner": "Yes",
        "Dependents": "No",
        "tenure": 5,
        "PhoneService": "Yes",
        "MultipleLines": "No",
        "InternetService": "Fiber optic",
        "OnlineSecurity": "No",
        "OnlineBackup": "Yes",
        "DeviceProtection": "No",
        "TechSupport": "No",
        "StreamingTV": "Yes",
        "StreamingMovies": "Yes",
        "Contract": "Month-to-month",
        "PaperlessBilling": "Yes",
        "PaymentMethod": "Electronic check",
        "MonthlyCharges": 95.5,
        "TotalCharges": 477.5
    }])

    # Encode
    sample_encoded = pd.get_dummies(sample_data)

    # Match columns
    training_columns = model.feature_names_in_

    sample_encoded = sample_encoded.reindex(
        columns=training_columns,
        fill_value=0
    )

    # Predict
    prediction = model.predict(sample_encoded)

    return {
        "prediction": int(prediction[0])
    }