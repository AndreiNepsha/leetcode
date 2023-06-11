class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        ln = 1
        left = 0
        while left + ln < len(s):
            dups = 0
            for i in range(1, ln + 1):
                if s[left + i] == s[left + i - 1]:
                    dups += 1
            if dups < 2:
                ln += 1
            else:
                left += 1
        return ln

a = Solution().longestSemiRepetitiveSubstring("52233")
assert 4 == a, a

a = Solution().longestSemiRepetitiveSubstring("5494")
assert 4 == a, a

a = Solution().longestSemiRepetitiveSubstring("1111111")
assert 2 == a, a
