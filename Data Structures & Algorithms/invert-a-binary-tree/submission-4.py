# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def invert(node):
    if not node:
        return None
    return TreeNode(
        node.val,
        invert(node.right),
        invert(node.left)
    )

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return invert(root)