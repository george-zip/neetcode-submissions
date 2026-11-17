from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest_substring_len = 1
        char_count = Counter()
        left = 0
        max_char_count = 0
        for right, char in enumerate(s):
            print(f"1. {char}")
            char_count[char] += 1
            max_char_count = max(
                max_char_count,
                char_count[char]
            )
            while (right - left + 1) - max_char_count > k:
                char = s[left]
                print(f"{char}")
                char_count[char] -= 1
                left += 1
            longest_substring_len = max(
                longest_substring_len,
                right - left + 1
            )

        return longest_substring_len