# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        

        #plan: store each node in a hash, if node is found again in hash return True else false

        nodes = set()

        cur = head

        while cur is not None:
            if cur in nodes:
                return True
            nodes.add(cur)
            cur = cur.next
        
        return False