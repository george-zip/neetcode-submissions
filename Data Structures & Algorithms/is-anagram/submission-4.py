def get_distribution(s: str):
    d = [0] * 26
    for c in s:
        d[ord(c) - ord("a")] += 1
    return d

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return get_distribution(s) == get_distribution(t)
