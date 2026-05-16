import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical

import joblib


# ==========================================
# CARGAR DATASET SIN HEADERS
# ==========================================

df = pd.read_csv(
    "ml/dataset.csv",
    sep=",",
    header=None
)

# ==========================================
# GENERAR HEADERS AUTOMÁTICOS
# ==========================================

num_columns = df.shape[1]

feature_columns = [
    f"f{i}"
    for i in range(num_columns - 1)
]

columns = feature_columns + ["label"]

df.columns = columns

print(df.head())

# ==========================================
# FEATURES / LABELS
# ==========================================

X = df.drop(
    "label",
    axis=1
).values

y = df["label"].values

# ==========================================
# NORMALIZAR
# ==========================================

scaler = StandardScaler()

X = scaler.fit_transform(X)

# ==========================================
# LABEL ENCODER
# ==========================================

encoder = LabelEncoder()

y_encoded = encoder.fit_transform(y)

y_categorical = to_categorical(
    y_encoded
)

# ==========================================
# TRAIN TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_categorical,
    test_size=0.2,
    random_state=42
)

# ==========================================
# MODELO
# ==========================================

model = Sequential([

    Dense(
        128,
        activation="relu",
        input_shape=(X.shape[1],)
    ),

    Dense(
        64,
        activation="relu"
    ),

    Dense(
        32,
        activation="relu"
    ),

    Dense(
        3,
        activation="softmax"
    )
])

# ==========================================
# COMPILAR
# ==========================================

model.compile(

    optimizer="adam",

    loss="categorical_crossentropy",

    metrics=["accuracy"]
)

# ==========================================
# ENTRENAR
# ==========================================

history = model.fit(

    X_train,

    y_train,

    epochs=50,

    batch_size=32,

    validation_data=(
        X_test,
        y_test
    )
)

# ==========================================
# EVALUAR
# ==========================================

loss, accuracy = model.evaluate(
    X_test,
    y_test
)

print(f"\nAccuracy: {accuracy:.4f}")

# ==========================================
# GUARDAR
# ==========================================

model.save(
    "gesture_model.keras"
)

joblib.dump(
    scaler,
    "scaler.pkl"
)

joblib.dump(
    encoder,
    "label_encoder.pkl"
)

print("\nModelo guardado correctamente.")