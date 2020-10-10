class Valid_One:
    # Global Variables
    x1 = None
    y1 = None
    x2 = None
    y2 = None
    dx = None
    dy = None

    def __init__(self, starting_point, ending_point):
        self.x1 = starting_point[0]
        self.y1 = starting_point[1]
        self.x2 = ending_point[0]
        self.y2 = ending_point[1]
        self.dx = self.x2 - self.x1
        self.dy = self.y2 - self.y1

    def pawn(self, piece, opponent, game_board):
        # Check Name
        if (piece.name != "pawn"):
            return False

        board = game_board.get_board()
        for piece in opponent:
            if (board[self.y2 - 1][self.x2 - 1] == piece.symbol and ((self.dy == 1 and self.dx == 1) or (self.dy == 1 and self.dx == -1))):
                return True
            elif (board[self.y2 - 1][self.x2 - 1] == " " and self.dy == 1 and self.dx == 0):
                return True

        return False

    def knight(piece, opponent, game_board):
        # Check Name
        if (piece.name != "knight"):
            return False

    def bishop(piece, opponent, game_board):
        # Check Name
        if (piece.name != "bishop"):
            return False

    def queen(piece, opponent, game_board):
        # Check Name
        if (piece.name != "queen"):
            return False

    def king(piece, opponent, game_board):
        # Check Name
        if (piece.name != "king"):
            return False

    def rook(piece, opponent, game_board):
        # Check Name
        if (piece.name != "rook"):
            return False
