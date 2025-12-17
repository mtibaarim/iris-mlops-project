from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_main():
    # Test du point d'entrée racine
    response = client.get("/")
    assert response.status_code == 200

def test_predict_setosa():
    # Test d'une prédiction réelle
    payload = {
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "prediction" in response.json()
    