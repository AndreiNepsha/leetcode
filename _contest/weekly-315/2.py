from collections import Counter


class Solution:
    def countDistinctIntegers(self, nums: list[int]) -> int:
        ln = len(nums)
        counter = Counter()
        for i in range(ln):
            counter[nums[i]] = True
            counter[int(str(nums[i])[::-1])] = True
        return len(counter)


nums = [1, 13, 10, 12, 31]
a = Solution().countDistinctIntegers(nums)
assert 6 == a, a

nums = [2, 2, 2]
a = Solution().countDistinctIntegers(nums)
assert 1 == a, a
