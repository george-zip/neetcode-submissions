class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_vals = set()
        for num in nums:
            if num in unique_vals:
                return True
            unique_vals.add(num)
        return False