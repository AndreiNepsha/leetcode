# TODO improve solution
# https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/solutions/3643477/dp-recursion-using-python-layman-s-code/
# https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/solutions/3643494/python-easy-fast-solution/

from math import comb


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left: "TreeNode" = left
        self.right: "TreeNode" = right
    
    def insert(self, val):
        if val > self.val:
            if self.right:
                self.right.insert(val)
            else:
                self.right = TreeNode(val)
        else:
            if self.left:
                self.left.insert(val)
            else:
                self.left = TreeNode(val)


MOD = 10 ** 9 + 7

ARR_MEM = {}

def calculate_arrangement(n, m):
    tup = (n, m)
    if tup in ARR_MEM:
        return ARR_MEM[tup]

    if n > m and m > 1:
        r = calculate_arrangement(n - 1, m - 1) + calculate_arrangement(n - 1, m)
        ARR_MEM[tup] = r
        return r
    return 1
        

class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        # build tree
        bst = TreeNode(nums[0])
        for i in range(1, len(nums)):
            bst.insert(nums[i])
        
        def count_permutations(n: TreeNode):
            nodes, nodes_to_left, nodes_to_right =  1, 0, 0
            left_perms, right_perms = 1, 1
            if n.left:
                nodes_to_left, left_perms = count_permutations(n.left)
            if n.right:
                nodes_to_right, right_perms = count_permutations(n.right)
            
            if nodes_to_left and nodes_to_right:
                perms = 0
                n = nodes_to_left + 1
                for k in range(1, min(nodes_to_right + 1, n + 1)):
                    perms += comb(n, k) % MOD * calculate_arrangement(nodes_to_right, k) % MOD
                if not perms:
                    perms = 1
            else:
                perms = 1
            perms = perms * left_perms % MOD
            perms = perms * right_perms % MOD
            nodes += nodes_to_left + nodes_to_right
            return nodes, perms

        return count_permutations(bst)[1] - 1


a = Solution().numOfWays([10,23,12,18,4,29,2,8,41,31,25,21,14,35,26,5,19,43,22,37,9,20,44,28,1,39,30,38,36,6,13,16,27,17,34,7,15,3,11,24,42,33,40,32])
assert 182440977 == a, a

a = Solution().numOfWays([9,4,2,1,3,6,5,7,8,14,11,10,12,13,16,15,17,18])
assert 216212978 == a, a

a = Solution().numOfWays([3,4,5,1,2])
assert 5 == a, a

a = Solution().numOfWays([1,2,3])
assert 0 == a, a

a = Solution().numOfWays([2,1,3])
assert 1 == a, a

a = Solution().numOfWays([4,1,3,5,2])  # [4,1,3,2,5], [4,3,1,5,2], [4,3,1,2,5]
assert 3 == a, a

a = Solution().numOfWays([4,5,3,2,1])  # [4,3,5,2,1], [4,3,2,5,1], [4,3,2,1,5]
assert 3 == a, a

a = Solution().numOfWays([4,5,2,3,1])  # [4,5,2,1,3], [4,2,5,3,1], [4,2,5,1,3] ...
assert 7 == a, a
