from collections import deque


class Solution:
    def simplifyPath(self, path: str) -> str:
        splitted = path.split("/")
        stack = deque()
        for i in range(1, len(splitted)):
            d = splitted[i]
            if d == "" or d == ".":
                continue
            elif d == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(d)
        
        return "/" + "/".join(stack)
