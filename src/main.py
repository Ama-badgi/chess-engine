from os import path
from board import Board

def main(board_path: str) -> None:
    board = Board()
    board.deserialize(board_path)
    white_score, black_score = board.evaluate()
    print(white_score)
    print(black_score)


if __name__ == "__main__":
    BOARDS_PATH = "../boards/"
    curr_board = "start.csv"
    main(path.normpath(BOARDS_PATH + curr_board))
