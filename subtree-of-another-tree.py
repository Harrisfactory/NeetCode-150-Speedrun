# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        #plan: if we hit a node, we fire off sameTree and attempt to match
            #otherwise we continue traversing,
            #if we reach the end of main tree and no sameTree returns true then we return false in our traversal
            #implement basic preorder traversal
            if root:
                
                if root.val == subRoot.val:
                    if self.sameTree(root, subRoot):
                        return True
                
                return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    
    def sameTree(self, treeOne, treeTwo):

        #check if both are empty
        if treeOne is None and treeTwo is None:
            return True
        #otherwise check if one is empty
        if treeOne is None or treeTwo is None:
            return False
        #otherwise check against vals and continue
        if treeOne.val != treeTwo.val:
            return False
        return self.sameTree(treeOne.left, treeTwo.left) and self.sameTree(treeOne.right, treeTwo.right)
    

    #O(h + s^h)