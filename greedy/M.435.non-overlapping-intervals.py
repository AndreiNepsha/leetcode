from collections import deque
import math


class Solution:
    def _eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        n = len(intervals)
        intervals = sorted(intervals)
        non_overlapping = deque([intervals[0]])
        for i in range(1, n):
            if non_overlapping[-1][1] > intervals[i][0]:
                new_end = min(non_overlapping[-1][1], intervals[i][1])
                while non_overlapping and (non_overlapping[-1][1] > intervals[i][0]):
                    non_overlapping.pop()   
                non_overlapping.append((intervals[i][0], new_end))
            else:
                non_overlapping.append((intervals[i][0], intervals[i][1]))
        return n - len(non_overlapping)

    # much better solution
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        last_end, count = -math.inf, 0

        for start, end in sorted(intervals, key=lambda interval: interval[1]):
            if start >= last_end:
                last_end = end
            else:
                count += 1
        
        return count


a = Solution().eraseOverlapIntervals(intervals = [[1,2],[2,3],[3,4],[1,3]])
assert 1 == a, a
