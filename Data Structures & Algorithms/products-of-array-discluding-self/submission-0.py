class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left2right = [0] * len(nums)
        left2right[0] = nums[0]
        for i in range(1, len(nums)):
            left2right[i] = left2right[i - 1] * nums[i]
        right2left = [0] * len(nums)
        right2left[-1] = nums[-1]
        for i in range(len(nums) - 2, 0, -1):
            right2left[i] = right2left[i + 1] * nums[i]
        answers = [0] * len(nums)
        answers[0] = right2left[1]
        answers[-1] = left2right[-2]
        for i in range(1, len(nums) - 1):
            answers[i] = left2right[i - 1] * right2left[i + 1]
        return answers