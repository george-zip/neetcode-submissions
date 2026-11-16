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
        if not head:
            return None
        nodes = {}
        new_ll = Node(-1)
        new_head = new_ll
        current = head
        while current:
            node = Node(
                current.val,
                None,
                None
            )
            if id(current.random) in nodes:
                node.random = nodes[id(current.random)]
            elif current.random is not None:
                node.random_node_id = id(current.random)
            nodes[id(current)] = node
            new_ll.next = node
            new_ll = new_ll.next
            current = current.next
        current = new_head
        while current:
            if hasattr(current, "random_node_id"):
                current.random = nodes[current.random_node_id]    
            current = current.next
        return new_head.next
