class Solution:

    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            try:
                val = int(op)
                stack.append(val)
            except ValueError:
                if op == 'D':
                    stack.append(stack[-1] * 2)
                elif op == '+':
                    stack.append(stack[-1] + stack[-2])
                elif op == 'C':
                    stack.pop()

        return sum(stack)