import random


class GameManager:

    MOVES = [
        "rock",
        "paper",
        "scissors"
    ]

    RESULTS = {

        ("rock", "scissors"): "GANASTE",
        ("rock", "paper"): "PERDISTE",

        ("paper", "rock"): "GANASTE",
        ("paper", "scissors"): "PERDISTE",

        ("scissors", "paper"): "GANASTE",
        ("scissors", "rock"): "PERDISTE"
    }

    def __init__(self):

        self.player_move = ""

        self.robot_move = ""

        self.result = ""

        self.player_score = 0

        self.robot_score = 0

    def play_round(self, player_move):

        self.player_move = player_move

        self.robot_move = random.choice(
            self.MOVES
        )

        self.result = self.get_result()

        self.update_score()

        return {
            "player": self.player_move,
            "robot": self.robot_move,
            "result": self.result
        }

    def get_result(self):

        if self.player_move == self.robot_move:
            return "EMPATE"

        return self.RESULTS.get(
            (self.player_move, self.robot_move),
            "ERROR"
        )

    def update_score(self):

        if self.result == "GANASTE":

            self.player_score += 1

        elif self.result == "PERDISTE":

            self.robot_score += 1