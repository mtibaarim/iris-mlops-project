import joblib
from sklearn.linear_model import LogisticRegression
from scripts.prepare_data import prepare_dataset

def train_model():
    # Récupération des données ET des noms de cibles
    X_train, y_train, target_names = prepare_dataset()
    
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)
    
    # Sauvegarde de TOUS les artefacts nécessaires à l'API
    joblib.dump(model, 'models/model.joblib')
    joblib.dump(target_names, 'models/targets.joblib')
    print("Étape 2 : Modèle et noms de cibles sauvegardés.")

if __name__ == "__main__":
    train_model()