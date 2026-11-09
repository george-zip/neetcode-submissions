from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = Counter(t)
        s_count = Counter()
        left = 0
        answer = ""
        matches = 0
        for right in range(len(s)):
            c = s[right]
            s_count[c] += 1
            if s_count[c] == t_count[c]:
                matches += 1
            while matches == len(t_count):
                if not answer or right - left + 1 < len(answer):
                    answer = s[left:right + 1]
                c = s[left]
                s_count[c] -=1
                left += 1
                if s_count[c] < t_count[c]:
                    matches -= 1
        return answer