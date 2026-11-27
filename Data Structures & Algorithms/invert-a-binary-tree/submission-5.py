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
        nodes = [root]
        while nodes:
            node = nodes.pop()
            if node:
                r, l = node.right, node.left
                node.left = r
                node.right = l
                nodes.append(r)
                nodes.append(l)
        return root