from enum import Enum

class Color(Enum):
    WHITE = 0,
    BLACK = 1,


class GamePiece(Enum):
    PAWN = 0,
    KNIGHT = 1,
    BISHOP = 2,
    ROOK = 3,
    QUEEN = 4,
    KING = 5


class ColoredPiece:
    def __init__(self, piece: GamePiece, color: Color) -> None:
        self.piece = piece
        self.color = color


PIECE_LOOKUP_TABLE = {
    "♙": ColoredPiece(GamePiece.PAWN, Color.WHITE),
    "♔": ColoredPiece(GamePiece.KING, Color.WHITE),
    "♕": ColoredPiece(GamePiece.QUEEN, Color.WHITE),
    "♖": ColoredPiece(GamePiece.ROOK, Color.WHITE),
    "♘": ColoredPiece(GamePiece.KNIGHT, Color.WHITE),
    "♗": ColoredPiece(GamePiece.BISHOP, Color.WHITE),
    "♟": ColoredPiece(GamePiece.PAWN, Color.BLACK),
    "♚": ColoredPiece(GamePiece.KING, Color.BLACK),
    "♛": ColoredPiece(GamePiece.QUEEN, Color.BLACK),
    "♜": ColoredPiece(GamePiece.ROOK, Color.BLACK),
    "♞": ColoredPiece(GamePiece.KNIGHT, Color.BLACK),
    "♝": ColoredPiece(GamePiece.BISHOP, Color.BLACK)
}
VALUE_LOOKUP_TABLE = {
    GamePiece.PAWN: 1,
    GamePiece.KING: 200,
    GamePiece.QUEEN: 9,
    GamePiece.ROOK: 5,
    GamePiece.KNIGHT: 3,
    GamePiece.BISHOP: 3 
}
LOWER_A_ASCII_OFFSET = ord("a")


class Board:
    def __init__(self):
        self.board: list[list[ColoredPiece | None]] = [[None for _ in range(8)] for _ in range(8)]
    
    def deserialize(self, board_path: str) -> None:
        with open(board_path, mode="r", encoding="utf-8") as csv:
            text = csv.read()
        split_pieces = text.split(",")
        for piece in split_pieces:
            self.board[int(piece[2]) - 1][ord(piece[1]) - LOWER_A_ASCII_OFFSET] = PIECE_LOOKUP_TABLE.get(piece[0])

    def evaluate(self) -> tuple[int, int]:
        white_count = 0
        black_count = 0
        for x in range(8):
            for y in range(8):
                curr_piece = self.board[x][y]
                if curr_piece is None:
                    pass
                elif curr_piece.color == Color.WHITE:
                    white_count += VALUE_LOOKUP_TABLE.get(curr_piece.piece)
                else:
                    black_count += VALUE_LOOKUP_TABLE.get(curr_piece.piece)
        return white_count, black_count
