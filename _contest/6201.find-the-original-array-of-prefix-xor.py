class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        n = len(pref)
        r = pref[0]
        arr = [r]
        i = 1
        while i < n:
            arr.append(r ^ pref[i])
            r ^= arr[i]
            i += 1
        return arr


pref = [5, 2, 0, 3, 1]
answer = Solution().findArray(pref)
assert [5, 7, 2, 3, 2] == answer, answer
