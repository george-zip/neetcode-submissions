def to_key(s: str) -> tuple[int]:
    ALPHABET_SIZE = 26
    chars = [0] * ALPHABET_SIZE
    for c in s:
        chars[ord(c) - ord("a")] += 1
    return tuple(chars)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups: dict[tuple[int], list[str]] = {}
        for str in strs:
            key = to_key(str)
            if key not in anagram_groups:
                anagram_groups[key] = []
            anagram_groups[key].append(str)
        return [v for k, v in anagram_groups.items()]
        