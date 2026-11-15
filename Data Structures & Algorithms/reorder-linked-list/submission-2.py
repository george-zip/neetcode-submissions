# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def get_list_len(head):
    answer = 0
    while head:
        answer += 1
        head = head.next
    return answer

def reverse_linked_list(previous, current):
    if not current:
        return previous
    tmp = current.next
    current.next = previous
    previous = current
    current = tmp
    return reverse_linked_list(previous, current)

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        list_len = get_list_len(head)
        list_b = head
        previous = None
        for _ in range(-(-list_len // 2)):
            previous = list_b
            list_b = list_b.next
        previous.next = None
        list_b = reverse_linked_list(None, list_b)
        combined = head
        list_a = head.next
        for i in range(1, list_len):
            if i % 2:
                combined.next = list_b
                list_b = list_b.next 
                combined = combined.next
            else:
                combined.next = list_a
                list_a = list_a.next
                combined = combined.next 
