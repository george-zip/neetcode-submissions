class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        chars = set()
        left = 0
        for right in range(len(s)):
            c = s[right]
            while c in chars:
                chars.remove(s[left])
                left += 1
            chars.add(c)
            max_len = max(max_len, right - left + 1)
        return max_len
        