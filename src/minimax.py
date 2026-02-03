from board import Board

class TreeNode():
    def __init__(self, board: Board, successors: list["TreeNode"]):
        self.board = board
        self.successors = successors
    

class MiniMaxTree():
    def __init__(self, root) -> None:
        self.root = root


def alpha_beta(node: TreeNode, alpha: int, beta: int) -> int:
    pass

def build_tree(board: Board, depth: int=0) -> MiniMaxTree:
    pass

def build_node(board: Board, depth: int) -> TreeNode:
    pass
