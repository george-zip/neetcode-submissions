class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(
            f"{len(s)}#{s}" for s in strs
        )

    def decode(self, s: str) -> List[str]:
        answer = []
        i = 0
        while i < len(s):
            delimiter = s.find("#", i)
            if delimiter == -1:
                break
            str_len = int(s[i : delimiter])
            answer.append(s[delimiter + 1: delimiter + str_len + 1])
            i = delimiter + str_len + 1
        return answer
            