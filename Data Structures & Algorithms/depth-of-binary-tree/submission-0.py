# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def max_depth(root) -> int:
    if not root:
        return 0
    return max(
        1 + max_depth(root.left),
        1 + max_depth(root.right)
    )

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return max_depth(root)