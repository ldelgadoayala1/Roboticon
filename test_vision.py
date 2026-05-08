import cv2
from vision.detector import HandDetector

def fingers_to_text(fingers):
    total = sum(fingers)

    if total == 0:
        return "Piedra"
    elif total == 2:
        return "Tijera"
    elif total == 5:
        return "Papel"
    else:
        return f"Detectando... ({total} dedos)"

def main():
    cap = cv2.VideoCapture(0)
    detector = HandDetector()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        hand = detector.detect(frame)

        if hand:
            detector.draw_landmarks(frame, hand)

            fingers = detector.get_fingers_state(hand)
            text = fingers_to_text(fingers)

            print(f"Dedos: {fingers} -> {text}")

            cv2.putText(frame, text, (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 255, 0), 2)

        cv2.imshow("Test Vision", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()