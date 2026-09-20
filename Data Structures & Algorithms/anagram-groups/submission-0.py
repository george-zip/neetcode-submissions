from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for str in strs:
            key = "".join(sorted(str))
            anagrams[key].append(str)
        return [anagrams[i] for i in anagrams]
            