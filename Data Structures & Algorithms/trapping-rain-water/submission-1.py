class Solution:
    def trap(self, height: List[int]) -> int:
        # left_to_right_heights = [0] * len(height)
        # max_height = 0
        # for i in range(1, len(height)):
        #     max_height = max(max_height, height[i - 1])
        #     left_to_right_heights[i] = max_height
        right_to_left_heights = [0] * len(height)
        max_height = 0
        for i in range(len(height) - 2, -1, -1):
            max_height = max(max_height, height[i + 1])
            right_to_left_heights[i] = max_height
        # print(f"{right_to_left_heights=}")
        max_height = 0
        total_water = 0
        for i in range(1, len(height) - 1):
            max_height = max(max_height, height[i - 1])
            water_amount = max(
                min(max_height, right_to_left_heights[i]) - height[i],
                0
            )
            # print(f"{i=},{max_height=},{right_to_left_heights[i]=},{water_amount=},{total_water=},{height[i]=}")
            total_water += water_amount
        return total_water
