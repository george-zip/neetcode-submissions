# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        turtle = head
        rabbit = head
        while turtle and rabbit:
            turtle = turtle.next
            if rabbit.next:
                rabbit = rabbit.next.next
            else:
                return False
            if turtle == rabbit:
                return True
        return False