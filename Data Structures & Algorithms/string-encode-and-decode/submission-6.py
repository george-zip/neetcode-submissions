class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(
            str(len(s)) + "#" + s for s in strs
        )


    def decode(self, s: str) -> List[str]:
        answer = []
        i = 0
        while i < len(s):
            str_len = ""
            while s[i] != "#":
                str_len += s[i]
                i += 1
            word_len = int(str_len)
            i += 1
            starting_point = i
            word = ""
            while i < starting_point + word_len:
                word += s[i]
                i += 1
            answer.append(word)
        return answer
