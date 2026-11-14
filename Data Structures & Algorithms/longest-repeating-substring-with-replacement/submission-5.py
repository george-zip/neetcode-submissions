from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 1
        char_count = Counter()
        left = 0
        max_frequency = 0
        for right in range(len(s)):
            c = s[right]
            char_count[c] += 1

            max_frequency = max(
                max_frequency,
                char_count[c]
            )

            while (right - left + 1) - max_frequency > k:
                c = s[left]
                char_count[c] -= 1
                left += 1

            max_len = max(
                max_len,
                right - left + 1
            )
        return max_len