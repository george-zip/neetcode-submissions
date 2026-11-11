class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eat_bananas(bananas_per_hour):
            hours = 0
            for pile in piles:
                if pile % bananas_per_hour != 0:
                    hours += (pile // bananas_per_hour) + 1
                else:
                    hours += pile // bananas_per_hour
            return hours
        lo, hi = 1, max(piles)
        min_banana_eating_rate = float("inf")
        while lo <= hi:
            mid = (lo + hi) // 2
            if eat_bananas(mid) <= h:
                min_banana_eating_rate = min(min_banana_eating_rate, mid)
                hi = mid - 1
            else:
                lo = mid + 1
        return min_banana_eating_rate
