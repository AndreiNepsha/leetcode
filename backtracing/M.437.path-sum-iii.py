from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> list[list[int]]:
        if not root:
            return []
        paths = []
        def dfs(n: TreeNode, path: list[int], s: int):
            if s + n.val == targetSum:
                paths.append(path + [n.val])
            if n.left:
                dfs(n.left, path + [n.val], s + n.val)
                dfs(n.left, path, s)
            if n.right:
                dfs(n.right, path + [n.val], s + n.val)
                dfs(n.right, path, s)
        dfs(root, [], 0)
        dfs(root, [root.val], root.val)
        return paths
