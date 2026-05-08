import random

class RockPaperScissors:
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    def get_ai_move(self):
        return random.choice([1, 2, 3])

    def get_winner(self, player, ai):
        if player == ai:
            return "Empate"
        elif (player == 1 and ai == 3) or \
             (player == 2 and ai == 1) or \
             (player == 3 and ai == 2):
            return "Jugador gana"
        else:
            return "IA gana"

    def fingers_to_move(self, fingers):
        """
        Mapear dedos a jugada:
        0 dedos -> piedra
        2 dedos -> tijera
        5 dedos -> papel
        """
        total = sum(fingers)

        if total == 0:
            return self.ROCK
        elif total == 2:
            return self.SCISSORS
        elif total == 5:
            return self.PAPER
        else:
            return None