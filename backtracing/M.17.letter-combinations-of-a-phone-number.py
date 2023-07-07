from collections import deque


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        n = len(digits)
        letters = [
            "",
            "",
            "abc",
            "def",
            "ghi",
            "jkl",
            "mno",
            "pqrs",
            "tuv",
            "wxyz",
        ]

        combs = []
        cur = deque()

        def trace(i):
            if i == n:
                combs.append("".join(cur))
            else:
                for l in letters[int(digits[i])]:
                    cur.append(l)
                    trace(i + 1)
                    cur.pop()

        trace(0)

        return combs
