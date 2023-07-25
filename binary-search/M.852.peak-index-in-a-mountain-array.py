class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        li = len(arr) - 1
        l, r = 0, li

        while l <= r:
            mid = l + (r - l) // 2
            
            if mid < li and arr[mid] < arr[mid + 1]:
                l = mid + 1
            elif mid > 0 and arr[mid] < arr[mid - 1]:
                r = mid - 1
            else:
                return mid
