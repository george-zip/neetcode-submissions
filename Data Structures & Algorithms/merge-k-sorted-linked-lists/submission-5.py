# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def merge_lists(list1, list2) -> List[ListNode]:
    new_head = ListNode()
    current = new_head
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    while list1:
        current.next = list1
        list1 = list1.next
        current = current.next
    while list2:
        current.next = list2
        list2 = list2.next
        current = current.next
    return new_head.next


class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        while len(lists) > 1:
            merged = []
            n = len(lists)
            for i in range(0, n, 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < n else None
                merged.append(merge_lists(l1, l2))
            lists = merged

        return lists[0]
