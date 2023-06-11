class Solution:
    def isFascinating(self, n: int) -> bool:
        c = str(n) + str(n * 2) + str(n * 3)
        if len(c) != 9:
            return False
        if "0" in c:
            return False
        return len(set(c)) == 9
        
assert not Solution().isFascinating(783)
assert Solution().isFascinating(192)
assert not Solution().isFascinating(100)
assert not Solution().isFascinating(267)
