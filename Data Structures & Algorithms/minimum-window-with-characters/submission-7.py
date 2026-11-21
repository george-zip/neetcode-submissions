from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_window = ""
        t_count = Counter(t)
        s_count = Counter()
        left = 0
        need = len(t_count)
        for right, char in enumerate(s):

            if char in t_count:
                s_count[char] += 1
                if s_count[char] == t_count[char]:
                    need -= 1

            while need == 0:
                if not min_window or right - left + 1 < len(min_window):
                    min_window = s[left:right + 1]
                char = s[left]
                if char in t_count:
                    s_count[char] -= 1
                    if s_count[char] < t_count[char]:
                        need += 1
                left += 1

        return min_window                
