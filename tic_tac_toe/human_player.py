from game import TicTacToe
from player import Player


class HumanPlayer(Player):
    def get_move(self, game):
        """
        :type game: TicTacToe
        """
        valid_move = False
        move = None

        while not valid_move:
            move = input(f"{self.letter}'s turn. Enter your move (0-{(game.size ** 2) - 1}): ")
            print("")
            try:
                move = int(move)
                if move not in game.available_moves():
                    raise ValueError
                valid_move = True
            except ValueError:
                print("Invalid move please try again\n")

        return move
