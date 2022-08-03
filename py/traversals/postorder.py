"""
                1
        2               3
    4       5       6       7

    inorder: 4 5 2 6 7 3 1
"""


from typing import Optional
from dataclasses import dataclass


@dataclass
class TreeNode:
    x: int
    left: Optional['TreeNode'] = None
    right: Optional['TreeNode'] = None


def recursive(tn: Optional[TreeNode]):
    if not tn:
        return None

    recursive(tn.left)
    recursive(tn.right)
    print(tn.x)
