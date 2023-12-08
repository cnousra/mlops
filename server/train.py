from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import joblib



# Load the Iris dataset
iris = load_iris()

# Access the features and target variable
X = iris.data  # Features
y = iris.target  # Target variable

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


# Créer un modèle de régression linéaire
model = LogisticRegression()

# Entraîner le modèle sur les données d'entraînement
model.fit(X_train, y_train)

# Faire des prédictions sur les données de test
predictions = model.predict(X_test)

# Évaluer les performances du modèle
score = model.score(X_test, y_test)

print(score)

model_filename = "model.pkl"
joblib.dump(model, model_filename)

loaded_model = joblib.load("model.pkl")

