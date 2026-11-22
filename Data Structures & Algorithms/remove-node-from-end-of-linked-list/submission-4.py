# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def get_list_size(head):
    answer = 0
    while head:
        answer += 1
        head = head.next
    return answer


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        list_size = get_list_size(head)
        if list_size == 1:
            return None
        elif list_size == n:
            return head.next
        current, previous = head, None
        for _ in range(list_size - n):
            previous = current
            current = current.next
        print(previous.val)
        previous.next = current.next
        return head