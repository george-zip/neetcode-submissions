class Solution:
    def search(self, nums: List[int], target: int) -> int:
        answer = -1
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                answer = mid
                break
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return answer