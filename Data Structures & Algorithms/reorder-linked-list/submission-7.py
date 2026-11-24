# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def list_len(head):
    answer = 0
    while head:
        answer += 1
        head = head.next
    return answer

def reverse_list(head):
    current, previous = head, None
    while current:
        tmp = current.next
        current.next = previous
        previous = current
        current = tmp
    return previous

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        n = list_len(head)
        if n == 1:
            return
        current = head
        for _ in range(-(-n // 2)):
            current = current.next
        second_half = reverse_list(current)
        first_half = current = head
        first_half = first_half.next
        for i in range(1, n):
            if i % 2:
                current.next = second_half
                second_half = second_half.next
            else:
                current.next = first_half
                first_half = first_half.next
            current = current.next
        current.next = None