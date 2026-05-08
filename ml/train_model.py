import os
import joblib
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report


DATASET = "ml/dataset.csv"

MODEL_OUTPUT = "ml/model/rps_model.pkl"

os.makedirs("ml/model", exist_ok=True)

print("Cargando dataset...")

df = pd.read_csv(DATASET, header=None)

X = df.iloc[:, :-1]
y = df.iloc[:, -1]

print(f"Muestras totales: {len(df)}")

print("Separando dataset...")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Entrenando modelo...")

model = RandomForestClassifier(
    n_estimators=300,
    random_state=42
)

model.fit(X_train, y_train)

print("Evaluando modelo...")

predictions = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    predictions
)

print(f"\nAccuracy: {accuracy:.4f}\n")

print("Reporte:\n")

print(
    classification_report(
        y_test,
        predictions
    )
)

print("Exportando modelo...")

joblib.dump(
    model,
    MODEL_OUTPUT
)

print(f"\nModelo exportado en: {MODEL_OUTPUT}")