from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        values = []
        def inorder(n: TreeNode):
            if n.left:
                inorder(n.left)
            values.append(n.val)
            if n.right:
                inorder(n.right)
        inorder(root)
        print(values)

        return min([values[i] - values[i - 1] for i in range(1, len(values))])

    # stack solution
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        stack = []
        prev = None
        mindif = float('inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            mindif = min(root.val - prev.val, mindif) if prev else mindif
            prev = root
            root = root.right
        return mindif