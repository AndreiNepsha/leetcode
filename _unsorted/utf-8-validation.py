class Solution:
    def validUtf8(self, data: list[int]) -> bool:
        ld = len(data)
        i = 0
        n = 0
        while i < ld:
            if n:
                if data[i] & 0b1100_0000 != 0b1000_0000:
                    return False
                n -= 1
            else:
                if data[i] & 0b1000_0000 == 0b0:
                    pass
                elif data[i] & 0b1110_0000 == 0b1100_0000:
                    n = 1
                elif data[i] & 0b1111_0000 == 0b1110_0000:
                    n = 2
                elif data[i] & 0b1111_1000 == 0b1111_0000:
                    n = 3
                else:
                    return False
            i += 1
        return n == 0


data = [197, 130, 1]
assert Solution().validUtf8(data)
