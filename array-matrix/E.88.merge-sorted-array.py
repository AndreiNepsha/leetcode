class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        i, k, e = m - 1, n - 1, n + m - 1
        while e > -1:
            if k < 0 or (i >= 0 and  nums1[i] > nums2[k]):
                nums1[e] = nums1[i]
                i -= 1
            else:
                nums1[e] = nums2[k]
                k -= 1
            e -= 1

nums1 = [1,2,3,0,0,0]
a = Solution().merge(nums1 = nums1, m = 3, nums2 = [2,5,6], n = 3)
assert [1,2,2,3,5,6] == nums1, nums1


nums1 = [4,5,6,0,0,0]
a = Solution().merge(nums1 = nums1, m = 3, nums2 = [1,2,3], n = 3)
assert [1,2,3,4,5,6] == nums1, nums1

nums1 = [1]
a = Solution().merge(nums1 = nums1, m = 1, nums2 = [], n = 0)
assert [1] == nums1, nums1