from board import Board

class TreeNode():
    def __init__(self, value: Board, successors: list["TreeNode"]):
        self.value = value
        self.successors = successors
    

class MiniMaxTree():
    def __init__(self, root) -> None:
        self.root = root
