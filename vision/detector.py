import cv2
import mediapipe as mp

from mediapipe.tasks import python
from mediapipe.tasks.python import vision


class HandDetector:

    def __init__(self):

        base_options = python.BaseOptions(
            model_asset_path="hand_landmarker.task"
        )

        options = vision.HandLandmarkerOptions(
            base_options=base_options,
            num_hands=1
        )

        self.detector = vision.HandLandmarker.create_from_options(
            options
        )

    def detect(self, frame):

        rgb_frame = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=rgb_frame
        )

        detection_result = self.detector.detect(
            mp_image
        )

        if detection_result.hand_landmarks:

            return detection_result.hand_landmarks[0]

        return None

    def draw_landmarks(self, frame, hand_landmarks):

        h, w, _ = frame.shape

        for landmark in hand_landmarks:

            x = int(landmark.x * w)
            y = int(landmark.y * h)

            cv2.circle(
                frame,
                (x, y),
                5,
                (0,255,0),
                -1
            )

    def get_fingers_state(self, hand_landmarks):

        tips = [4, 8, 12, 16, 20]

        fingers = []

        thumb_tip = hand_landmarks[tips[0]]
        thumb_ip = hand_landmarks[tips[0] - 1]

        fingers.append(
            1 if thumb_tip.x < thumb_ip.x else 0
        )

        for tip in tips[1:]:

            finger_tip = hand_landmarks[tip]
            finger_pip = hand_landmarks[tip - 2]

            fingers.append(
                1 if finger_tip.y < finger_pip.y else 0
            )

        return fingers