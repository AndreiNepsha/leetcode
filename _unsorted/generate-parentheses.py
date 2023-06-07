from collections import deque


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        q = deque()
        q.append((n - 1, 1, ["("]))
        r = []
        while len(q) > 0:
            pool, opened, a = q.pop()
            if pool == 0:
                r.append("".join(a + [")"] * opened))
            else:
                q.append((pool - 1, opened + 1, a + ["("]))
                if opened > 0:
                    q.append((pool, opened - 1, a + [")"]))
        return r


# print(str(["a", "b"]))

a = Solution().generateParenthesis(3)
assert ["((()))", "(()())", "(())()", "()(())", "()()()"] == a, a

# exp = ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]
# act = ["()()()()","(()()())","()(()())","((()()))","(()())()","()()(())","(()(()))","()(())()","()((()))","(((())))","((()))()","((())())","(())()()"]
# for e in exp:
#     if e not in act:
#         print(e)