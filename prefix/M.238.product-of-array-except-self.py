class Solution:
    def _productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        left_prefix = [nums[0]] * n
        right_prefix = [nums[n - 1]] * n
        for i in range(1, n):
            left_prefix[i] = left_prefix[i - 1] * nums[i]
        for i in range(n - 2, -1, -1):
            right_prefix[i] = right_prefix[i + 1] * nums[i]
        
        result = [0] * n
        for i in range(n):
            lp = 1 if i == 0 else left_prefix[i - 1]
            rp = 1 if i == n - 1 else right_prefix[i + 1]
            result[i] = lp * rp
        
        return result
    
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        l, r, n = 1, 1, len(nums) - 1
        output = [1] * len(nums)

        for i, j in zip(range(n), range(n, 0, -1)):
            l *= nums[i]
            r *= nums[j]
            output[i + 1] *= l
            output[j - 1] *= r
        
        return output


a = Solution().productExceptSelf(nums = [1,2,3,4])
assert [24,12,8,6] == a, a
