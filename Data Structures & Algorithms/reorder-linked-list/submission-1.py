def get_list_len(head):
    n = 0
    while head:
        n += 1
        head = head.next
    return n

def reverse_ll(head):
    previous = None
    while head:
        tmp = head.next
        head.next = previous
        previous = head
        head = tmp
    return previous
        
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        list_len = get_list_len(head)
        if list_len == 1:
            return
        other_half = head
        first_half = head
        previous = None
        for _ in range(-(-list_len // 2)):
            previous = other_half
            other_half = other_half.next
        previous.next = None
        other_half = reverse_ll(other_half)
        new_head = first_half
        first_half = first_half.next 
        for i in range(1, list_len):
            if i % 2:
                new_head.next = other_half
                other_half = other_half.next
                new_head = new_head.next 
            else:
                new_head.next = first_half 
                first_half = first_half.next 
                new_head = new_head.next
