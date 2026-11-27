class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        right_to_left = [0] * n
        for i in range(n - 2, -1, -1):
            right_to_left[i] = max(
                height[i + 1],
                right_to_left[i + 1]
            )
        # print(right_to_left)
        left_to_right = [0] * n
        for i in range(1, n):
            left_to_right[i] = max(
                height[i - 1],
                left_to_right[i - 1]
            ) 
        # print(left_to_right)
        area = 0
        for i in range(1, n - 1):
            wall_height = min(left_to_right[i], right_to_left[i])
            # print(f"{i=},{wall_height=},{height[i]=}")
            area += max(wall_height - height[i], 0)
        return area
        
