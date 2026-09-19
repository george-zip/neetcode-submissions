from collections import namedtuple

StackPair = namedtuple('StackPair', ['val', 'min_val'])

class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        stack_min = min(val, self.stack[-1].min_val) if self.stack else val
        self.stack.append(StackPair(val, stack_min))
            

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1].val

    def getMin(self) -> int:
        return self.stack[-1].min_val
        
