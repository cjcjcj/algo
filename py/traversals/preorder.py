"""
                1
        2               3
    4       5       6       7

    preorder: 1 2 4 5 3 6 7
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
    if tn:
        stack.append(tn)

    while stack:
        current = stack.pop()
        print(current.x)

        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)


def recursive(tn: Optional[TreeNode]):
    if not tn:
        return None

    print(tn.x)
    recursive(tn.left)
    recursive(tn.right)


def build_tree_from_preorder(values: list[int]):
    ...
