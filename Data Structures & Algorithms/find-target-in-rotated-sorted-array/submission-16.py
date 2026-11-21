class Solution:
    def search(self, nums: List[int], target: int) -> int:
        answer = -1
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            print(nums[mid])
            if nums[mid] == target:
                answer = mid
                break
            elif nums[lo] <= nums[mid]:
                # left side is sorted
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return answer