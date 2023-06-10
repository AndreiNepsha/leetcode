class Solution:
    def maxValue(self, n: int, index: int, max_sum: int) -> int:
        if max_sum == n:
            return 1
        li = n - 1
        c_sum = n
        peak = 1
        dif = 1
        l, r = index, index
        while c_sum + dif <= max_sum:
            if l == 0 and r == li:
                return peak + (max_sum - c_sum) // dif
            else:
                c_sum += dif
                peak += 1
                if l > 0:
                    l -= 1
                    dif += 1
                if r < li:
                    r += 1
                    dif += 1
        return peak
            


n, index, max_sum = 4, 2, 6
a = Solution().maxValue(n, index, max_sum)
assert 2 == a, a

n, index, max_sum = 6, 1, 10
a = Solution().maxValue(n, index, max_sum)
assert 3 == a, a

n, index, max_sum = 4, 0, 4
a = Solution().maxValue(n, index, max_sum)
assert 1 == a, a

n, index, max_sum = 3, 2, 18
a = Solution().maxValue(n, index, max_sum)
assert 7 == a, a

n, index, max_sum = 3, 0, 815094800
a = Solution().maxValue(n, index, max_sum)
assert 271698267 == a, a
