class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        bit_mask = 1
        flips = 0
        for _ in range(32):
            a_bit = a & bit_mask
            b_bit = b & bit_mask
            c_bit = c & bit_mask
            if not c_bit:
                if a_bit and b_bit:
                    flips += 2
                elif a_bit or b_bit:
                    flips += 1
            else:
                if not a_bit and not b_bit:
                    flips += 1
            bit_mask <<= 1
        return flips


# a = 1000
# b = 0011
# c = 0101
r = Solution().minFlips(8, 3, 5)
assert r == 3, r


# a = 0000 1011 0000
# b = 0010 0001 1111
# c = 0000 0001 0100
r = Solution().minFlips(176, 543, 20)
assert r == 6, r
