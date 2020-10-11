class Move:
    def __init__(self, from_point, to, game_board, current_player, opponent_player, current_piece):
        self.x = from_point[0]
        self.y = from_point[1]
        self.to = to
        self.game_board = game_board
        self.current_player = current_player
        self.opponent_player = opponent_player
        self.current_piece = current_piece
        self.move()

    def move(self):
        # Check If Opponents Piece is in Square
        for piece in self.opponent_player.pieces:
            if (self.to == piece.current_position):
                self.opponent_player.pieces.remove(piece)

        # Clear Board at Position
        self.game_board.set_board(self.y, self.x)

        # Move Current Piece to Position
        players_pieces = self.current_player.pieces
        piece = players_pieces[self.current_piece]
        piece.current_position = self.to
