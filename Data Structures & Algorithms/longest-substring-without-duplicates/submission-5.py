from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring = 0
        chars = Counter()
        left = 0
        for right, c in enumerate(s):
            chars[c] += 1
            # print(f"{chars=}")
            while chars[c] > 1:
                lc = s[left]
                chars[lc] -= 1
                left += 1
            # print(f"{s[left:right+1]=}")
            longest_substring = max(
                longest_substring,
                right - left + 1
            )
        return longest_substring