# Utilisation d'une image de base légère
FROM python:3.10-slim

# Définition du répertoire de travail dans le conteneur
WORKDIR /app

# Installation des dépendances système si nécessaire
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copie du fichier de dépendances
COPY requirements.txt .

# Installation des bibliothèques Python
RUN pip install --no-cache-dir -r requirements.txt

# Copie du code de l'application et des artefacts du modèle
COPY app/ ./app/
COPY models/ ./models/
COPY scripts/ ./scripts/

# Exposition du port utilisé par FastAPI
EXPOSE 8000

# Commande de lancement de l'API
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]