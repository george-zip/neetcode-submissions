class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(
            [f"{len(s)}#{s}" for s in strs]
        )

    def decode(self, s: str) -> List[str]:
        answer = []
        i = 0
        while i < len(s):
            delimiter_idx = s.find("#", i)
            word_len = int(s[i:delimiter_idx])
            answer.append(
                s[delimiter_idx + 1 : delimiter_idx + word_len + 1]
            )
            i = delimiter_idx + word_len + 1
        return answer