# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if not root:
            return []
        levels = []
        next_level = [root]
        while next_level:
            l = next_level
            levels.append([n.val for n in l])
            next_level = []
            for n in l:
                if n.left:
                    next_level.append(n.left)
                if n.right:
                    next_level.append(n.right)
        return levels
