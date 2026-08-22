class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:
    def __init__(self):
        self.head = ListNode(0)
        self.size = 0


    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        current = self.head.next
        for _ in range(index):
            current = current.next
        return current.val


    def addAtHead(self, val: int) -> None:
        node = ListNode(val, self.head.next)
        self.head.next = node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        node = ListNode(val)
        current = self.head
        while current.next:
            current = current.next
        current.next = node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        current = self.head
        for _ in range(index):
            current = current.next
        node = ListNode(val)
        node.next = current.next
        current.next = node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        current = self.head
        for _ in range(index):
            current = current.next
        current.next = current.next.next
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
