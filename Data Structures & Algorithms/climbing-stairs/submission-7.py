from functools import lru_cache

class Solution:

    @lru_cache
    def climbStairs(self, n: int) -> int:
        if n <= 0:
            return 0
        elif n in (1, 2):
            return n
        else:
            return (self.climbStairs(n - 1) +
                    self.climbStairs(n - 2))
        
