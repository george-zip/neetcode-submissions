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

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        list_len = get_list_len(head)
        if list_len == n:
            return head.next
        current = head
        for _ in range(list_len - n - 1):
            current = current.next
        current.next = current.next.next
        return head