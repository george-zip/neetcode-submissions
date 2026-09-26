class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_indices: dict[int, int] = {}
        for idx, num in enumerate(nums):
            if target - num in num_indices:
                return [num_indices[target - num], idx]
            num_indices[num] = idx
