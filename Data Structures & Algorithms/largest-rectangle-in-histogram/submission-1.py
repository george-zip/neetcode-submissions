class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        bar_stack = []
        for idx, height in enumerate(heights):
            start = idx
            while bar_stack and height < bar_stack[-1][1]:
                prev_idx, prev_height = bar_stack.pop()
                max_area = max(
                    max_area,
                    (idx - prev_idx) * prev_height
                )
                start = prev_idx
            bar_stack.append((start, height))

        for idx, height in bar_stack:
            max_area = max(
                max_area,
                (len(heights) - idx) * height
            )

        return max_area