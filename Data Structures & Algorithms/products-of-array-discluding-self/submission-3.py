class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_to_right = [0] * len(nums)
        left_to_right[0] = nums[0]
        for i in range(1, len(nums)):
            left_to_right[i] = left_to_right[i - 1] * nums[i]
        # print(f"{left_to_right=}")
        right_to_left = [0] * len(nums)
        right_to_left[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            right_to_left[i] = right_to_left[i + 1] * nums[i]
        # print(f"{left_to_right=}")
        answer = [0] * len(nums)
        answer[0] = right_to_left[1]
        answer[-1] = left_to_right[-2]
        for i in range(1, len(nums) - 1):
            answer[i] = left_to_right[i-1] * right_to_left[i+1]
        return answer
