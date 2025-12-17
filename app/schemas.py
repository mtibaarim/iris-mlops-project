'''Ce fichier contient les schémas Pydantic utilisés pour la validation
des données d’entrée du modèle Iris.

Les schémas permettent de :
- vérifier les types des données reçues
- garantir que tous les champs requis sont présents
- générer automatiquement la documentation de l’API avec des exemples
'''

from pydantic import BaseModel, Field

class IrisInput(BaseModel):
    sepal_length: float = Field(..., example=5.1)
    sepal_width: float = Field(..., example=3.5)
    petal_length: float = Field(..., example=1.4)
    petal_width: float = Field(..., example=0.2)