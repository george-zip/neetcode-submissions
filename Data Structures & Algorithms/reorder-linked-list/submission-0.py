class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        node_stack = []
        current = head
        while current:
            node_stack.append(current)
            current = current.next
        old_list_ref = head
        new_list_ref = head
        n = len(node_stack) 
        for i in range(1, n):
            tmp = old_list_ref.next
            if i % 2:
                node = node_stack.pop()
                new_list_ref.next = node
                new_list_ref = new_list_ref.next
                old_list_ref = tmp if i == 1 else old_list_ref
            else:
                new_list_ref.next = old_list_ref
                new_list_ref = new_list_ref.next
                old_list_ref = tmp
        new_list_ref.next = None
