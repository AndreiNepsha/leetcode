MOD = 10 ** 9 + 7

class Solution:
    def specialPerm(self, nums: list[int]) -> int:
        ln = len(nums)
        dp = {}
        num_to_ind = {n: i for i, n in enumerate(nums)}
        mask = ["0"] * ln
        used = set()

        def dfs(prev: int):
            key = f'{prev}_{"".join(mask)}'
            if key in dp:
                return dp[key]

            if len(used) == ln:
                return 1

            perms = 0
            for n in nums:
                if n not in used and (prev == -1 or prev % n == 0 or n % prev == 0):
                    used.add(n)
                    mask[num_to_ind[n]] = "1"
                    perms = (perms + dfs(n)) % MOD
                    mask[num_to_ind[n]] = "0"
                    used.remove(n)
            dp[key] = perms
            return perms

        return dfs(-1)


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