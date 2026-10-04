class MinStack:

    def __init__(self):
        self.vals_stack = []

    def push(self, val: int) -> None:
        min_val = min(val, self.vals_stack[-1][1] if self.vals_stack else val)
        self.vals_stack.append((val, min_val))

    def pop(self) -> None:
        self.vals_stack.pop()

    def top(self) -> int:
        return self.vals_stack[-1][0]

    def getMin(self) -> int:
        return self.vals_stack[-1][1]
