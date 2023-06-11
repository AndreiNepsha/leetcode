class Solution:
    def minCost(self, nums: list[int], x: int) -> int:
        ln = len(nums)
        min_costs = nums
        min_total = sum(nums)

        for shift in range(1, ln):
            min_costs = [
                min(nums[(i + shift  if i + shift < ln else i + shift - ln)], min_costs[i])
                for i in range(ln)
            ]

            min_total = min(min_total, sum(min_costs) + shift * x)

        return min_total



nums = [15,150,56,69,214,203]
x = 42
a = Solution().minCost(nums, x)
assert 298 == a, a

# 27 + 18 + 18 + 31 + 25
nums = [31,25,18,59]
x = 27
a = Solution().minCost(nums, x)
assert 119 == a, a

nums = [20,1,15]
x = 5
a = Solution().minCost(nums, x)
assert 13 == a, a

nums = [100,100,1,100]
x = 15
a = Solution().minCost(nums, x)
assert 49 == a, a
