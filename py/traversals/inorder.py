"""
                1
        2               3
    4       5       6       7

    inorder: 4 2 5 1 6 3 7
"""


from typing import Optional
from dataclasses import dataclass


@dataclass
class TreeNode:
    x: int
    left: Optional['TreeNode'] = None
    right: Optional['TreeNode'] = None


def iterative(tn: Optional[TreeNode]):
    stack: list[TreeNode] = []
    current = tn

    while stack or current:
        if current:
            stack.append(current)
            current = current.left
        else:
            current = stack.pop()
            print(current.x)
            current = current.right


def recursive(tn: Optional[TreeNode]):
    if not tn:
        return None

    recursive(tn.left)
    print(tn.x)
    recursive(tn.right)


def build_tree_from_inorder(values: list[int]) -> TreeNode:
    ...
