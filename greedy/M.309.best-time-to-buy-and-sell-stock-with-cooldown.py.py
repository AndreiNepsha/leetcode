class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        cooldown, sell, hold = 0, 0, float("-inf")

        for p in prices:
            prev_cooldown, prev_sell, prev_hold = cooldown, sell, hold
            cooldown = max(prev_cooldown, prev_sell)
            sell = hold + p
            hold = max(prev_hold, prev_cooldown - p)
        
        return max(sell, cooldown)
