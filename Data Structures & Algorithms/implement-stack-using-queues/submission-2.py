from collections import deque

class MyStack:

    def __init__(self):
        self.primary = deque()
        self.backup = deque()

    def push(self, x: int) -> None:
        self.primary.append(x)

    def pop(self) -> int:
        while len(self.primary) > 1:
            self.backup.append(self.primary.popleft())
        answer = self.primary.popleft()
        self.primary, self.backup = self.backup, self.primary
        return answer

    def top(self) -> int:
        while len(self.primary) > 1:
            self.backup.append(self.primary.popleft())
        answer = self.primary.popleft()
        self.backup.append(answer)
        self.primary, self.backup = self.backup, self.primary
        return answer
        

    def empty(self) -> bool:
        return not self.primary


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()