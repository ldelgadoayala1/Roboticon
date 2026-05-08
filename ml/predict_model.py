import joblib
import numpy as np


class GestureModel:

    def __init__(self):

        self.model = joblib.load(
            "ml/model/rps_model.pkl"
        )

    def predict(self, hand_landmarks):

        row = []

        for landmark in hand_landmarks:

            row.extend([
                landmark.x,
                landmark.y,
                landmark.z
            ])

        prediction = self.model.predict(
            [np.array(row)]
        )

        return prediction[0]