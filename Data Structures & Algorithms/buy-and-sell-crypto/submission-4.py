class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        current_min = prices[0]
        for i in range(1, len(prices)):
            px = prices[i]
            profit = px - current_min
            max_profit = max(max_profit, profit)
            current_min = min(current_min, px)
        return max_profit