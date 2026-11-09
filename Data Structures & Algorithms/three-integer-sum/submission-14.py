class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer_set = set()
        nums_sorted = sorted(nums)
        for i, num in enumerate(nums_sorted):
            j = i + 1
            k = len(nums_sorted) - 1
            while j < k:
                if (nums_sorted[j] + nums_sorted[k]) == -num:
                    answer_set.add(
                        tuple(
                            sorted(
                                [nums_sorted[j], nums_sorted[k], num]
                            )
                        )
                    )
                    j += 1
                    k -= 1
                elif (nums_sorted[j] + nums_sorted[k]) > -num:
                    k -= 1
                else:
                    j += 1
        return list(answer_set)