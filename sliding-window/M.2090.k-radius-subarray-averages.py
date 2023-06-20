class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        ln = len(nums)
        avgs = [-1] * ln
        if k * 2 + 1 > ln:
            return avgs
        end = ln - k
        w = k * 2 + 1
        s = sum(nums[:k + k + 1])
        avgs[k] = s // w
        for i in range(k + 1, end):
            s -= nums[i - k - 1]
            s += nums[i + k]
            avgs[i] = s // w
        return avgs