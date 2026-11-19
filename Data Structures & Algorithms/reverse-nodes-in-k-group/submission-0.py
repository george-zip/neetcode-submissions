def reverse_k_nodes(head: ListNode, k: int) -> tuple[ListNode, ListNode, ListNode]:
    current = tail = head
    previous = None
    for _ in range(k):
        tmp = current.next
        current.next = previous
        previous = current
        current = tmp
    return previous, tail, current

def get_list_len(head) -> int:
    answer: int = 0
    while head:
        head = head.next
        answer += 1
    return answer

def advance_k(head, k):
    while k and head.next:
        head = head.next
        k -= 1
    return head

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        list_len = get_list_len(head)
        if list_len == 1:
            return head
        sub_lists = []
        current = head
        for i in range(list_len // k):
            next_head, tail, current = reverse_k_nodes(current, k)
            sub_lists.append((next_head, tail))
        if current:
            sub_lists.append((current, None))
        new_head, prev_tail = sub_lists[0][0], None
        for h, t in sub_lists:
            if prev_tail:
                prev_tail.next = h
            prev_tail = t
        return new_head
