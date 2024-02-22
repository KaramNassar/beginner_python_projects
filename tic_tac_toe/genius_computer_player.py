import math
import random

from game import TicTacToe
from player import Player


class GeniusComputerPlayer(Player):
    def get_move(self, game):
        """
        :type game: TicTacToe
        """
        if game.empty_squares_num() == game.size ** 2:
            square = random.choice(game.available_moves())
        else:
            square = self.minimax(game, self.letter)["position"]

        return square

    def minimax(self, state, player):
        max_player = self.letter
        other_player = 'X' if player == 'O' else 'O'

        if state.current_winner == other_player:
            return {
                "position": None,
                "score": 1 * (state.empty_squares_num() + 1) if other_player == max_player
                else -1 * (state.empty_squares_num() + 1)
            }

        elif not state.empty_squares():
            return {
                "position": None,
                "score": 0
            }

        if player == max_player:
            best = {
                "position": None,
                "score": -math.inf
            }
        else:
            best = {
                "position": None,
                "score": math.inf
            }

        for possible_move in state.available_moves():
            state.make_move(possible_move, player)

            sim_score = self.minimax(state, other_player)

            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score["position"] = possible_move

            # 4. Update the dictionary if necessary
            if player == max_player:
                if sim_score["score"] > best["score"]:
                    best = sim_score

            else:
                if sim_score["score"] < best["score"]:
                    best = sim_score

        return best
