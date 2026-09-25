class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_px_by_day = prices.copy()
        # calculate the maximum that you can sell for on 
        # a given day if you sell it on or after this day
        for i in range(len(prices) - 2, -1, -1):
            max_px_by_day[i] = max(
                max_px_by_day[i + 1],
                max_px_by_day[i]
            )
        # now, assuming you buy in day i, calculate the max
        # profit based on the max_px_by_day at i
        max_profit = 0
        for i in range(len(prices)):
            max_profit = max(
                max_profit,
                max_px_by_day[i] - prices[i]
            )
        return max_profit