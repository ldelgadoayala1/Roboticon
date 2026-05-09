import cv2

from vision.detector import HandDetector

from ml.predict_model import GestureModel

from serial_controller import RobotHandController

from game.game_manager import GameManager

from ui.hud import HUD


class RoboCachipunApp:

    PREDICTION_THRESHOLD = 15

    ROBOT_COMMANDS = {

        "rock": 1,
        "paper": 2,
        "scissors": 3
    }

    def __init__(self):

        self.detector = HandDetector()

        self.model = GestureModel()

        self.robot = RobotHandController()

        self.game = GameManager()

        self.cap = cv2.VideoCapture(0)

        self.last_prediction = ""

        self.prediction_counter = 0

    def process_prediction(self, prediction):

        if prediction == self.last_prediction:

            self.prediction_counter += 1

        else:

            self.prediction_counter = 0

            self.last_prediction = prediction

        if self.prediction_counter >= self.PREDICTION_THRESHOLD:

            self.prediction_counter = 0

            return True

        return False

    def send_robot_command(self, move):

        if not self.robot.serial_connection:
            return

        try:

            command = self.ROBOT_COMMANDS[move]

            self.robot.send_command(command)

        except Exception as e:

            print(
                f"Error enviando comando: {e}"
            )

    def draw_ui(self, frame, prediction):

        HUD.draw_text(
            frame,
            f"Jugador: {prediction}",
            (20,50),
            (0,255,0)
        )

        HUD.draw_text(
            frame,
            f"Robot: {self.game.robot_move}",
            (20,100),
            (255,0,0)
        )

        HUD.draw_text(
            frame,
            f"Resultado: {self.game.result}",
            (20,150),
            (0,0,255)
        )

        status = (
            "Arduino conectado"
            if self.robot.serial_connection
            else "Arduino desconectado"
        )

        color = (
            (0,255,0)
            if self.robot.serial_connection
            else (0,0,255)
        )

        HUD.draw_text(
            frame,
            status,
            (20,200),
            color,
            0.8
        )

    def run(self):

        while True:

            ret, frame = self.cap.read()

            if not ret:
                break

            hand = self.detector.detect(frame)

            prediction = ""

            if hand:

                self.detector.draw_landmarks(
                    frame,
                    hand
                )

                prediction = self.model.predict(
                    hand
                )

                if self.process_prediction(
                    prediction
                ):

                    result = self.game.play_round(
                        prediction
                    )

                    self.send_robot_command(
                        result["robot"]
                    )

                    print(result)

            self.draw_ui(
                frame,
                prediction
            )

            cv2.imshow(
                "RoboCachipun",
                frame
            )

            if cv2.waitKey(1) == 27:
                break

        self.close()

    def close(self):

        self.cap.release()

        self.robot.close()

        cv2.destroyAllWindows()


if __name__ == "__main__":

    app = RoboCachipunApp()

    app.run()