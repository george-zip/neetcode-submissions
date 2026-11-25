# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverse_list(previous, current):
    if not current:
        return previous
    tmp = current.next
    current.next = previous
    return reverse_list(current, tmp)

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None     
        return reverse_list(None, head)   