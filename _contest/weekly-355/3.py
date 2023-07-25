from collections import defaultdict
from heapq import heapify, heappop, heappush, heapreplace


class Solution:
    # TODO TLE
    def maxIncreasingGroups(self, usageLimits: list[int]) -> int:
        mp = defaultdict(int)
        for l in usageLimits:
            mp[l] += 1

        limits_heap = [(-l, k) for l, k in mp.items()]
        heapify(limits_heap)

        k = 0
        while limits_heap:
            k += 1
            sq = []
            i = 0
            while i < k:
                if not limits_heap:
                    return k - 1
                l, c = heappop(limits_heap)
                dif = min(c, k - i)
                i += dif
                if c > dif:
                    sq.append((l, c - dif))
                sq.append((l + 1, dif))
            for l, c in sq:
                if l <= -1:
                    if limits_heap and l == limits_heap[0][0]:
                        heapreplace(limits_heap, (l, c + limits_heap[0][1]))
                    else:
                        heappush(limits_heap, (l, c))
        return k


a = Solution().maxIncreasingGroups(usageLimits = [5,1,1,5,1])
assert 4 == a, a

a = Solution().maxIncreasingGroups(usageLimits = [2,7,6,2,2])
assert 5 == a, a

a = Solution().maxIncreasingGroups(usageLimits = [2,2,2])
assert 3 == a, a

a = Solution().maxIncreasingGroups(usageLimits = [100000 for i in range(100000)])
assert 9999 == a, a

a = Solution().maxIncreasingGroups(usageLimits = [1,2,5])
assert 3 == a, a

a = Solution().maxIncreasingGroups(usageLimits = [1])
assert 1 == a, a


