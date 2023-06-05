class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        poli_max = [s[0]]
        for i in range(n - 1):
            poli = [s[i]]
            for k in range(1, min(i + 1, n - i)):
                if s[i - k] != s[i + k]:
                    break
                poli.insert(0, s[i - k])
                poli.append(s[i - k])
            if len(poli_max) < len(poli):
                poli_max = poli
            if s[i] == s[i + 1]:
                poli = [s[i], s[i + 1]]
                for k in range(1, min(i + 1, n - i - 1)):
                    if s[i - k] != s[i + k + 1]:
                        break
                    poli.insert(0, s[i - k])
                    poli.append(s[i - k])
                if len(poli_max) < len(poli):
                    poli_max = poli
        return "".join(poli_max)


s = "abb"
a = Solution().longestPalindrome(s)
assert "bb" == a, a


s = "ccc"
a = Solution().longestPalindrome(s)
assert "ccc" == a, a


s = "tattarrattat"
a = Solution().longestPalindrome(s)
assert "tattarrattat" == a, a
