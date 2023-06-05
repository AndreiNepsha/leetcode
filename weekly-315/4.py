class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        n = len(nums)
        res, i = 0, 0

        while i < n:
            while i < n and (nums[i] < minK or nums[i] > maxK):
                i += 1
            if i == n:
                break

            l = i
            while i < n and (nums[i] >= minK and nums[i] <= maxK):
                i += 1

            last_min, last_max = l - 1, l - 1
            invalid = 0
            cnt = i - l
            while l < i:
                if nums[l] == minK:
                    last_min = l
                if nums[l] == maxK:
                    last_max = l

                invalid += l - min(last_max, last_min)
                l += 1

            res += (cnt * (cnt + 1)) // 2 - invalid

        return res


nums = [
    35054,
    398719,
    945315,
    945315,
    820417,
    945315,
    35054,
    945315,
    171832,
    945315,
    35054,
    109750,
    790964,
    441974,
    552913,
]
print(sum([13, 9, 9, 9, 8, 5, 5]))
minK = 35054
maxK = 945315
a = Solution().countSubarrays(nums, minK, maxK)
assert 81 == a, a

nums = [1, 3, 5, 2, 7, 5]
minK = 1
maxK = 5
a = Solution().countSubarrays(nums, minK, maxK)
assert 2 == a, a

nums = [1, 1, 1, 1]
minK = 1
maxK = 1
a = Solution().countSubarrays(nums, minK, maxK)
assert 10 == a, a
