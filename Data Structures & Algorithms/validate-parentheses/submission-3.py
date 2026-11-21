paren_pairs = {
    '}':'{',
    ']':'[',
    ')':'('
}

class Solution:
    def isValid(self, s: str) -> bool:
        paren_stack = []
        for c in s:
            if c in paren_pairs:
                if not paren_stack:
                    return False
                open_bracket = paren_stack.pop()
                if paren_pairs[c] != open_bracket:
                    return False
            else:
                paren_stack.append(c)
        return len(paren_stack) == 0