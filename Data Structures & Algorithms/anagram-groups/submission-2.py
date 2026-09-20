from collections import defaultdict

def get_key(s: str) -> tuple[int]:
    char_list = [0] * 26
    for c in s:
        char_list[ord(c) - ord('a')] += 1
    return tuple(char_list)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            key = get_key(s)
            anagrams[key].append(s)
        return [anagrams[i] for i in anagrams]
            