from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_count = Counter(s1)
        j = len(s1)
        s2_count = Counter(s2[:j - 1])
        while j <= len(s2):
            # print(f"Before {j=},{s2_count=}")
            arriving = s2[j - 1]
            s2_count[arriving] += 1
            if s1_count == s2_count:
                return True
            leaving = s2[j - len(s1)]
            s2_count[leaving] -= 1
            if s2_count[leaving] == 0:
                s2_count.pop(leaving)
            # print(f"{arriving=},{leaving=},{s1_count=},{s2_count=}")
            j += 1
        return False