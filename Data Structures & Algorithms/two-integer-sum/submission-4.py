class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = {}
        for idx, num in enumerate(nums):
            other_num = target - num
            if target - num in vals:
                return [vals[other_num], idx]
            vals[num] = idx
        return []
