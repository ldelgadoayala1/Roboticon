import numpy as np
import joblib

from tensorflow.keras.models import load_model


class GestureNNModel:

    def __init__(self):

        self.model = load_model(
            "gesture_model.keras"
        )

        self.scaler = joblib.load(
            "scaler.pkl"
        )

        self.encoder = joblib.load(
            "label_encoder.pkl"
        )

    def predict(self, landmarks):

        data = np.array(
            landmarks
        ).reshape(1, -1)

        data = self.scaler.transform(
            data
        )

        prediction = self.model.predict(
            data,
            verbose=0
        )

        predicted_class = np.argmax(
            prediction
        )

        label = self.encoder.inverse_transform(
            [predicted_class]
        )[0]

        return label