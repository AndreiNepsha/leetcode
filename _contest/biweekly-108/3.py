class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        words = [bin(5 ** n)[2:] for n in range(6, -1, -1)]
        n = len(s)
        
        min_parts = 16
        def backtrace(l, parts):
            nonlocal min_parts
            if l == n:
                min_parts = min(min_parts, parts)
            for w in words:
                if l + len(w) <= n and s[l:].startswith(w):
                    backtrace(l + len(w), parts + 1)
        backtrace(0, 0)

        return min_parts if min_parts < 16 else -1


a = Solution().minimumBeautifulSubstrings(s = "1011")
assert 2 == a, a

a = Solution().minimumBeautifulSubstrings(s = "111")
assert 3 == a, a

a = Solution().minimumBeautifulSubstrings(s = "0")
assert -1 == a, a
