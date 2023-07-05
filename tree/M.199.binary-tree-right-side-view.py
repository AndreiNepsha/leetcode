# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []
        next_level = [root]
        view = []
        while next_level:
            l = next_level
            view.append(l[-1].val)
            next_level = []
            for n in l:
                if n.left:
                    next_level.append(n.left)
                if n.right:
                    next_level.append(n.right)
        return view
