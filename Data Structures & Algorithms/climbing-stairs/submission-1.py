cache = {
    1: 1,
    2: 2
}

class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 0:
            return 0
        elif n not in cache:
            cache[n] = self.climbStairs(n - 1) + \
            self.climbStairs(n - 2)
        return cache[n]
