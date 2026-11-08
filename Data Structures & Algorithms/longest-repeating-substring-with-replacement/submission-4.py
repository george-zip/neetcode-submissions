from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_char_count = defaultdict(lambda: 0)
        left = 0
        max_len = 1
        max_frequency = 1
        for right in range(len(s)):
            joining = s[right]
            window_char_count[joining] += 1
            max_frequency = max(max_frequency, window_char_count[joining])
            while (right - left + 1) - max_frequency > k:
                leaving = s[left]
                window_char_count[leaving] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len