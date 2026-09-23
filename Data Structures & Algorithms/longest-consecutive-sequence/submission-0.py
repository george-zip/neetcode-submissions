class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        def sequence_start(num):
            return num in num_set and num - 1 not in num_set

        longest_sequence = 0
        for num in nums:
            if sequence_start(num):
                current_val = num
                while current_val + 1 in num_set:
                    current_val += 1
                longest_sequence = max(
                    longest_sequence, 
                    current_val - num + 1
                )
        return longest_sequence