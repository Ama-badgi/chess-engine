from enum import Enum

class GamePiece(Enum):
    PAWN = 0,
    KNIGHT = 1,
    BISHOP = 2,
    ROOK = 3,
    QUEEN = 4,
    KING = 5

class Board:
    def __init__(self):
        self.board: list[list[GamePiece]] = [[] for _ in range()]
    
    def deserialize(self):
        pass

    def evaluate_board(self) -> int:
        pass