from heapq import heappop, heappush


class Solution:
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
        heap = []
        l, r = 0, len(costs) - 1
        for _ in range(candidates):
            if l <= r:
                heappush(heap, (costs[r], True))
                r -= 1
            if l <= r:
                heappush(heap, (costs[l], False))
                l += 1

        
        total = 0
        for _ in range(k):
            cost, is_right = heappop(heap)
            total += cost
            if l <= r:
                if not is_right:
                    heappush(heap, (costs[l], False))
                    l += 1
                else:
                    heappush(heap, (costs[r], True))
                    r -= 1
        
        return total



a = Solution().totalCost(costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4)
assert 11 == a, a

a = Solution().totalCost(costs = [1,2,4,1], k = 3, candidates = 3)
assert 4 == a, a

a = Solution().totalCost(costs = [31,25,72,79,74,65,84,91,18,59,27,9,81,33,17,58], k = 11, candidates = 2)
assert 423 == a, a

a = Solution().totalCost(costs = [10,1,11,10], k = 2, candidates = 1)
assert 11 == a, a