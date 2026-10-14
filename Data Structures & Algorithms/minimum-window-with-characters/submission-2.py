from collections import Counter

def _contains_all_the_chars(counts_to_match, counts_in_window):
    for char in counts_to_match:
        if counts_in_window[char] < counts_to_match[char]:
            return False
    return True

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        t_char_counts = Counter(t)        
        s_char_counts = Counter()
        res = ""
        need, have = len(t_char_counts), 0
        l = 0
        for r in range(len(s)):
            c = s[r]
            if c in t_char_counts:
                s_char_counts[c] += 1
                if s_char_counts[c] == t_char_counts[c]:
                    have += 1
                while have == need:
                    if not res or r - l + 1 < len(res):
                        res = s[l:r+1]
                    if s[l] in t_char_counts:
                        s_char_counts[s[l]] -= 1
                        if s_char_counts[s[l]] < t_char_counts[s[l]]:
                            have -= 1
                    l += 1
        return res