class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        ints = sorted(intervals, key = lambda i: i[0])
        ln = len(ints)
        r = []
        cur = ints[0]
        for i in range(1, ln):
            if ints[i][0] <= cur[1]:
                cur[1] = max(ints[i][1], cur[1])
            else:
                r.append(cur)
                cur = ints[i]
        r.append(cur)
        return r


a = Solution().merge([[1,3],[2,6],[8,15],[9,11]])
assert [[1,6],[8,15]] == a, a

a = Solution().merge([[1,3],[2,6],[8,10],[9,11]])
assert [[1,6],[8,11]] == a, a

a = Solution().merge([[1,3],[2,6],[8,10],[15,18]])
assert [[1,6],[8,10],[15,18]] == a, a

a = Solution().merge([[1,4],[4,5]])
assert [[1,5]] == a, a
