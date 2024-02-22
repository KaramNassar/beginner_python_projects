import os

from game import TicTacToe
from genius_computer_player import GeniusComputerPlayer
from human_player import HumanPlayer


# from computer_player import ComputerPlayer


def play(game, player_x, player_o, print_game=True):
    if print_game:
        game.print_board_nums()

    current_player = "X"

    while game.empty_squares():
        if current_player == "X":
            square = player_x.get_move(game)
        else:
            square = player_o.get_move(game)

        if game.make_move(square, current_player):
            if print_game:
                print(f"{current_player} makes a move to square {square}\n")
                game.print_board()
                print("")

            if game.current_winner:
                if print_game:
                    print(f"{current_player} wins!")
                return current_player

            current_player = "O" if current_player == "X" else "X"

    if print_game:
        print("It's a Tie!")


if __name__ == "__main__":
    x_score = 0
    o_score = 0
    ties = 0
    x_player = HumanPlayer("X")
    o_player = GeniusComputerPlayer("O")

    for i in range(1, 4):
        print(f"Stage {i}\n")
        t = TicTacToe()
        winner = play(t, x_player, o_player)
        if winner == "X":
            x_score += 1
        elif winner == "O":
            o_score += 1
        else:
            ties += 1
        os.system('cls')
        print(f"Winner of stage {i} is {winner}")

    print(f"Final result is:\n{x_score} X wins,\n{o_score} O wins,\n{ties} ties")
