from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(left: Optional[TreeNode], right: Optional[TreeNode]):
            if left and right:
                return left.val == right.val and check(left.right, right.left) and check(left.left, right.right)
            elif not left and not right:
                return True
            return False
        return check(root.left, root.right)
