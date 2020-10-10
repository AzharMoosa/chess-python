class Game:
    def __init__(self):
        self.saved_data = []
        self.printMenu()

    def printLineBreak(self):
        print("=================================================")

    def printMenu(self):
        self.printLineBreak()
        print("Welcome to Chess".center(50))
        self.printLineBreak()
        print("Instructions: \n* Type a Position, e.g a5\n* Player 1 Goes First\n* Win by Defeating King\n* To Save During Game Type 'save'")
        self.printLineBreak()
        print("* Type 'start' To Begin Playing\n* Type 'open' To Open Saved Game\n* Type 'save' During Game To Save Game\n* Type 'rules' To Display Rules of Chess\n* Type 'quit' To Quit")
        self.printLineBreak()


chess_game = Game()
