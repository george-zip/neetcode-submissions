class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer: int = 0
        current_substring: set[str] = set()
        start: int = 0
        end: int = 0
        while end < len(s):
            while start < end and s[end] in current_substring:
                current_substring.remove(s[start])
                start += 1
            current_substring.add(s[end])
            answer = max(answer, len(current_substring))
            end += 1
        return answer