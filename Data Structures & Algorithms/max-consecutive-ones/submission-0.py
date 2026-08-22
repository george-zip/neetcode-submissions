class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones_len = 0
        this_range_len = 0
        for num in nums:
            if num == 1:
                this_range_len += 1
                max_ones_len = max(max_ones_len, this_range_len)
            else:
                this_range_len = 0
        return max_ones_len