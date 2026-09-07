class ListNode:

    __slots__ = ("url", "prev", "next")

    def __init__(self, url, prev=None, next=None):
        self.url = url
        self.next = next
        self.prev = prev


class BrowserHistory:
    def __init__(self, homepage: str):
        self.head = ListNode(homepage)
        self.current = self.head

    def visit(self, url: str) -> None:
        node = ListNode(url, prev=self.current)
        self.current.next = node
        self.current = node

    def back(self, steps: int) -> str:
        while self.current.prev and steps:
            self.current = self.current.prev
            steps -= 1
        return self.current.url

    def forward(self, steps: int) -> str:
        while self.current.next and steps:
            self.current = self.current.next
            steps -= 1
        return self.current.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
