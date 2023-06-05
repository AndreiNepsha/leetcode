from collections import deque

OPEN = ['(', "{", "["]
CLOSE = [')', "}", "]"]
OPPOSITE = dict(zip(OPEN, CLOSE))


class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for c in s:
            if c in OPEN:
                stack.append(c)
            else:
                if len(stack) == 0 or c != OPPOSITE[stack.pop()]:
                    return False 
        return len(stack) == 0


s = "()"
assert Solution().isValid(s)

s = "()[]{}"
assert Solution().isValid(s)
