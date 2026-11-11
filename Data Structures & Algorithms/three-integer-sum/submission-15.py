class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer_set = set()
        nums_sorted = sorted(nums)
        for i, num in enumerate(nums_sorted):
            j = i + 1
            k = len(nums_sorted) - 1
            while j < k:
                combined = nums_sorted[j] + nums_sorted[k]
                if combined == -num:
                    answer_set.add(
                        tuple(sorted([num, nums_sorted[j], nums_sorted[k]]))
                    )
                    k -= 1
                    j += 1
                elif combined > -num:
                    k -= 1
                else:
                    j += 1
        return list(answer_set)