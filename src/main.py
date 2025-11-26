from os import path
from board import Board
from minimax import MiniMaxTree, TreeNode

BOARDS_PATH = "../boards/"


def build_minimax_tree(board: Board) -> MiniMaxTree:
    pass


def alpha_beta(node: TreeNode, alpha: int, beta: int, depth: int=0) -> int:
    pass


def main() -> None:
    curr_board = "start.csv"

    board = Board()
    board.deserialize(path.normpath(BOARDS_PATH + curr_board))

    minimax_tree = build_minimax_tree(board)
    best_node_idx = alpha_beta(minimax_tree.root, alpha=-500, beta=500)
    # TODO - send game instruction


if __name__ == "__main__":
    main()
