# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        #using a arr so I don't have to worry about passing around an integer recursivly
        good_node_count = [0]

        def dfs(root, maxVal):
            #base case, do we have a root?
            if root is None:
                return 0
            #check to see if we have a good val
            if root.val >= maxVal:
                good_node_count[0]+=1
                maxVal = root.val
            #traverse left and right
            dfs(root.left, maxVal)
            dfs(root.right, maxVal)
        dfs(root, root.val)
        
        return good_node_count[0]
        
        #O(h)