import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

class HandDetector:
    def __init__(self, model_path="hand_landmarker.task"):
        # Configuración del modelo
        base_options = python.BaseOptions(model_asset_path=model_path)

        options = vision.HandLandmarkerOptions(
            base_options=base_options,
            num_hands=1
        )

        self.detector = vision.HandLandmarker.create_from_options(options)

    def detect(self, frame):
        # Convertir imagen a formato MediaPipe
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)

        result = self.detector.detect(mp_image)

        if result.hand_landmarks:
            return result.hand_landmarks[0]  # solo una mano

        return None

    def draw_landmarks(self, frame, hand_landmarks):
        h, w, _ = frame.shape

        for landmark in hand_landmarks:
            cx, cy = int(landmark.x * w), int(landmark.y * h)
            cv2.circle(frame, (cx, cy), 5, (0, 255, 0), -1)

    def get_fingers_state(self, hand_landmarks):
        """
        Retorna lista de dedos levantados [thumb, index, middle, ring, pinky]
        """
        tips_ids = [4, 8, 12, 16, 20]
        fingers = []

        # Pulgar (comparación eje X)
        if hand_landmarks[4].x < hand_landmarks[3].x:
            fingers.append(1)
        else:
            fingers.append(0)

        # Otros dedos (eje Y)
        for tip in tips_ids[1:]:
            if hand_landmarks[tip].y < hand_landmarks[tip - 2].y:
                fingers.append(1)
            else:
                fingers.append(0)

        return fingers