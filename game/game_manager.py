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

    def play_round(self, player_move):

        self.player_move = player_move

        self.robot_move = random.choice(
            self.MOVES
        )

        self.result = self.get_result()

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