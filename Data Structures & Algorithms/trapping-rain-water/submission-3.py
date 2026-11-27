class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        area = 0
        lo, hi = 0, n - 1
        left_max, right_max = height[lo], height[hi]
        while lo < hi:
            if left_max < right_max:
                lo += 1
                left_max = max(left_max, height[lo])
                area += left_max - height[lo]
            else:
                hi -= 1
                right_max = max(right_max, height[hi])
                area += right_max - height[hi]
        return area