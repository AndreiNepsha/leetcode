class Solution:
    def reverseWords(self, s: str) -> str:
        words = [w for w in s.split(" ") if len(w.strip())]
        words.reverse()
        return " ".join(words)


s = "  hello world  "
a = Solution().reverseWords(s)
assert "world hello" == a
