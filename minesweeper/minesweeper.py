import re

from board import Board


def play(dim_size=10, num_bombs=10):
    board = Board(dim_size, num_bombs)

    safe = True

    while len(board.dug) < board.dim_size ** 2 - num_bombs:
        print(board)
        try:
            user_input = re.split(',(\\s)*', input("Where would you like to dig? input as row, col:"))
            row, col = int(user_input[0]), int(user_input[-1])
        except ValueError:
            print("Invalid input, please try again!")
            continue

        if row < 0 or row >= board.dim_size or col < 0 or col >= board.dim_size:
            print("Invalid")
            continue

        safe = board.dig(row, col)

        if not safe:
            break

    if safe:
        print("You won!")
    else:
        print("You lost!")
        board.dug = [(r, c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)


if __name__ == "__main__":
    play()
