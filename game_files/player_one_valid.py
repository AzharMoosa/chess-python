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

        # Get Game Board
        board = game_board.get_board()

        # Check Validity Move
        for piece in opponent:
            if (board[self.y2 - 1][self.x2 - 1] == piece.symbol and ((self.dy == -1 and self.dx == 1) or (self.dy == -1 and self.dx == -1))):
                return True
            elif (board[self.y2 - 1][self.x2 - 1] == " " and self.dy == -1 and self.dx == 0):
                return True

        return False

    def knight(self, piece, opponent, game_board):
        # Check Name
        if (piece.name != "knight"):
            return False

        # Get Game Board
        board = game_board.get_board()

        # Check Validity Move
        for move in piece.possible_moves:
            for piece in opponent:
                if (move[0] == self.dx and move[1] == self.dy and board[self.y2 - 1][self.x2 - 1] == " "):
                    return True
                elif (board[self.y2 - 1][self.x2 - 1] == piece.symbol and move[0] == self.dx and move[1] == self.dy):
                    return True

    def bishop(self, piece, opponent, game_board):
        # Check Name
        if (piece.name != "bishop"):
            return False

        # Get Game Board
        board = game_board.get_board()

        # Check Validity Move
        for piece in opponent:
            if (abs(self.dy) == abs(self.dx) and board[self.y2 - 1][self.x2 - 1] == " "):
                return True
            elif (board[self.y2 - 1][self.x2 - 1] == piece.symbol and abs(self.dy) == abs(self.dx)):
                return True

        return False

    def queen(self, piece, opponent, game_board):
        # Check Name
        if (piece.name != "queen"):
            return False

        # Get Game Board
        board = game_board.get_board()

        # Check Validity Move
        if (self.dx == 0 or self.dy == 0 or abs(self.dx) == abs(self.dy)):
            dirX = 0 if (self.dx == 0) else 1
            dirY = 0 if (self.dy == 0) else 1
            length = self.dy if (self.dx == 0) else self.dx

            dirX = 1 if (self.x2 > self.x1) else -1
            dirY = 1 if (self.y2 > self.y1) else -1

            if (self.dx == 0):
                dirX = 0
                dirY = -1
            elif (self.dy == 0):
                dirX = -1
                dirY = 0
            for i in range(1, abs(length) + 1):
                if (board[self.y1 + i * dirY - 1][self.x1 + i * dirX - 1] != " "):
                    return False
        else:
            return False
        print("ss")
        for piece in opponent:
            if (board[self.y2 - 1][self.x2 - 1] == " "):
                return True
            elif (board[self.y2 - 1][self.x2 - 1] == piece.symbol):
                return True

        return False

    def king(self, piece, opponent, game_board):
        # Check Name
        if (piece.name != "king"):
            return False

        # Get Game Board
        board = game_board.get_board()

        # Check Validity Move
        for move in piece.possible_moves:
            for piece in opponent:
                if (move[0] == self.dx and move[1] == self.dy and board[self.y2 - 1][self.x2 - 1] == " "):
                    return True
                elif (board[self.y2 - 1][self.x2 - 1] == piece.symbol and move[0] == self.dx and move[1] == self.dy):
                    return True

        return False

    def rook(self, piece, opponent, game_board):
        # Check Name
        if (piece.name != "rook"):
            return False

        # Get Game Board
        board = game_board.get_board()

        # Check Validity Move
        dirX = 0 if (self.dx == 0) else -1
        dirY = 0 if (self.dy == 0) else -1
        length = self.dy if (self.dx == 0) else self.dx

        for i in range(1, abs(length) + 1):
            if (board[self.y1 + i * dirY - 1][self.x1 + i * dirX - 1] != " "):
                return False

        for piece in opponent:
            if (self.dy == 0 and board[self.y2 - 1][self.x2 - 1] == " "):
                return True
            elif (self.dx == 0 and board[self.y2 - 1][self.x2 - 1] == " "):
                return True
            elif (board[self.y2 - 1][self.x2 - 1] == piece.symbol and self.dx == 0):
                return True
            elif (board[self.y2 - 1][self.x2 - 1] == piece.symbol and self.dy == 0):
                return True

        return False
