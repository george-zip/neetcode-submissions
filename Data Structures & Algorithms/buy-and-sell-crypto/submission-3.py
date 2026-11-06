class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        current_min = prices[0]
        for px in prices:
            profit = px - current_min
            max_profit = max(max_profit, profit)
            current_min = min(current_min, px)
        return max_profit