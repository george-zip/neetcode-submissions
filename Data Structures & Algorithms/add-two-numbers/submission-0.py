# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        sum_ll_head = ListNode()
        sum_ll = sum_ll_head
        while l1 and l2:
            total = l1.val + l2.val + carry 
            carry = total // 10 if total >= 10 else 0
            sum_ll.next = ListNode(total % 10)
            sum_ll = sum_ll.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            total = l1.val + carry
            sum_ll.next = ListNode(total % 10)
            carry = total // 10 if total >= 10 else 0
            sum_ll = sum_ll.next
            l1 = l1.next
        while l2:
            total = l2.val + carry
            sum_ll.next = ListNode(total % 10)
            carry = total // 10 if total >= 10 else 0
            sum_ll = sum_ll.next
            l2 = l2.next
        if carry:
            sum_ll.next = ListNode(carry)
        return sum_ll_head.next
