from heapq import heappop, heappush


class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        n, m = len(nums1), len(nums2)
        mem = set()
        heap = [(0, 0, 0)]
        s = []
        for _ in range(k):
            if not len(heap):
                return s
            _, i, j = heappop(heap)
            s.append([nums1[i], nums2[j]])
            ni, nj = i + 1, j + 1
            if ni < n and (ni, j) not in mem:
                mem.add((ni, j))
                heappush(heap, (nums1[ni] + nums2[j], ni, j))
            if nj < m and (i, nj) not in mem:
                mem.add((i, nj))
                heappush(heap, (nums1[i] + nums2[nj], i, nj))
        return s


a = Solution().kSmallestPairs(nums1 = [1,7,11], nums2 = [2,4,6], k = 3)
assert [[1,2],[1,4],[1,6]] == a, a
