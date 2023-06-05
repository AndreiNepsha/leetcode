class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n < 3:
            return 1
        f0 = 0
        f1 = 1
        f2 = 1
        while n > 2:
            tmp = f1
            f2 = f2 + f1 + f0
            f1 = f2 - f1 - f0
            f0 = tmp
            n -= 1
        return f2


a = Solution().tribonacci(25)
assert 1389537 == a, a