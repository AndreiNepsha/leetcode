# TODO improve solution

from collections import Counter


class Solution:
    def makeArrayIncreasing(self, arr1: list[int], arr2: list[int]) -> int:
        arr2 = sorted([i for i in Counter(arr2).keys()])
        li = len(arr1) - 1

        def find(gt):
            l, r = 0, len(arr2) - 1
            while l < r:
                mid = l + (r - l) // 2
                if arr2[mid] <= gt:
                    l = mid + 1
                else:
                    r = mid
            if gt < arr2[l]:
                return arr2[l]
            return -1
        
        dp = {}
        
        def dfs(prev, i):
            if (prev, i) in dp:
                return dp[(prev, i)]

            if i > li:
                return 0
            
            replaces = []

            if prev < arr1[i] and (r := dfs(arr1[i], i + 1)) >= 0:
                replaces.append(r)
            if (to_replace := find(prev)) >= 0 and (r := dfs(to_replace, i + 1)) >= 0:
                replaces.append(r + 1)
            
            cost = -1
            if replaces:
                cost = min(replaces)
            
            dp[(prev, i)] = cost

            return cost
        
        return dfs(-1, 0)


a = Solution().makeArrayIncreasing(
    arr1 = [9,18,3,8,21,6,7,2,7,28,23,16,33,2,25,14,15], 
    arr2 = [13,2,15,30,31,30,9,10,7,30,31,4,33,10,25,28,19,6,15,6,19,30,25,14,7,28,23,20,1,2,25,16]
)
assert 14 == a, a

a = Solution().makeArrayIncreasing(arr1 = [5,16,19,2,1,12,7,14,5,16], arr2 = [1,3,3,4,4,6,6,7,13,14,16,16,17,17,18])
assert 8 == a, a

a = Solution().makeArrayIncreasing(arr1 = [0,11,6,1,4,3], arr2 = [5,4,11,10,1,0])
assert 5 == a, a

a = Solution().makeArrayIncreasing(arr1 = [1,5,3,6,7], arr2 = [4,3,1])
assert 2 == a, a

a = Solution().makeArrayIncreasing(arr1 = [1,5,3,6,7], arr2 = [1,3,2,4])
assert 1 == a, a

a = Solution().makeArrayIncreasing(arr1 = [1,5,3,6,7], arr2 = [1,6,3,3])
assert -1 == a, a
