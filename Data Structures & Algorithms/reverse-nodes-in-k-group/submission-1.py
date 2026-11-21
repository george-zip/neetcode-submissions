# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverse_k_nodes(l, k):
    # reverse k nodes and return
    # head of new list, the tail 
    # and next node after list
    tail, current, previous = l, l, None
    while current and k > 0:
        tmp = current.next
        current.next = previous
        previous = current
        current = tmp
        k -= 1
    return previous, tail, current

def get_list_len(l):
    answer = 0
    while l:
        answer += 1
        l = l.next
    return answer

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        sub_lists = []
        n = get_list_len(head)
        current = head
        for _ in range(n // k):
            sl_head, sl_tail, current = reverse_k_nodes(current, k)
            # print(sl_head.val, sl_tail.val, current)
            sub_lists.append((sl_head, sl_tail))
        # print(sub_lists)
        if current:
            sub_lists.append((current, None))
        for i in range(1, len(sub_lists)):
            sub_lists[i - 1][1].next = sub_lists[i][0]
        return sub_lists[0][0]