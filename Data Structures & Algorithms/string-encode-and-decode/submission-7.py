class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(
            str(len(s)) + "#" + s for s in strs
        )


    def decode(self, s: str) -> List[str]:
        answer = []
        i = 0
        while i < len(s):
            j = s.index("#", i)
            length = int(s[i:j])
            i = j + 1
            answer.append(s[i:i+length])
            i += length
        return answer
