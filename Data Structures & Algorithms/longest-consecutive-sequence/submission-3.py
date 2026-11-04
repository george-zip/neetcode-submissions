class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num_set = set(nums)
        max_seq_len = 1
        current_seq_len = 1
        while num_set:
            current = num_set.pop()
            i = 1
            while current - i in num_set:
                num_set.remove(current - i)
                i += 1
                current_seq_len += 1
            i = 1
            while current + i in num_set:
                num_set.remove(current + i)
                i += 1
                current_seq_len += 1
            max_seq_len = max(max_seq_len, current_seq_len)
            current_seq_len = 1
        return max_seq_len