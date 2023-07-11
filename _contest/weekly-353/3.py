from collections import defaultdict


class Solution:
    def maxNonDecreasingLength(self, nums1: list[int], nums2: list[int]) -> int:
        n = len(nums1)
        
        dp = defaultdict(int)
        dp[(0, nums1[0])] = 1
        dp[(0, nums2[0])] = 1

        longest = 0
        
        for i in range(1, n):
            f = max(
                dp[(i - 1, nums1[i - 1])] if nums1[i] >= nums1[i - 1] else 0, 
                dp[(i - 1, nums2[i - 1])] if nums1[i] >= nums2[i - 1] else 0,
            ) + 1
            
            s = max(
                dp[(i - 1, nums1[i - 1])] if nums2[i] >= nums1[i - 1] else 0, 
                dp[(i - 1, nums2[i - 1])] if nums2[i] >= nums2[i - 1] else 0,
            ) + 1

            longest = max(longest, f, s)
        
            dp[(i, nums1[i])] = f
            dp[(i, nums2[i])] = s
        
        return longest
            




a = Solution().maxNonDecreasingLength(nums1 = [14,4], nums2=[2,13])
assert 2 == a, a
