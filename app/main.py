from fastapi import FastAPI
from app.schemas import IrisInput
import joblib
import numpy as np

app = FastAPI(title="Iris MLOps API")

# Chargement des artefacts au démarrage de l'API
MODEL = joblib.load('models/model.joblib')
SCALER = joblib.load('models/scaler.joblib')
TARGETS = joblib.load('models/targets.joblib')

@app.get("/")
def health_check():
    return {"status": "online"}

@app.post("/predict")
def predict(data: IrisInput):
    """Prédit l'espèce d'Iris à partir des caractéristiques."""
    features = np.array([[data.sepal_length, data.sepal_width, 
                          data.petal_length, data.petal_width]])
    
    # Application du scaling sauvegardé
    features_scaled = SCALER.transform(features)
    prediction = MODEL.predict(features_scaled)
    
    return {
        "prediction": TARGETS[prediction[0]],
        "model_info": "LogisticRegression"
    }