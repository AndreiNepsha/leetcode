from collections import deque


class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []

        def is_palindrome(s: str) -> bool:
            i, j = 0, len(s) - 1
            while i < j:
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                else:
                    return False
            return True

        parts = deque()
        def backtrace(s: str):
            if not s:
                res.append(list(parts))
                return
            
            for i in range(1, len(s) + 1):
                part = s[:i]
                if is_palindrome(part):
                    parts.append(part)
                    backtrace(s[i:])
                    parts.pop()
        
        backtrace(s)
        
        return res

a = Solution().partition(s = "aab")
assert [["a","a","b"],["aa","b"]] == a, a
