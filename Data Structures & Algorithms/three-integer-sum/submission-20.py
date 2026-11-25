class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answers = set()
        nums_sorted = sorted(nums)
        for i in range(len(nums_sorted)):
            j = i + 1
            k = len(nums_sorted) - 1
            while j < k:
                if nums_sorted[i] + nums_sorted[j] + nums_sorted[k] == 0:
                    answers.add(
                        tuple([nums_sorted[i], nums_sorted[j], nums_sorted[k]])
                    )
                    j += 1
                    k -= 1
                elif nums_sorted[k] + nums_sorted[j] > -nums_sorted[i]:
                    k -= 1
                else:
                    j += 1
        return list(answers)