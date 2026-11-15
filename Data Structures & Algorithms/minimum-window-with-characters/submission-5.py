from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = Counter(t)
        s_count = Counter()
        left = 0
        min_substring = ""
        need = len(t_count)
        for right in range(len(s)):
            c = s[right]
            s_count[c] += 1
            if s_count[c] == t_count[c]:
                need -= 1
            while need == 0:
                if not min_substring or len(min_substring) > right - left + 1:
                    min_substring = s[left : right + 1]
                c = s[left]
                s_count[c] -= 1
                if s_count[c] < t_count[c]:
                    need += 1
                left += 1

        return min_substring