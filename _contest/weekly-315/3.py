class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        if num == 0:
            return True
        sn = str(num)
        start = 10 ** (len(sn) - 1)
        if len(sn) > 1 and sn[0] < "2":
            start //= 10
        for i in range(start, num):
            if num == i + int(str(i)[::-1]):
                return True
        return False


num = 10
a = Solution().sumOfNumberAndReverse(num)
assert a, a

num = 443
a = Solution().sumOfNumberAndReverse(num)
assert a, a

num = 63
a = Solution().sumOfNumberAndReverse(num)
assert not a, a

num = 181
a = Solution().sumOfNumberAndReverse(num)
assert a, a
