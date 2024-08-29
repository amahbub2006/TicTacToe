import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")

        self.current_player = 'X'
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        self.create_board()

    def create_board(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.root, text=' ', font=('Arial', 24), width=5, height=2,
                                   command=lambda r=row, c=col: self.make_move(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            if self.check_winner(self.current_player):
                messagebox.showinfo("Tic-Tac-Toe", f"Player {self.current_player} wins!")
                self.reset_board()
            elif self.check_draw():
                messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
                self.reset_board()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self, player):
        # Check rows, columns, and diagonals for a win
        for row in range(3):
            if all([self.board[row][col] == player for col in range(3)]):
                return True

        for col in range(3):
            if all([self.board[row][col] == player for row in range(3)]):
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player or \
           self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True

        return False

    def check_draw(self):
        return all([self.board[row][col] != ' ' for row in range(3) for col in range(3)])

    def reset_board(self):
        self.current_player = 'X'
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text=' ')

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
  
