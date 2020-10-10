class King:
    def __init__(self, symbol, current_position):
        self.name = "king"
        self.possible_moves = [[0, 1], [0, 1], [0, -1],
                               [-1, 0], [1, 1], [-1, -1], [-1, 1], [1, -1]]
        self.current_position = current_position
        self.symbol = symbol
        self.alive = True


class Pawn:
    def __init__(self, symbol, current_position):
        self.name = "pawn"
        self.possible_moves = [[0, 1]]
        self.capture_moves = [[1, -1], [1, 1]]
        self.current_position = current_position
        self.symbol = symbol
        self.alive = True


class Queen:
    def __init__(self, symbol, current_position):
        self.name = "queen"
        self.current_position = current_position
        self.symbol = symbol
        self.alive = True


class Bishop:
    def __init__(self, symbol, current_position):
        self.name = "bishop"
        self.current_position = current_position
        self.symbol = symbol
        self.alive = True


class Rook:
    def __init__(self, symbol, current_position):
        self.name = "rook"
        self.current_position = current_position
        self.symbol = symbol
        self.alive = = True


class Knight:
    def __init__(self, symbol, current_position):
        self.name = "knight"
        self.possible_moves = [[1, 2], [2, 1], [2, -1],
                               [1, -2], [-1, 2], [-2, -1], [-2, 1], [-1, -2]]
        self.current_position = current_position
        self.symbol = symbol
        self.alive = alive
