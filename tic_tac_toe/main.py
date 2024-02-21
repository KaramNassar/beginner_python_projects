from computer_player import ComputerPlayer
from game import TicTacToe
from human_player import HumanPlayer


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
                print(f"{current_player} makes a move to square {square}")
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
    x_player = HumanPlayer('X')
    o_player = ComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player)
