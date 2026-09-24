import operator as op
from collections.abc import Callable

def next_unique(nums: list[int], index: int, operation: Callable, stop: int):
    val = nums[index]
    while index != stop:
        if nums[index] != val:
            return index
        index = operation(index, 1)
    return index

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_sorted = sorted(nums)
        triplets = []
        i = 0
        while i < len(nums_sorted):
            j = i + 1
            k = len(nums_sorted) - 1
            while j < k:
                if nums_sorted[i] + nums_sorted[j] + nums_sorted[k] == 0:
                    triplets.append([nums_sorted[i], nums_sorted[j], nums_sorted[k]])
                    j = next_unique(nums_sorted, j, op.add, k)
                    k = next_unique(nums_sorted, k, op.sub, j)
                elif nums_sorted[i] + nums_sorted[j] + nums_sorted[k] < 0:
                    j = next_unique(nums_sorted, j, op.add, k)
                else:
                    k = next_unique(nums_sorted, k, op.sub, j)
            i = next_unique(nums_sorted, i, op.add, len(nums_sorted))
        return triplets