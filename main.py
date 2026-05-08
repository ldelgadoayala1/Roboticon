import cv2
from vision import HandDetector
from serial_controller import ArduinoController
from game import RockPaperScissors

def main():
    cap = cv2.VideoCapture(0)

    detector = HandDetector()
    game = RockPaperScissors()
    arduino = ArduinoController(port='COM3')  # cambia según tu puerto

    last_move = None

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        hand = detector.detect(frame)

        if hand:
            fingers = detector.get_fingers_state(hand)
            player_move = game.fingers_to_move(fingers)

            if player_move and player_move != last_move:
                ai_move = game.get_ai_move()
                result = game.get_winner(player_move, ai_move)

                print(f"Jugador: {player_move}, IA: {ai_move} -> {result}")

                # Enviar movimiento al Arduino
                arduino.send_move(ai_move)

                last_move = player_move

        cv2.imshow("Hand Detection", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    arduino.close()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()