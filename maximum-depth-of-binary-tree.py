# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        l,r = 0, 0

        if root is None:
            return 0
        
        l += self.maxDepth(root.left) + 1
        r += self.maxDepth(root.right) + 1

        return max(l,r)