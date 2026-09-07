from heapq import heappush


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_val = None

    def _find_min_val(self):
        return min(self.stack)

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_val is None or self.min_val > val:
            self.min_val = val

    def pop(self) -> None:
        val = self.stack.pop()
        if not self.stack:
            self.min_val = None
        elif val == self.min_val:
            self.min_val = self._find_min_val()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_val
