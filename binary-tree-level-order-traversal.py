# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #level order traversal algorithm:
            #0: check if root even exists
            if root is None:
                return []
            #1: store root in a queue, this is the top level
            queue = [root]
            result = []
            #2: in outer loop, while the queue is not empty, get the length of current queue to traverse in inner loop
            while len(queue) > 0:
                queue_len = len(queue)
                level = []
                #3: in inner loop, iterate through the queues current layer
                for i in range(queue_len):
                    #getting the leftmost node out of the queue
                    node = queue.pop(0)
                    #append the nodes value to the current level
                    level.append(node.val)
                    #add its children to the queue
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                #add the current level to our result level order traversal
                result.append(level)
            return result