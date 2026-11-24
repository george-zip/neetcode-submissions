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

def reverse(head):
    previous, current = None, head
    while current:
        tmp = current.next
        current.next = previous
        previous = current
        current = tmp
    return previous

def print_null_safe(thing):
    if thing:
        print(thing.val)
    else:
        print("None")

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        n = get_list_len(head)
        if n == 1:
            return 
        current = head
        for _ in range(-(-n // 2)):
            current = current.next
        second_list = reverse(current)
        current = first_list = head
        first_list = first_list.next
        for i in range(1, n):
            if i % 2:
                current.next = second_list
                second_list = second_list.next
            else:
                current.next = first_list
                first_list = first_list.next
            current = current.next
        current.next = None

        