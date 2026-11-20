class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for px in prices:
            min_price = min(min_price, px)
            max_profit = max(max_profit, px - min_price)
        return max_profit