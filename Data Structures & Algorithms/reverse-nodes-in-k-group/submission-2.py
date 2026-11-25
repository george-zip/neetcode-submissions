# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def list_len(head):
    answer = 0
    while head:
        answer += 1
        head = head.next
    return answer

def reverse_k_nodes(head, k):
    current, previous = head, None
    for _ in range(k):
        tmp = current.next
        current.next = previous
        previous = current
        current = tmp
    return previous, current

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = list_len(head) 
        if n == 1:
            return head
        node_groups = []
        current = head
        for _ in range(n // k):
            node_group_tail = current
            node_group_head, current = reverse_k_nodes(current, k)
            node_groups.append((node_group_head, node_group_tail))
        if current:
            node_groups.append((current, None))
        for i in range(len(node_groups) - 1):
            node_groups[i][1].next = node_groups[i + 1][0]
        return node_groups[0][0]
