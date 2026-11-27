class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        lo, hi = 0, n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if mid > 0 and nums[mid] < nums[mid - 1]:
                return nums[mid]
            elif mid < n -1 and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
        return nums[lo]