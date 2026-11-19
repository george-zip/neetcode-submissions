from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        s2_count = Counter()
        left = 0
        for right, c in enumerate(s2):
            s2_count[c] += 1
            if right - left + 1 > len(s1):
                c = s2[left]
                s2_count[c] -= 1
                left += 1
            # print(s2[left:right+1], s2_count)
            if s1_count == s2_count:
                return True
        return False

