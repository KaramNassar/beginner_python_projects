import random

from player import Player


class ComputerPlayer(Player):
    def get_move(self, game):
        return random.choice(game.available_moves())
