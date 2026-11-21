def char_count(s):
    chars = [0] * 26
    for c in s:
        chars[ord(c) - ord("a")] += 1
    return chars

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = char_count(s)
        for c in t:
            s_count[ord(c) - ord("a")] -= 1
        return all(c == 0 for c in s_count)