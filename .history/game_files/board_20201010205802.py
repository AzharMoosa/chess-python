class Board:

    # Global Variables
    game_board = None

    def __init__(self):
        self.game_board = [[" ", " ", " ", " ", " ", " ", " ", " "],
                           [" ", " ", " ", " ", " ", " ", " ", " "],
                           [" ", " ", " ", " ", " ", " ", " ", " "],
                           [" ", " ", " ", " ", " ", " ", " ", " "],
                           [" ", " ", " ", " ", " ", " ", " ", " "],
                           [" ", " ", " ", " ", " ", " ", " ", " "],
                           [" ", " ", " ", " ", " ", " ", " ", " "],
                           [" ", " ", " ", " ", " ", " ", " ", " "]]

    def get_board(self):
        # Return Game Board
        return self.game_board

    def set_board(self, y, x):
        # Set Board to Empty
        self.game_board[y - 1][x - 1] = " "

    def print_board(self):
        # Print Axis
        count = 1
        display_board = ""
        for row in self.game_board:
            display_board += f"{count} "
            display_board += "|"
            for i in range(0, 8):
                display_board += f" {row[i]} |"
            count += 1
            display_board += "\n"
        display_board += "    a  b  c  d  e  f  g  h"
        print(display_board)

    def update_board(self, player_one, player_two):
        # Update Player One's Pieces
        for piece in player_one.pieces:
            x = piece.current_position[0] - 1
            y = piece.current_position[1] - 1
            self.game_board[y][x] = piece.symbol

        # Update Player Two's Pieces
        for piece in player_two.pieces:
            x = piece.current_position[0] - 1
            y = piece.current_position[1] - 1
            self.game_board[y][x] = piece.symbol
