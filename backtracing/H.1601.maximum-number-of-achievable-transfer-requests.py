class Solution:
    def maximumRequests(self, n: int, requests: list[list[int]]) -> int:
        changes = [0] * n

        max_r = 0
        def backtrack(i, a):
            nonlocal max_r
            if i == len(requests):
                for c in changes:
                    if c != 0:
                        return
                max_r = max(max_r, a)
            else:
                # skip and check next
                backtrack(i + 1, a)

                # accept request
                fr, to = requests[i]

                changes[fr] = changes[fr] - 1
                changes[to] = changes[to] + 1

                backtrack(i + 1, a + 1)

                changes[to] = changes[to] - 1
                changes[fr] = changes[fr] + 1

        backtrack(0, 0)
        return max_r


a = Solution().maximumRequests(n = 2, requests = [[1,0],[0,0],[1,0],[0,1],[0,1],[1,1],[0,1],[0,0],[0,0],[0,1],[1,0],[0,0],[0,1],[1,1],[1,1]])
assert 13 == a, a

a = Solution().maximumRequests(n = 5, requests = [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]])
assert 5 == a, a

a = Solution().maximumRequests(n = 1, requests = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]])
assert 16 == a, a
