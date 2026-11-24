from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest_distinct = 1
        biggest_char = 0
        char_count = Counter()
        left = 0
        for right, char in enumerate(s):

            char_count[char] += 1
            biggest_char = max(biggest_char, char_count[char])

            while (right - left + 1) - biggest_char > k: 
                char = s[left]
                char_count[char] -= 1
                left += 1

            longest_distinct = max(
                longest_distinct,
                right - left + 1
            )
            
        return longest_distinct