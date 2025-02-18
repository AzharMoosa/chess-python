import os
from os import sendfile
import sys
import yaml
from game_files.player import Player
from game_files.board import Board
from game_files.pieces import *
from game_files.player_one_valid import Valid_One
from game_files.player_two_valid import Valid_Two
from game_files.move import Move


class Game:

    # Global Variables
    saved_data = None
    turn = 0
    player_one = None
    player_two = None
    game_board = None
    opponent_player = None
    current_piece = 0
    starting_point = []
    valid = None

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
                self.openGame()
                self.turn = self.saved_data[0]
                self.player_one = self.saved_data[1]
                self.player_two = self.saved_data[2]
                self.game_board = self.saved_data[3]
                self.cls()
                self.start()
                break
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
            f"{self.player_one.name} - Black | {self.player_two.name} - White".center(50))

        # Create Board
        self.game_board = Board()

        # Add Pieces to Players
        self.add_pieces_one(self.player_one)
        self.add_pieces_two(self.player_two)

    def start(self):
        while True:
            # Update Board
            self.game_board.update_board(self.player_one, self.player_two)
            self.printLineBreak()

            # Print Board
            self.game_board.print_board()
            self.printLineBreak()

            # Determine Player Turns
            current_player = self.current_turn(
                self.player_one, self.player_two)
            self.opponent_player = self.opponent_turn(
                self.player_one, self.player_two)

            # Displays Current Turn
            print(f"{current_player.name}'s Turn".center(50))
            self.printLineBreak()

            # User Input for Position
            from_input = ""
            to_input = ""

            while True:
                from_input = input("From: ")
                if (from_input == "save"):
                    self.saveGame()
                    sys.exit(0)
                to_input = input("To: ")

                if (self.valid_from(from_input, current_player) and self.valid_to(to_input, current_player)):
                    break

            # Move Piece
            from_position = self.convert_position(from_input)
            to = self.convert_position(to_input)
            move = Move(from_position, to, self.game_board,
                        current_player, self.opponent_player, self.current_piece)

            # Next Turn
            if (move):
                self.next_turn()
                self.cls()

            # Check or Checkmate
            if (self.check_winner(to, self.game_board, current_player, self.opponent_player)):
                break

    def add_pieces_one(self, player_one):
        king = King("\u2654", [5, 8])
        queen = Queen("\u2655", [4, 8])
        rook_one = Rook("\u2656", [1, 8])
        rook_two = Rook("\u2656", [8, 8])
        bishop_one = Bishop("\u2657", [3, 8])
        bishop_two = Bishop("\u2657", [6, 8])
        knight_one = Knight("\u2658", [2, 8])
        knight_two = Knight("\u2658", [7, 8])
        player_one.pieces.extend((king, queen, rook_one, rook_two,
                                  bishop_one, bishop_two, knight_one, knight_two))

        # Pawns
        for i in range(0, 8):
            pawn = Pawn("\u2659", [i+1, 7])
            player_one.pieces.append(pawn)

    def add_pieces_two(self, player_two):
        king = King("\u265A", [5, 1])
        queen = Queen("\u265B", [4, 1])
        rook_one = Rook("\u265C", [1, 1])
        rook_two = Rook("\u265C", [8, 1])
        bishop_one = Bishop("\u265D", [3, 1])
        bishop_two = Bishop("\u265D", [6, 1])
        knight_one = Knight("\u265E", [2, 1])
        knight_two = Knight("\u265E", [7, 1])
        player_two.pieces.extend((king, queen, rook_one, rook_two,
                                  bishop_one, bishop_two, knight_one, knight_two))

        # Pawns
        for i in range(0, 8):
            pawn = Pawn("\u265F", [i+1, 2])
            player_two.pieces.append(pawn)

    def current_turn(self, player_one, player_two):
        # Determine Who is Current Player
        if (self.turn == 0):
            return player_one
        elif (self.turn == 1):
            return player_two
        else:
            return -1

    def opponent_turn(self, player_one, player_two):
        # Determine Who is Opponent Player
        if (self.turn == 0):
            return player_two
        elif (self.turn == 1):
            return player_one
        else:
            return -1

    def next_turn(self):
        # Next Turn
        if (self.turn == 0):
            self.turn = 1
        elif (self.turn == 1):
            self.turn = 0

    def saveGame(self):
        self.saved_data = [self.turn, self.player_one,
                           self.player_two, self.game_board]
        with open("./saved_game/saved_data.yaml", "w") as file:
            yaml.dump(self.saved_data, file)
        self.printLineBreak()
        print("Type 'open' to Resume Game".center(50))
        self.printLineBreak()

    def openGame(self):
        with open("./saved_game/saved_data.yaml") as file:
            self.saved_data = yaml.full_load(file)

    def convert_position(self, position):
        # Split Position into List
        position_array = list(position)
        # Convert Letter to Number
        letter_to_number = ord(position_array[0]) - 96
        # Return Position in Numbers
        return [int(letter_to_number), int(position_array[1])]

    def valid_from(self, from_point, current_player):
        # Check If Input Is Valid
        if (len(from_point) != 2 or from_point == ""):
            return False

        # Convert Coords
        coord = self.convert_position(from_point)

        # Check If Coords is Between 1 and 8
        if (coord[0] >= 1 and coord[0] <= 8 and coord[1] >= 1 and coord[1] <= 8):
            players_pieces = current_player.pieces
            for i in range(0, len(players_pieces)):
                if (players_pieces[i].current_position == coord):
                    self.current_piece = i
                    self.starting_point = coord
                    return True

        return False

    def valid_to(self, to, current_player):
        # Check If Input Is Valid
        if (len(to) != 2 or to == ""):
            return False

        # Convert Coords
        coord = self.convert_position(to)

        # Input Out of Range
        if (coord[0] < 1 and coord[0] > 8 and coord[1] < 1 and coord[1] > 8):
            return False

        # Get Current Piece
        player_pieces = current_player.pieces
        piece = player_pieces[self.current_piece]

        # Use Correct Validity Checker
        if (current_player == self.player_one):
            self.valid = Valid_One(self.starting_point, coord)
        elif (current_player == self.player_two):
            self.valid = Valid_Two(self.starting_point, coord)

        # Check Validity Of Move
        if (self.valid.pawn(piece, self.opponent_player.pieces, self.game_board)):
            return True
        elif (self.valid.knight(piece, self.opponent_player.pieces, self.game_board)):
            return True
        elif (self.valid.queen(piece, self.opponent_player.pieces, self.game_board)):
            return True
        elif (self.valid.bishop(piece, self.opponent_player.pieces, self.game_board)):
            return True
        elif (self.valid.rook(piece, self.opponent_player.pieces, self.game_board)):
            return True
        elif (self.valid.king(piece, self.opponent_player.pieces, self.game_board)):
            return True

        return False

    def check_winner(self, to, game_board, current_player, opponent_player):
        moves = [[0, 1], [1, 0], [0, -1], [-1, 0],
                 [1, 1], [-1, -1], [-1, 1], [1, -1]]
        valid_moves = []
        king_position = []
        current_player_pieces = current_player.pieces
        opponent_player_pieces = opponent_player.pieces

        for piece in opponent_player_pieces:
            if (piece.name == "king"):
                king_position = piece.current_position

        if (not king_position):
            print(f"{current_player.name} Wins!")
            return True

        x1 = king_position[0]
        y1 = king_position[1]
        board = game_board.get_board()

        for move in moves:
            x2 = x1 + move[0]
            y2 = y1 + move[1]
            if (x2 > 0 and x2 < 9 and y2 > 0 and y2 < 9 and board[y2 - 1][x2 - 1] == " "):
                valid_moves += [move]

        possible_count = 0
        valid_moves_length = len(valid_moves)

        for move in valid_moves:
            x2 = x1 + move[0]
            y2 = y1 + move[1]
            coord = [x2, y2]
            players_pieces = current_player_pieces
            for piece in players_pieces:
                if (current_player == self.player_one):
                    self.valid = Valid_One(piece.current_position, coord)
                elif (current_player == self.player_two):
                    self.valid = Valid_Two(piece.current_position, coord)

                if (self.valid.pawn(piece, self.opponent_player.pieces, self.game_board)):
                    possible_count += 1
                elif (self.valid.knight(piece, self.opponent_player.pieces, self.game_board)):
                    possible_count += 1
                elif (self.valid.queen(piece, self.opponent_player.pieces, self.game_board)):
                    possible_count += 1
                elif (self.valid.bishop(piece, self.opponent_player.pieces, self.game_board)):
                    possible_count += 1
                elif (self.valid.rook(piece, self.opponent_player.pieces, self.game_board)):
                    possible_count += 1
                elif (self.valid.king(piece, self.opponent_player.pieces, self.game_board)):
                    possible_count += 1

        # If King is Surrounded
        if (len(valid_moves) == 0):
            return False

        if (possible_count == valid_moves_length):
            print(f"Checkmate\n{current_player.name} Wins!")
            return True

        if (possible_count > 0):
            print("Check")

        return False


chess_game = Game()
