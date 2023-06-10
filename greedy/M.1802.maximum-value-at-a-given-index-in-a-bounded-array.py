class Solution:
    def maxValue(self, n: int, index: int, max_sum: int) -> int:
        def count_sum(peak):
            leftmost = max(peak - index, 0)
            s = (peak + leftmost) * (peak - leftmost + 1) // 2
            rightmost = max(peak - ((n-1) - index), 0)
            s += (peak + rightmost) * (peak - rightmost + 1) // 2
            return s - peak # peak counted twice
        
        max_sum -= n
        left, right = 1, max_sum + 1

        while left < right:
            mid = (right - left) // 2 + left
            if count_sum(mid) > max_sum:
                right = mid
            else:
                left = mid + 1

        return left


n, index, max_sum = 4, 2, 6
a = Solution().maxValue(n, index, max_sum)
assert 2 == a, a

n, index, max_sum = 6, 1, 10
a = Solution().maxValue(n, index, max_sum)
assert 3 == a, a

n, index, max_sum = 4, 0, 4
a = Solution().maxValue(n, index, max_sum)
assert 1 == a, a

n, index, max_sum = 3, 2, 18
a = Solution().maxValue(n, index, max_sum)
assert 7 == a, a

n, index, max_sum = 3, 0, 815094800
a = Solution().maxValue(n, index, max_sum)
assert 271698267 == a, a
