class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previous_nums = {}
        for idx, num in enumerate(nums):
            remainder = target - num
            if remainder in previous_nums:
                return [previous_nums[remainder], idx]
            previous_nums[num] = idx