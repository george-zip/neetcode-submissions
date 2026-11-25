"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_new = {None: None}
        current = head
        while current:
            old_to_new[current] = Node(current.val)
            current = current.next
        for old, new in old_to_new.items():
            if old:
                new.next = old_to_new[old.next]
                new.random = old_to_new[old.random]
        return old_to_new[head]

