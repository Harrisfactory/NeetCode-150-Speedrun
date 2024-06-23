# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        new_head = ListNode()
        remember_head = new_head

        if list1 is None and list2 is None:
            return

        while list1 or list2:

            while list1 and list2:
                if list1.val < list2.val:
                    new_head.val = list1.val
                    list1 = list1.next
                elif list1.val > list2.val:
                    new_head.val = list2.val
                    list2 = list2.next
                else:
                    new_head.val = list1.val
                    list1 = list1.next
                if list1 is not None or list2 is not None:
                    new_head.next = ListNode()
                    new_head = new_head.next
            
            while list1 and not list2:
                new_head.val = list1.val
                list1 = list1.next
                if list1 is not None:
                    new_head.next = ListNode()
                    new_head = new_head.next
            
            while list2 and not list1:
                new_head.val = list2.val
                list2 = list2.next
                if list2 is not None:
                    new_head.next = ListNode()
                    new_head = new_head.next
            

        return remember_head

        #O(n + M)