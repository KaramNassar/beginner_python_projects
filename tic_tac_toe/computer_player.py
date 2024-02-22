import random

from game import TicTacToe
from player import Player


class ComputerPlayer(Player):
    def get_move(self, game):
        """
        :type game: TicTacToe
        """
        return random.choice(game.available_moves())
