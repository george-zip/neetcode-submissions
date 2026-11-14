from collections import defaultdict

def get_key(s):
    chars = [0] * 26
    for c in s:
        chars[ord(c) - ord("a")] += 1
    return tuple(chars)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(lambda: [])
        for s in strs:
            groups[get_key(s)].append(s)
        return list(groups.values())