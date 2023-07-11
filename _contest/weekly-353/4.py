from collections import defaultdict, deque


class Solution:
    def checkArray(self, nums: list[int], k: int) -> bool:
        if k == 1:
            return True
        
        subtract_queue = deque()
        
        n = len(nums)
        subtract = 0
        for i in range(n):
            while subtract_queue and i >= subtract_queue[0][1]:
                subtract -= subtract_queue.popleft()[0]
            nums[i] -= subtract
            if i + k <= n:
                if nums[i] < 0:
                    return False
                if nums[i] > 0:
                    subtract_queue.append((nums[i], i + k))
                    subtract += nums[i]
                    nums[i] = 0
            else:
                if nums[i] != 0:
                    return False
        return True
            

a = Solution().checkArray(nums = [89,8,8,8,8,8,8,8,8,8,8,8], k=12)
assert not a, a

a = Solution().checkArray(nums = [0,45,82,98,99], k=4)
assert not a, a

a = Solution().checkArray(nums = [2,2,3,1,1,0], k=3)
assert a, a

a = Solution().checkArray(nums = [0,16,0,29,0,0,0,9,0,0,0,0,0,0,0,0,0,95,49,0,0,0,0,68], k=24)
assert not a, a

a = Solution().checkArray(nums = [1,3,1,1], k=2)
assert not a, a


