class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ls = len(s)
        cs = {}
        m = 0
        i = k = 0
        while i < ls:
            if s[i] in cs:
                if (nm := len(cs)) > m:
                    m = nm
                while s[k] != s[i]:
                    del cs[s[k]]
                    k += 1
            cs[s[i]] = True
            i += 1
        if len(cs) > m:
            m = len(cs)
        return m


s = "abcabcbb"
a = Solution().lengthOfLongestSubstring(s)
assert 3 == a, a
