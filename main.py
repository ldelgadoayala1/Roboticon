import cv2
import time

from vision.detector import HandDetector
from ml.predict_nn_model import GestureNNModel
from serial_controller import RobotHandController
from game.game_manager import GameManager
from ui.hud import HUD


class RoboCachipunApp:

    STATE_MENU = "MENU"

    STATE_COUNTDOWN = "COUNTDOWN"

    STATE_RESULT = "RESULT"

    STATE_ASK_CONTINUE = "ASK_CONTINUE"

    ROBOT_COMMANDS = {

        "rock": 1,
        "paper": 2,
        "scissors": 3
    }

    def __init__(self):

        self.detector = HandDetector()

        self.model = GestureNNModel()

        self.robot = RobotHandController()

        self.game = GameManager()

        self.cap = cv2.VideoCapture(0)

        self.state = self.STATE_MENU

        self.countdown_words = [
            "CA",
            "CHI",
            "PUN"
        ]

        self.countdown_index = 0

        self.last_countdown_time = time.time()

        self.result_time = 0

    # ==========================================
    # ARDUINO
    # ==========================================

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

    # ==========================================
    # RESET ROUND
    # ==========================================

    def reset_round(self):

        self.countdown_index = 0

        self.last_countdown_time = time.time()

    # ==========================================
    # MENU
    # ==========================================

    def draw_menu(self, frame):

        HUD.draw_text(
            frame,
            "ROBOCACHIPUN",
            (140, 120),
            (0, 255, 255),
            2
        )

        HUD.draw_text(
            frame,
            "Presione ENTER para comenzar",
            (90, 260),
            (255, 255, 255),
            1
        )

    # ==========================================
    # COUNTDOWN
    # ==========================================

    def handle_countdown(self, frame):

        current_time = time.time()

        if current_time - self.last_countdown_time >= 1:

            self.countdown_index += 1

            self.last_countdown_time = current_time

        if self.countdown_index < 3:

            word = self.countdown_words[
                self.countdown_index
            ]

            HUD.draw_text(
                frame,
                word,
                (250, 240),
                (0, 255, 255),
                3
            )

        else:

            self.resolve_round()

            self.state = self.STATE_RESULT

            self.result_time = time.time()

    # ==========================================
    # RESOLVER PARTIDA
    # ==========================================

    def resolve_round(self):

        ret, frame = self.cap.read()

        if not ret:
            return

        hand = self.detector.detect(frame)

        if not hand:

            self.game.player_move = "NO DETECTADO"

            self.game.robot_move = "-"

            self.game.result = "MANO NO DETECTADA"

            return

        # ==========================================
        # CONVERTIR LANDMARKS A VECTOR NUMÉRICO
        # ==========================================

        landmark_list = []

        for landmark in hand:

            landmark_list.extend([
                landmark.x,
                landmark.y,
                landmark.z
            ])

        # ==========================================
        # PREDICCIÓN ML
        # ==========================================

        prediction = self.model.predict(
            landmark_list
        )

        result = self.game.play_round(
            prediction
        )

        self.send_robot_command(
            result["robot"]
        )

        print(result)

        ret, frame = self.cap.read()

        if not ret:
            return

        hand = self.detector.detect(frame)

        if not hand:

            self.game.player_move = "NO DETECTADO"

            self.game.robot_move = "-"

            self.game.result = "MANO NO DETECTADA"

            return

        # ==========================================
        # CONVERTIR LANDMARKS A VECTOR NUMÉRICO
        # ==========================================

        landmark_list = []

        for landmark in hand:

            landmark_list.extend([
                landmark.x,
                landmark.y,
                landmark.z
            ])


        # ==========================================
        # PREDICCIÓN ML
        # ==========================================

        prediction = self.model.predict(
            landmark_list
        )

        self.send_robot_command(
            result["robot"]
        )

        print(result)

    # ==========================================
    # RESULTADO
    # ==========================================

    def draw_result(self, frame):

        HUD.draw_text(
            frame,
            f"Jugador: {self.game.player_move}",
            (40, 80),
            (0, 255, 0),
            1
        )

        HUD.draw_text(
            frame,
            f"Robot: {self.game.robot_move}",
            (40, 140),
            (255, 0, 0),
            1
        )

        HUD.draw_text(
            frame,
            self.game.result,
            (180, 240),
            (0, 0, 255),
            2
        )

        HUD.draw_text(
            frame,
            f"Jugador: {self.game.player_score}",
            (40, 340),
            (0, 255, 0),
            1
        )

        HUD.draw_text(
            frame,
            f"Robot: {self.game.robot_score}",
            (40, 390),
            (255, 0, 0),
            1
        )

        if time.time() - self.result_time >= 3:

            self.state = self.STATE_ASK_CONTINUE

    # ==========================================
    # CONTINUAR
    # ==========================================

    def draw_continue(self, frame):

        HUD.draw_text(
            frame,
            "Desea continuar?",
            (150, 180),
            (255, 255, 255),
            1.5
        )

        HUD.draw_text(
            frame,
            "ENTER = SI",
            (210, 260),
            (0, 255, 0),
            1
        )

        HUD.draw_text(
            frame,
            "ESC = NO",
            (220, 320),
            (0, 0, 255),
            1
        )

    # ==========================================
    # MAIN LOOP
    # ==========================================

    def run(self):

        while True:

            ret, frame = self.cap.read()
            frame = cv2.flip(frame, 1)

            if not ret:
                break

            key = cv2.waitKey(1)

            # ==========================================
            # MENU
            # ==========================================

            if self.state == self.STATE_MENU:

                self.draw_menu(frame)

                if key == 13:

                    self.reset_round()

                    self.state = self.STATE_COUNTDOWN

            # ==========================================
            # COUNTDOWN
            # ==========================================

            elif self.state == self.STATE_COUNTDOWN:

                self.handle_countdown(frame)

            # ==========================================
            # RESULT
            # ==========================================

            elif self.state == self.STATE_RESULT:

                self.draw_result(frame)

            # ==========================================
            # ASK CONTINUE
            # ==========================================

            elif self.state == self.STATE_ASK_CONTINUE:

                self.draw_continue(frame)

                if key == 13:

                    self.reset_round()

                    self.state = self.STATE_COUNTDOWN

            # ==========================================
            # EXIT
            # ==========================================

            if key == 27:
                break

            cv2.imshow(
                "RoboCachipun",
                frame
            )

        self.close()

    # ==========================================
    # CLOSE
    # ==========================================

    def close(self):

        self.cap.release()

        self.robot.close()

        cv2.destroyAllWindows()


if __name__ == "__main__":

    app = RoboCachipunApp()

    app.run()