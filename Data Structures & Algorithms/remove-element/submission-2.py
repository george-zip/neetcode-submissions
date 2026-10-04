class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        insertion_point = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[insertion_point] = nums[i]
                insertion_point += 1
        return insertion_point