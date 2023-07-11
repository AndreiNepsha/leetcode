class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        sell = 0
        buy = float("-inf")
        for p in prices:
            buy = max(buy, sell - p)
            sell = max(sell, buy + p - fee)
        return sell
