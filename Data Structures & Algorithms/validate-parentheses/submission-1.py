pairs = {
    ')': '(',
    '}': '{',
    ']': '['
}

class Solution:
    def isValid(self, s: str) -> bool:
        op_stack = []
        for c in s:
            if c in ('(', '{', '['):
                op_stack.append(c)
            elif op_stack:
                op = op_stack.pop()
                if pairs[c] != op:
                    return False
            else:
                return False
        return len(op_stack) == 0