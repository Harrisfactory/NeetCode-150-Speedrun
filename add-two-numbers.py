# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        #going to prepend each num in each list to avoid having to reverse list

        #then conv list to int then execute sum then reverse loop to place it back into a list

        l1_list = []
        l1_num = ""

        l2_list = []
        l2_num = ""

        fin_list = ListNode()

        while l1:
            l1_list.insert(0, l1.val)
            l1 = l1.next
        while l2:
            l2_list.insert(0, l2.val)
            l2 = l2.next
        
        #convert list to str then to int
        for num in l1_list:
            l1_num += str(num)
        for num in l2_list:
            l2_num += str(num)
        
        fin_num = str(int(l1_num) + int(l2_num))
        head_fin_list = fin_list
        for i in reversed(range(len(fin_num))):
            print(fin_num[i])
            fin_list.val = fin_num[i]
            if i > 0:
                fin_list.next = ListNode()
                fin_list = fin_list.next
        
        return head_fin_list