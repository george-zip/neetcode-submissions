class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest = prices[0]
        for i in range(1, len(prices)):
            px = prices[i]
            lowest = min(lowest, px)
            max_profit = max(max_profit, px - lowest)
        return max_profit