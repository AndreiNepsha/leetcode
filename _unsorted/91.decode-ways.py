from collections import deque
from math import prod


class Solution:
    def _fib(self, n):
        f1 = 1
        f2 = 1
        for _ in range(2, n):
            f2 = f2 + f1
            f1 = f2 - f1
        return f2

    def numDecodings(self, s: str) -> int:
        n = len(s)
        if s.startswith("0") or s.find("00") > -1:
            return 0
        # d = deque([0], maxlen=n)
        # ways = 0
        # while len(d) > 0:
        #     i = d.pop()
        #     if i == n:
        #         ways += 1
        #     elif i > n or s[i] == "0":
        #         continue
        #     elif i + 1 < n and s[i] < "3":
        #         if s[i + 1] == "0":
        #             d.append(i + 2)
        #         elif s[i] == "2" and s[i + 1] > "6":
        #             d.append(i + 1)
        #         else:
        #             d.append(i + 2)
        #             d.append(i + 1)
        #     else:
        #         d.append(i + 1)
        i = 0
        k = 2
        fibs = []
        for i in range(n - 1):
            two = "".join(s[i : i + 2])
            if s[i] > "2" and s[i + 1] == "0":
                return 0
            if two < "27" and two > "10" and two != "20":
                k += 1
            elif s[i] == "0" or two == "10" or two == "20":
                fibs.append(self._fib(k - 1))
                k = 2
            else:
                fibs.append(self._fib(k))
                k = 2
        fibs.append(self._fib(k))
        return prod(fibs)


nums = "2101"
a = Solution().numDecodings(nums)
assert 1 == a, a

nums = "123123"
a = Solution().numDecodings(nums)
assert 9 == a, a

nums = "11"
a = Solution().numDecodings(nums)
assert 2 == a, a

nums = "111"
a = Solution().numDecodings(nums)
assert 3 == a, a

nums = "1111"
a = Solution().numDecodings(nums)
assert 5 == a, a

nums = "01"
a = Solution().numDecodings(nums)
assert 0 == a, a

nums = "12"
a = Solution().numDecodings(nums)
assert 2 == a, a

nums = "2261"
a = Solution().numDecodings(nums)
assert 3 == a, a
