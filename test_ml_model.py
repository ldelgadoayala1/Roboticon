import cv2
import sys

sys.path.append(".")

from vision.detector import HandDetector
from ml.predict_model import GestureModel

detector = HandDetector()

model = GestureModel()

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    hand = detector.detect(frame)

    if hand:

        detector.draw_landmarks(
            frame,
            hand
        )

        prediction = model.predict(
            hand
        )

        cv2.putText(
            frame,
            f"ML: {prediction}",
            (20,50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,255,0),
            2
        )

    cv2.imshow(
        "ML Gesture Recognition",
        frame
    )

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()