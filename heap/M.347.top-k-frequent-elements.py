from collections import defaultdict
from heapq import heappush, heapreplace


class Solution:
    # Heap solution O(n * log(k)) | O(n + k)
    def _topKFrequent(self, nums: list[int], k: int) -> list[int]:
        num_f = defaultdict(int)
        for n in nums:
            num_f[n] += 1
        

        num_f = list(num_f.items())
        heap = []
        for n in num_f[:k]:
            heappush(heap, (n[1], n[0]))
        for n in num_f[k:]:
            if heap[0][0] < n[1]:
                heapreplace(heap, (n[1], n[0]))

        return [i[1] for i in heap]

    # Bucket sort solution O(n)
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        num_f = defaultdict(int)
        for n in nums:
            num_f[n] += 1

        buckets = [None] + [None] * len(nums)
        for n, f in num_f.items():
            if buckets[f]:
                buckets[f].append(n)
            else:
                buckets[f] = [n]

        res = []
        i = len(nums)
        while len(res) < k:
            if buckets[i]:
                res += buckets[i]
            i -= 1

        return res[:k]


a = Solution().topKFrequent(nums = [3,0,1,0], k = 1)
assert [0] == a, a

a = Solution().topKFrequent(nums = [1,1,1,2,2,3], k = 2)
assert [1,2] == a, a
