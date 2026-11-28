class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for idx, height in enumerate(heights):
            start = idx
            while stack and height < stack[-1][1]:
                prev_start_idx, prev_height = stack.pop()
                max_area = max(
                    max_area,
                    (idx - prev_start_idx) * prev_height
                )
                start = prev_start_idx
            stack.append((start, height))
        print(stack)
        print(max_area)
        for start_idx, height in stack:
            max_area = max(
                max_area,
                (len(heights) - start_idx) * height
            )
        return max_area