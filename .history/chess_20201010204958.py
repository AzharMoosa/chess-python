import os
from os import sendfile
import sys
from game_files.player import Player
from game_files.board import Board
from game_files.pieces import *


class Game:

    # Global Variables
    saved_data = None
    turn = 0
    player_one = None
    player_two = None
    game_board = None

    def __init__(self):
        self.printMenu()

    def cls(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def printLineBreak(self, n=50):
        print("=" * n)

    def printMenu(self):
        # Print Menu
        self.printLineBreak()
        print("Welcome to Chess".center(50))
        self.printLineBreak()
        print("Instructions: \n* Type a Position, e.g a5\n* Player 1 Goes First\n* Win by Defeating King\n* To Save During Game Type 'save'")
        self.printLineBreak()
        print("* Type 'start' To Begin Playing\n* Type 'open' To Open Saved Game\n* Type 'save' During Game To Save Game\n* Type 'rules' To Display Rules of Chess\n* Type 'quit' To Quit")
        self.printLineBreak()

        while True:
            # Read User's Input
            user_input = input("Enter Your Input: ").lower()

            # Start Game
            if (user_input == "start"):
                self.initialize_game()
                self.start()
                break
            # Open Previous Game
            elif (user_input == "open"):
                print("TODO")
            # Display Rules
            elif (user_input == "rules"):
                self.rules()
            # Quit Game
            elif (user_input == "quit"):
                self.printLineBreak()
                print("Goodbye!".center(50))
                self.printLineBreak()
                sys.exit(0)
                break

    def rules(self):
        # Rules of Chess
        self.printLineBreak()
        print("Rules of Chess".center(50))
        self.printLineBreak()
        print("* King: Can Move 1 Square Horizontally, Vertically or Diagonally")
        print(
            "* Queen: Can Move Any Number of Squares Horizontally, Vertically or Diagonally")
        print("* Rook: Can Move Any Number of Squares Horizontally or Vertically")
        print("* Bishop: Can Move Any Number of Squares Diagonally")
        print("* Knight: Can Move In A L-Shape of 1 Square by 2")
        print("* Pawns: Can Move One Square Forward. Can Only Capture Enemy Piece 1 Square Diagonally")
        self.printLineBreak()

    def initialize_game(self):
        self.printLineBreak()
        # Get Players Name
        player_one_name = input("Name of Player One: ")
        player_two_name = input("Name of Player Two: ")

        # Create Players
        self.player_one = Player(player_one_name)
        self.player_two = Player(player_two_name)

        # Init Game
        self.cls()
        self.printLineBreak()
        print(
            f"{self.player_one.name} - White | {self.player_two.name} - Black".center(50))

        # Create Board
        self.game_board = Board()

        # Add Pieces to Players

    def start(self):
        while True:
            self.printLineBreak()
            self.game_board.print_board()
            break

    def add_pieces_one(self, player_one):
        king = King("\u2654", [5, 1])
        queen = Queen("\u2655", [4, 1])
        rook_one = Rook("\u2656", [1, 1])
        rook_two = Rook("\u2656", [8, 1])
        bishop_one = Bishop("\u2657", [3, 1])
        bishop_two = Bishop("\u2657", [6, 1])
        knight_one = Knight("\u2658", [2, 1])
        knight_two = Knight("\u2658", [7, 1])
        player_one.pieces.push(king, queen, rook_one, rook_two,
                               bishop_one, bishop_two, knight_one, knight_two)
        # Pawns
        for i in range(0, 8):
            pawn = Pawn("\u2659", [i+1, 2])
            player_one.pieces.push(pawn)


chess_game = Game()
