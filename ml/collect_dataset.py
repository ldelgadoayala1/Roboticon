import csv
import cv2
import os
import sys

sys.path.append(".")

from vision.detector import HandDetector

LABEL = "rock"  # cambiar: rock/paper/scissors

OUTPUT_FILE = "ml/dataset.csv"

detector = HandDetector()

cap = cv2.VideoCapture(0)

os.makedirs("ml", exist_ok=True)

with open(OUTPUT_FILE, "a", newline="") as f:

    writer = csv.writer(f)

    while True:

        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        
        if not ret:
            break

        hand = detector.detect(frame)

        if hand:

            detector.draw_landmarks(frame, hand)

            row = []

            for landmark in hand:

                row.extend([
                    landmark.x,
                    landmark.y,
                    landmark.z
                ])

            row.append(LABEL)

            writer.writerow(row)

            cv2.putText(
                frame,
                f"Capturando: {LABEL}",
                (20,50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0,255,0),
                2
            )

        cv2.imshow("Dataset Capture", frame)

        key = cv2.waitKey(1)

        if key == 27:
            break

cap.release()
cv2.destroyAllWindows()