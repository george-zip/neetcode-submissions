class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_val = prices[0]
        for i in range(1, len(prices)):
            min_val = min(min_val, prices[i])
            max_profit = max(max_profit, prices[i] - min_val)
        return max_profit