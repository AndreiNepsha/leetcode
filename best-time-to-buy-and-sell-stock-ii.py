class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        lp = len(prices)
        proffit = 0
        i = 1
        asc_trend = True
        last_buy = prices[0]
        while i < lp:
            if prices[i - 1] > prices[i]:
                if asc_trend:
                    proffit += prices[i - 1] - last_buy
                    asc_trend = False
                last_buy = prices[i]
            else:
                asc_trend = True
            i += 1
        if asc_trend:
            proffit += prices[i - 1] - last_buy
        return proffit
