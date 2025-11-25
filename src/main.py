from board import Board

def main(board_path: str) -> None:
    board = Board()
    board.deserialize(board_path)
    board.evaluate_board()


if __name__ == "__main__":
    BOARD_PATH = "../boards/"
    curr_board = ""
    main(BOARD_PATH + curr_board)
