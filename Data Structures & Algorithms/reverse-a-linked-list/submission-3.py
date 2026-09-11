# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_node(previous, current) -> Optional[ListNode]:
            if not current:
                return previous
            next_node = current.next
            current.next = previous
            return reverse_node(current, next_node)
        return reverse_node(None, head)