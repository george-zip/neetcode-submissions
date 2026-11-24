# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def create_node(val):
    return ListNode(
        val % 10
    ), val // 10

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        current = new_head = ListNode()
        while l1 and l2:
            val = l1.val + l2.val + carry
            # print(f"{val=}")
            current.next, carry = create_node(val)
            # print(f"{current.val=},{carry=}")
            l1 = l1.next
            l2 = l2.next
            current = current.next
        while l1:
            current.next, carry = create_node(l1.val + carry)
            l1 = l1.next
            current = current.next
        while l2:
            current.next, carry = create_node(l2.val + carry)
            l2 = l2.next
            current = current.next
        if carry:
            current.next, _ = create_node(carry)
        return new_head.next
