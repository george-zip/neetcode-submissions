class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring = 0
        chars: dict[str, int] = {}
        left = 0
        for right, c in enumerate(s):
            if c in chars:
                old_idx = chars[c]
                if old_idx >= left:
                    left = old_idx + 1
            chars[c] = right        
            longest_substring = max(
                longest_substring,
                right - left + 1
            )
        return longest_substring
