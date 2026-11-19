# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def from_linked_list(list: Optional[ListNode]):
    answer = []
    while list:
        answer.append(list.val)
        list = list.next
    return answer

def get_list_len(head):
    answer = 0
    while head:
        head = head.next
        answer += 1
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
        list_len = get_list_len(head)
        if list_len == 1:
            return 
        second_list_start = head
        for _ in range(-(-list_len // 2)):
            second_list_start = second_list_start.next
        second_list_start = reverse_list(second_list_start)
        current = first_list_start = head
        first_list_start = first_list_start.next
        # print(from_linked_list(second_list_start))
        for i in range(1, list_len):
            print(i, current.val)
            if i % 2:
                current.next = second_list_start
                # print(f"{second_list_start.val=}")
                second_list_start = second_list_start.next
            else:
                current.next = first_list_start
                first_list_start = first_list_start.next
            current = current.next
        current.next = None
        # print(from_linked_list(head))
