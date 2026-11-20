class Solution:
    def findMin(self, nums: List[int]) -> int:
        answer = nums[0]
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] < nums[mid - 1]:
                print(1)
                answer = nums[mid]
                break
            elif nums[lo] <= nums[mid] <= nums[hi]:
                print(2)
                hi = mid - 1
            elif nums[lo] <= nums[mid]:
                print(3)
                # break is on the right
                lo = mid + 1
            else:
                print(4)
                hi = mid - 1
        return answer