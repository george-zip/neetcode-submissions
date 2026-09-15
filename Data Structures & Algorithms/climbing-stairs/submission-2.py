
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = { 1: 1, 2: 2 }
        def helper(k):
            if k not in memo:
                memo[k] = helper(k - 1) + helper(k - 2)
            return memo[k]
        return helper(n)