# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head == None: return None
        dic = {}
        p = head
        while p != None:
            
            if p.val not in dic:
                dic[p.val] = 1
            else:
                dic[p.val] += 1
                
            p = p.next
                
        dumpy = ListNode(0)
        dumpy.next = head
        pre = dumpy
        p = head
        
        while p != None:
           
            if dic[p.val] != 1:
                
                pre.next = p.next
                dic[p.val] -= 1
            else:
                pre = p
          
            p = p.next
            
        return dumpy.next
