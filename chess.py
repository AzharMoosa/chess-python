class Game:

    # Global Variables
    saved_data = None
    turn = None
    player_one = None
    player_two = None
    game_board = None

    def __init__(self):
        self.printMenu()

    def printLineBreak(self, n):
        print("=" * n)

    def printMenu(self):
        # Print Menu
        self.printLineBreak(50)
        print("Welcome to Chess".center(50))
        self.printLineBreak(50)
        print("Instructions: \n* Type a Position, e.g a5\n* Player 1 Goes First\n* Win by Defeating King\n* To Save During Game Type 'save'")
        self.printLineBreak(50)
        print("* Type 'start' To Begin Playing\n* Type 'open' To Open Saved Game\n* Type 'save' During Game To Save Game\n* Type 'rules' To Display Rules of Chess\n* Type 'quit' To Quit")
        self.printLineBreak(50)

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
            elif (user_input == "quit" or "q"):
                self.printLineBreak(50)
                print("Goodbye!".center(50))
                self.printLineBreak(50)
                break

    def rules(self):
        # Rules of Chess
        self.printLineBreak(50)
        print("Rules of Chess".center(50))
        self.printLineBreak(50)
        print("* King: Can Move 1 Square Horizontally, Vertically or Diagonally")
        print(
            "* Queen: Can Move Any Number of Squares Horizontally, Vertically or Diagonally")
        print("* Rook: Can Move Any Number of Squares Horizontally or Vertically")
        print("* Bishop: Can Move Any Number of Squares Diagonally")
        print("* Knight: Can Move In A L-Shape of 1 Square by 2")
        print("* Pawns: Can Move One Square Forward. Can Only Capture Enemy Piece 1 Square Diagonally")
        self.printLineBreak(50)

    def initialize_game(self):
        self.printLineBreak(50)

    def start(self):
        while True:
            break


chess_game = Game()
