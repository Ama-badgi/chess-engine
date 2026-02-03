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


PIECE_MAP = {
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

VALUE_MAP = {
    GamePiece.PAWN: 1,
    GamePiece.KING: 200,
    GamePiece.QUEEN: 9,
    GamePiece.ROOK: 5,
    GamePiece.KNIGHT: 3,
    GamePiece.BISHOP: 3 
}

LOWER_A_ASCII_OFFSET = ord("a")


class Board:
    """
    Class to represent the board of the game

    board: list[list[ColoredPiece | None]] -> matrix representation of the current board state
    player_color: Color -> color of the player being controlled
    weights: list[list[int]] -> weights representing board control
    """
    def __init__(self, player_color,
                 board: list[list[ColoredPiece | None]]=[[None for _ in range(8)] for _ in range(8)]):
        self.board: list[list[ColoredPiece | None]] = board
        self.player_color: Color = player_color
        self.weights: list[list[int]] = [[1 for _ in range(8)] for _ in range(8)]
    
    def deserialize(self, board_path: str) -> None:
        with open(board_path, mode="r", encoding="utf-8") as csv:
            text = csv.read()
        split_pieces = text.split(",")
        for piece in split_pieces:
            self.board[int(piece[2]) - 1][ord(piece[1]) - LOWER_A_ASCII_OFFSET] = PIECE_MAP.get(piece[0])
