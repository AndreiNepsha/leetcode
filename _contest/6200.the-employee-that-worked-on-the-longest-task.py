class Solution:
    def hardestWorker(self, n: int, logs: list[list[int]]) -> int:
        n = len(logs)
        if n == 1:
            return logs[0][0]

        longest = logs[0][1]
        li = 0
        i = 1
        while i < n:
            if (l := logs[i][1] - logs[i - 1][1]) >= longest:
                if l == longest and logs[i][0] > logs[li][0]:
                    pass
                else:
                    li = i
                    longest = l
            i += 1
        return logs[li][0]


n = 26
logs = [[36, 3], [1, 5], [12, 8], [25, 9], [53, 11], [29, 12], [52, 14]]
answer = Solution().hardestWorker(n, logs)
assert 12 == answer, answer
