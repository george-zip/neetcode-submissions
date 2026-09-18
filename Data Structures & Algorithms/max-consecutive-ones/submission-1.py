class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_so_far = 0
        current_batch = 0
        for num in nums:
            if num == 1:
                current_batch += 1
                max_so_far = max(max_so_far, current_batch)
            else:
                current_batch = 0
        return max_so_far