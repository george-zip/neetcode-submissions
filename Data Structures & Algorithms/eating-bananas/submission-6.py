def eat_bananas(piles, k) -> int:
    hours = 0
    for pile in piles:
        hours += -(-pile // k)
    return hours

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        min_k = hi
        while lo <= hi:
            k = (lo + hi) // 2
            hours = eat_bananas(piles, k)
            if hours > h:
                lo = k + 1
            else:
                hi = k - 1
                min_k = min(min_k, k)
        return min_k
        