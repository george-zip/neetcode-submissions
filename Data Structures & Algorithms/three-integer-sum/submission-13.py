class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = set()
        nums_sorted = sorted(nums)
        # print(f"{nums_sorted=}")
        for i, num in enumerate(nums_sorted):
            j = i + 1
            k = len(nums_sorted) - 1
            while j < k:
                # print(f"{num=},{nums_sorted[j]=},{nums_sorted[k]=}")
                if nums_sorted[j] + nums_sorted[k] == -num:
                    answer.add(
                        tuple(sorted([num, nums_sorted[j], nums_sorted[k]]))
                    )
                    j += 1
                    k -= 1 
                elif (nums_sorted[j] + nums_sorted[k]) > -num:
                    k -= 1
                else:
                    j += 1
        return list(answer)