ALPHABET_SIZE = 26

def get_count(s: str) -> list[int]:
    letter_counts = [0] * ALPHABET_SIZE
    for c in s:
        letter_counts[ord(c) - ord('a')] += 1
    return letter_counts

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = get_count(s)
        t_count = get_count(t)
        for i in range(ALPHABET_SIZE):
            if s_count[i] != t_count[i]:
                return False
        return True
