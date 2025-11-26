from board import Board

class TreeNode():
    def __init__(self, value: int, successors: list["TreeNode"], move: str, board: Board):
        self.value = value
        self.successors = successors

        self.move = move
        self.board = board
    

class MiniMaxTree():
    def __init__(self, root) -> None:
        self.root = root
