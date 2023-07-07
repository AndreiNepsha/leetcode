class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        def check(day: int):
            l = -1
            bouquets = 0
            for r, bd in enumerate(bloomDay):
                if bd <= day:
                    if r - l == k:
                        bouquets += 1
                        l = r
                else:
                    l = r
                if bouquets == m:
                    return True
            return False
        
        days = sorted(set(bloomDay))
        left, right = 0, len(days)

        found = False
        while left < right:
            mid = left + (right - left) // 2
            if check(days[mid]):
                right = mid
                found = True
            else:
                left = mid + 1
        return days[right] if found else -1


a = Solution().minDays(bloomDay = [1,10,3,10,2], m = 3, k = 1)
assert 3 == a, a

a = Solution().minDays(bloomDay = [1,10,3,10,2], m = 3, k = 2)
assert -1 == a, a

a = Solution().minDays(bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3)
assert 12 == a, a
