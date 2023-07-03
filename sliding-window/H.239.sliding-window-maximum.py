
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        q = deque()

        for i in range(k):
            while len(q) > 0 and q[-1] < nums[i]:
                q.pop()
            q.append(nums[i])

        swm = [q[0]]
        for i in range(len(nums) - k):
            if nums[i] == q[0]:
                q.popleft()
            while len(q) > 0 and q[-1] < nums[k + i]:
                q.pop()
            q.append(nums[k + i])
            swm.append(q[0])
        return swm


a = Solution().maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3)
assert [3,3,5,5,6,7] == a, a
