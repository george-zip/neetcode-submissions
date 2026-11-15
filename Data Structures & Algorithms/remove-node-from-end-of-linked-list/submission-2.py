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
        if list_len == 1:
            return None
        if list_len == n:
            return head.next
        previous = current = head
        for _ in range(list_len - n):
            print(current.val)
            previous = current
            current = current.next
        previous.next = current.next
        return head