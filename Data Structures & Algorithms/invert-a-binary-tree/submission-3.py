# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return None

        node_stack = [root]
        while node_stack:
            node = node_stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                node_stack.append(node.left)
                node_stack.append(node.right)

        return root