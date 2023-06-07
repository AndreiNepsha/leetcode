class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
        c = [(c, i) for i, c in enumerate(s)]
        c.sort(key=lambda t: t[0])
        k = [None] * n
        for i, t in enumerate(c):
            k[t[1]] = i
        
        for i in range(1, n):
            if k[i] 

        return "".join(a)


s = "vzhofnpo"
answer = Solution().robotWithString(s)
assert "fnohopzv" == answer, answer

s = "bac"
answer = Solution().robotWithString(s)
assert "abc" == answer, answer

s = "zzabba"
answer = Solution().robotWithString(s)
assert "aabbzz" == answer, answer

s = "bbazza"
answer = Solution().robotWithString(s)
assert "aazzbb" == answer, answer

s = "ccabzza"
answer = Solution().robotWithString(s)
assert "aazzbcc" == answer, answer

s = "bydcizfve"
answer = Solution().robotWithString(s)
assert "bcdevfziy" == answer, answer
