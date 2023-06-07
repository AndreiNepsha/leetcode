from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ls = len(s1)
        ls2 = len(s2)
        c1 = Counter(s1)
        c2 = Counter(s2[0:ls])
        if c2 == c1:
            return True
        k = 0
        i = ls
        while i < ls2:
            c2[s2[i]] += 1
            if c2[s2[k]] == 1:
                del c2[s2[k]]
            else:
                c2[s2[k]] -= 1
            i += 1
            k += 1
            if c2 == c1:
                return True
        return False


s1 = "ab"
s2 = "eidbaooo"
a = Solution().checkInclusion(s1, s2)
assert a
