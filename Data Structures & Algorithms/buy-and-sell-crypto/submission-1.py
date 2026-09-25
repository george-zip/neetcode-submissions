class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest_price_so_far = prices[0]
        for px in prices:
            lowest_price_so_far = min(
                lowest_price_so_far,
                px
            )
            max_profit = max(
                max_profit,
                px - lowest_price_so_far
            )
        return max_profit