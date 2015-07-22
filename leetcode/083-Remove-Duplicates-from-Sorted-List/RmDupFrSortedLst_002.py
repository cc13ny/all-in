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
        pre = ListNode(0)
        dumpy = pre
        pre.next = head
        p = head
        while p != None:
            
            if p.val not in dic:
                dic[p.val] = 1
                pre = pre.next
            else:
                pre.next = p.next
                
                
            p = p.next
        return dumpy.next
