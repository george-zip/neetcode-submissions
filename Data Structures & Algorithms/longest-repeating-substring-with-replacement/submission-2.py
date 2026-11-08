from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_char_count = defaultdict(lambda: 0)
        left = 0
        max_len = 1
        max_frequency = 1
        for right in range(len(s)):
            c = s[right]
            window_len = right - left + 1
            window_char_count[c] += 1
            max_frequency = max(max_frequency, window_char_count[c])
            while window_len - max_frequency > k:
                leaving = s[left]
                window_char_count[leaving] -= 1
                left += 1
                window_len = right - left + 1
            max_len = max(max_len, window_len)
        return max_len