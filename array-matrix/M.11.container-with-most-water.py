class Solution:
    def maxArea(self, h: list[int]) -> int:
        l, r = 0, len(h) - 1
        lh, rh = h[l], h[r]
        area = r * min(h[l], h[r])
        while l < r:
            if rh > lh:
                while l < r and lh >= h[l]:
                    l += 1
                lh = max(h[l], lh)
            else:
                while l < r and rh >= h[r]:
                    r -= 1
                rh = max(h[r], rh)
            area = max(area, (r - l) * min(lh, rh))
        return area


a = Solution().maxArea([1,3,2,5,25,24,5])
assert 24 == a, a

a = Solution().maxArea([1,8,6,2,5,4,8,3,7])
assert 49 == a, a

a = Solution().maxArea([1,1])
assert 1 == a, a
