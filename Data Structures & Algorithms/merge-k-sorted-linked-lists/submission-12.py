# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def merge_lists(l1, l2):
    new_head = ListNode()
    current = new_head
    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    while l1:
        current.next = l1
        l1 = l1.next
        current = current.next
    while l2:
        current.next = l2
        l2 = l2.next
        current = current.next
    return new_head.next


class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        while len(lists) > 1:
            merged = []
            n = len(lists)
            for i in range(0, n, 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < n else None
                merged.append(merge_lists(l1, l2))
                # print(merged)
            lists = merged
        return lists[0]
        