# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        if not head.next:
            return False
        hare = head.next 
        tortoise = head
        while hare and hare.next:
            if hare == tortoise:
                return True
            hare = hare.next.next if hare.next.next else hare.next
            tortoise = tortoise.next
        return False