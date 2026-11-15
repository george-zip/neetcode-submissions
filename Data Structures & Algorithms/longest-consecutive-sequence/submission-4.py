class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_sequence = 0
        while num_set:
            val = num_set.pop()
            current_sequence = 1
            i = 1
            while val - i in num_set:
                num_set.remove(val - i)
                i += 1
                current_sequence += 1
            i = 1
            while val + i in num_set:
                num_set.remove(val + i)
                i += 1
                current_sequence += 1
            longest_sequence = max(
                longest_sequence,
                current_sequence
            )
        return longest_sequence
