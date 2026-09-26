class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_subarray = nums[0]
        min_subarray = nums[0]
        current_max = 0
        current_min = 0
        total = 0
        for num in nums:
            current_max = max(current_max, 0)
            current_max += num
            max_subarray = max(max_subarray, current_max)
            current_min = min(current_min, 0)
            current_min += num
            min_subarray = min(min_subarray, current_min)
            total += num
        if min_subarray == total:
            return max_subarray
        else:
            return max(
                max_subarray,
                total - min_subarray
            )
