# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum = root.val
        min_level = 1
        cur_level = 2
        next_level = [n for n in [root.left, root.right] if n]
        while next_level:
            s = 0
            l = next_level
            next_level = []
            for n in l:
                s += n.val
                if n.left:
                    next_level.append(n.left)
                if n.right:
                    next_level.append(n.right)
            if s > max_sum:
                max_sum = s
                min_level = cur_level
            cur_level += 1
        return min_level