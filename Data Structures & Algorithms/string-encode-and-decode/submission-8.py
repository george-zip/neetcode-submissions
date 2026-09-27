class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(
            f"{len(word)}#{word}" for word in strs
        )

    def decode(self, s: str) -> List[str]:
        words = []
        i = 0
        while i < len(s):
            delimiter_pos = s.find("#", i)
            word_len = int(s[i : delimiter_pos])
            words.append(s[delimiter_pos + 1 : delimiter_pos + word_len + 1])
            i = delimiter_pos + word_len + 1
        return words