class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water_units = 0
        i = 0
        j = len(heights) - 1
        while i < j:
            current_water_units = (j -i) * min(heights[i], heights[j])
            max_water_units = max(max_water_units, current_water_units)
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
        return max_water_units