MOD = 10 ** 9 + 7

class Solution:
    def specialPerm(self, nums: list[int]) -> int:
        dp = {}
        num_to_mask = {n: 1 << i for i, n in enumerate(nums)}
        all_used = sum(v for v in num_to_mask.values())

        def dfs(prev: int, used_mask):
            key = prev << 16 | used_mask
            if key in dp:
                return dp[key]

            if used_mask == all_used:
                return 1

            perms = 0
            for n in nums:
                m = num_to_mask[n]
                if m & used_mask == 0 and (prev % n == 0 or n % prev == 0):
                    perms = (perms + dfs(n, used_mask | num_to_mask[n])) % MOD
            dp[key] = perms
            return perms

        return dfs(1, 0)


a = Solution().specialPerm(nums = [19,38,76,152,304,608,1216,2432,4864,9728,19456,38912,77824,155648])
assert 178290591 == a, a

a = Solution().specialPerm(nums = [1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192])
assert 178290591 == a, a

a = Solution().specialPerm(nums = [2,3,6])
assert 2 == a, a

a = Solution().specialPerm(nums = [31,93])
assert 2 == a, a

a = Solution().specialPerm(nums = [2,3,6,9])
assert 2 == a, a