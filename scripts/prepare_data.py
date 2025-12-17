import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib
import os

def prepare_dataset():
    """Simule le traitement de données brutes vers un format exploitable."""
    # 1. Acquisition (Donnée brute)
    raw_data = load_iris()
    df = pd.DataFrame(raw_data.data, columns=raw_data.feature_names)
    df['target'] = raw_data.target

    # 2. Nettoyage & Exploration des données
    # On vérifie qu'il n'y a pas de valeurs nulles
    df = df.dropna()
    
    # 3. Séparation Features/Target
    X = df.drop('target', axis=1)
    y = df['target']
    
    # 4. Feature Engineering : Standardisation
    # On crée le scaler ici pour qu'il soit identique en prod
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # 5. Split pour validation
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42
    )
    
    # Sauvegarde des données traitées et du scaler
    os.makedirs('data/processed', exist_ok=True)
    os.makedirs('models', exist_ok=True)
    
    # On sauvegarde le scaler : pièce maîtresse pour l'API
    joblib.dump(scaler, 'models/scaler.joblib')
    
    return X_train, y_train, raw_data.target_names

if __name__ == "__main__":
    prepare_dataset()
    print("Étape 1 : Données préparées et Scaler sauvegardé.")