# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        new_head = None
        current = ListNode()
        while list1 and list2:
            if list1.val <= list2.val:
                tmp = list1
                list1 = list1.next
                current.next = tmp
            else:
                tmp = list2
                list2 = list2.next
                current.next = tmp
            if new_head is None:
                new_head = current.next
            current = current.next
        while list1:
            tmp = list1
            list1 = list1.next
            current.next = tmp
            if new_head is None:
                new_head = current.next
            current = current.next
        while list2:
            tmp = list2
            list2 = list2.next
            current.next = tmp
            if new_head is None:
                new_head = current.next
            current = current.next
        return new_head
