# Definition for a binary tree node.
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def btree_from_list(l: list):
    ll = len(l)
    if ll < 1:
        return None

    head = TreeNode(l[0])
    d = deque([head])
    i = 1
    while i < ll:
        n = d.popleft()
        n.left = TreeNode(l[i]) if l[i] else None
        n.right = TreeNode(l[i + 1]) if i + 1 < ll and l[i + 1] else None
        d.append(n.left)
        d.append(n.right)
        i += 2
    return head


def btree_to_list(head: Optional[TreeNode]):
    if not head:
        return []

    a = []
    d = deque([head])
    while len(d) > 0:
        n = d.popleft()
        a.append(n.val)
        if n.left:
            d.append(n.left)
        if n.right:
            d.append(n.right)
    return a


class Solution:
    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
        res = TreeNode()
        d = deque([(res, root1, root2)])
        while len(d) > 0:
            r, n1, n2 = d.popleft()
            r.val = (n1.val if n1 else 0) + (n2.val if n2 else 0)
            n1_left = n1.left if n1 else None
            n1_right = n1.right if n1 else None
            n2_left = n2.left if n2 else None
            n2_right = n2.right if n2 else None
            if n1_left or n2_left:
                r.left = TreeNode()
                d.append((r.left, n1_left, n2_left))
            if n1_right or n2_right:
                r.right = TreeNode()
                d.append((r.right, n1_right, n2_right))
        return res


print(btree_to_list(btree_from_list([[1, 2, 3, None, None, 4, 5]])))
# root1 = btree_from_list([1, 3, 2, 5])
# root2 = btree_from_list([2, 1, 3, None, 4, None, 7])
# res = btree_to_list(Solution().mergeTrees(root1, root2))
# assert btree_from_list([3, 4, 5, 5, 4, None, 7]) == res, res
