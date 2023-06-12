# 1110000
# 1100001
# 1011000
# 1000011
# 0111000

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        if n == 0:
            return []
        sets = [[], nums]
        k = 1
        while k < n:
            mask = [True] * k + [False] * (n - k)
            l = 0
            while True:
                sets.append([n for i, n in enumerate(nums) if mask[i]])
                if l + k == n:
                    break
                ones = 0
                i = n - 1
                while mask[i]:
                    mask[i] = False
                    ones += 1
                    i -= 1
                while not mask[i]:
                    i -= 1
                if i == l:
                    l += 1
                i += 1
                mask[i - 1] = False
                mask[i] = True
                for j in range(ones):
                    mask[i + 1 + j] = True
            k += 1

        return sets


a = Solution().subsets([1,2,3,4,5])
assert a == [[], [1, 2, 3, 4, 5], [1], [2], [3], [4], [5], [1, 2], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 5], [1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 3, 4], [1, 3, 5], [1, 4, 5], [2, 3, 4], [2, 3, 5], [2, 4, 5], [3, 4, 5], [1, 2, 3, 4], [1, 2, 3, 5], [1, 2, 4, 5], [1, 3, 4, 5], [2, 3, 4, 5]], a
