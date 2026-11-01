def get_char_map(s: str) -> tuple[int]:
    distro = [0] * 26
    for c in s:
        distro[ord(c) - ord("a")] += 1
    return tuple(distro)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = {}
        for s in strs:
            char_map = get_char_map(s)
            if char_map not in answer:
                answer[char_map] = []
            answer[char_map].append(s)
        return list(answer.values())