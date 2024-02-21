class TicTacToe:
    size = 5

    def __init__(self):
        self.board = [" " for _ in range(TicTacToe.size ** 2)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i * TicTacToe.size:(i + 1) * TicTacToe.size] for i in range(TicTacToe.size)]:
            print("| " + " | ".join(row) + " |")

    @staticmethod
    def print_board_nums():
        number_board = [str(i) for i in range(TicTacToe.size ** 2)]
        for row in [number_board[i * TicTacToe.size:(i + 1) * TicTacToe.size] for i in range(TicTacToe.size)]:
            row = [" " + cell + " " if len(cell) < 2 else " " + cell for cell in row]
            print("| " + " | ".join(row) + " |")

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == " "]

    def empty_squares(self):
        return " " in self.board

    def empty_squares_num(self):
        return self.board.count(" ")

    def make_move(self, square, current_player):
        if self.board[square] == " ":
            self.board[square] = current_player
            if self.winner(square, current_player):
                self.current_winner = current_player
            return True

        return False

    def winner(self, square, current_player):
        row_ind = square // TicTacToe.size
        row = self.board[row_ind * TicTacToe.size:(row_ind + 1) * TicTacToe.size]
        if all([spot == current_player for spot in row]):
            return True

        col_ind = square % TicTacToe.size
        col = [self.board[col_ind + i * TicTacToe.size] for i in range(TicTacToe.size)]
        if all([spot == current_player for spot in col]):
            return True

        diagonal1 = [self.board[i] for i in [(TicTacToe.size + 1) * j for j in range(TicTacToe.size)]]
        if all([spot == current_player for spot in diagonal1]):
            return True

        diagonal2 = [self.board[i] for i in [(TicTacToe.size - 1) * j for j in range(1, TicTacToe.size + 1)]]
        if all([spot == current_player for spot in diagonal2]):
            return True

        return False
