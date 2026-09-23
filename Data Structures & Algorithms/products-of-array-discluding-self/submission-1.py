class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answers = [0] * len(nums)
        answers[0] = nums[0]
        for i in range(1, len(nums)):
            answers[i] = answers[i - 1] * nums[i]
        multiplier = 1
        for i in range(len(nums) - 1, 0, -1):
            answers[i] = answers[i - 1] * multiplier
            multiplier *= nums[i]
        answers[0] = multiplier
        return answers