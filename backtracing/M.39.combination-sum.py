class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        ln = len(candidates)

        def collect(ind, rem):
            if ind == ln:
                return []

            collected = []
            for i in range(rem // candidates[ind] + 1):
                if i * candidates[ind] == rem:
                    collected.append([candidates[ind]] * i)
                else:
                    collected += [
                        ([candidates[ind]] * i if i > 0 else []) + c 
                        for c in collect(ind + 1, rem - i * candidates[ind])
                    ]
            return collected

        return collect(0, target)

candidates = [2,3,6,7]
target = 7
a = Solution().combinationSum(candidates, target)
assert [[2,2,3],[7]] == a, a
