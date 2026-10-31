def get_distribution(s: str):
    d = [0] * 26
    for c in s:
        d[ord(c) - ord("a")] += 1
    return d

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_distro = get_distribution(s) 
        for c in t:
            s_distro[ord(c) - ord("a")] -= 1
        return all(val == 0 for val in s_distro)
