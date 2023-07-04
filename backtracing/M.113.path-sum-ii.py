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
        s = root.val
        path = deque([root.val])
        def dfs(n: TreeNode):
            nonlocal path, paths, s
            if not n.left and not n.right:
                if s == targetSum:
                    paths.append([n for n in path])
                return
            if n.left:
                path.append(n.left.val)
                s = s + n.left.val
                dfs(n.left)
                s = s - n.left.val
                path.pop()
            if n.right:
                path.append(n.right.val)
                s = s + n.right.val
                dfs(n.right)
                s = s - n.right.val
                path.pop()
        dfs(root)
        return paths
