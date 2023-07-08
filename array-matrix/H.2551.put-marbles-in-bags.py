class Solution:
    def _putMarbles(self, weights: list[int], k: int) -> int:
        n = len(weights)
        s = weights[0] + weights[n - 1]

        max_s = 0
        min_s = float("inf")
        def backtrace(last_part, parts_left):
            nonlocal s, max_s, min_s

            if not parts_left:
                max_s = max(max_s, s)
                min_s = min(min_s, s)
                return

            for i in range(last_part + 1, n - parts_left):
                dif = weights[i] + weights[i + 1]
                s += dif
                backtrace(i, parts_left - 1)
                s -= dif
        
        backtrace(-1, k - 1)
        return max_s - min_s

    def putMarbles(self, weights: list[int], k: int) -> int:
        n = len(weights)
        split_scores = sorted([weights[i] + weights[i + 1] for i in range(n - 1)])
        return  sum(split_scores[n - k:]) - sum(split_scores[:k - 1])


a = Solution().putMarbles(weights = [1,3,5,1], k = 2)
assert 4 == a, a

a = Solution().putMarbles(weights = [1,4,2,5,2], k = 3)
assert 3 == a, a
