class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = set()
        nums_sorted = sorted(nums)
        # print(nums_sorted)
        for idx, num in enumerate(nums_sorted):
            left = idx + 1
            right = len(nums_sorted) - 1
            while left < right:
                # print(num, nums_sorted[left], nums_sorted[right])
                if num + nums_sorted[left] + nums_sorted[right] == 0:
                    answer.add(tuple([num, nums_sorted[left], nums_sorted[right]]))
                    left += 1
                    right -= 1
                elif nums_sorted[left] + nums_sorted[right] > -num:
                    right -= 1
                else:
                    left += 1
        return list(answer)