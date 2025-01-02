import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        """
        Initialize the TicTacToe game.

        Args:
        - root: The Tkinter root window.
        """
        self.root = root
        self.root.title("Tic Tac Toe")
        
        self.turn = "X"  # Start with player X
        self.board = [" " for _ in range(9)]  # Empty board
        self.buttons = []  # List to store the button widgets
        
        # Create the game buttons and display them
        self.create_buttons()

    def create_buttons(self):
        """
        Create and arrange the 3x3 grid of buttons for the Tic Tac Toe game.
        
        Each button corresponds to a cell in the game grid. The buttons are arranged 
        in a 3x3 grid layout using Tkinter's grid system. Each button is initialized 
        with a light blue background, and when clicked, it triggers the `handle_click` method.
        """
        for i in range(9):
            button = tk.Button(self.root, text=" ", font=("Arial", 24), width=5, height=2,
                               bg="#ADD8E6", activebackground="#87CEEB", 
                               command=lambda i=i: self.handle_click(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

    def handle_click(self, i):
        """
        Handles the logic when a player clicks a cell on the grid.

        Args:
        - i: The index of the clicked cell (0-8).
        """
        # Only process the click if the cell is empty and no winner exists yet
        if self.board[i] == " " and not self.check_winner():
            self.board[i] = self.turn
            
            # Set the text color based on the current player
            text_color = "green" if self.turn == "X" else "red"
            self.buttons[i].config(text=self.turn, fg=text_color)

            # Check if there is a winner
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.turn} wins!")
            # Check for a draw
            elif " " not in self.board:
                messagebox.showinfo("Game Over", "It's a draw!")
            else:
                # Switch turns between "X" and "O"
                self.turn = "O" if self.turn == "X" else "X"

    def check_winner(self):
        """
        Checks if there is a winner in the game.
        
        Returns:
        - True if there is a winner, otherwise False.
        """
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)   # Diagonals
        ]
        
        # Check all possible winning conditions (rows, columns, diagonals)
        for a, b, c in win_conditions:
            if self.board[a] == self.board[b] == self.board[c] != " ":
                # Highlight the winning cells by changing the background color
                self.buttons[a].config(bg="yellow")
                self.buttons[b].config(bg="yellow")
                self.buttons[c].config(bg="yellow")
                return True
        return False

if __name__ == "__main__":
    # Create the main Tkinter window and start the game
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
