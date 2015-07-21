# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        
        dumpy = ListNode(0)
        p1 = l1
        p2 = l2
        p = dumpy
        
        if p1 == None:
            return p2
        if p2 == None:
            return p1
        while p1 != None and p2 != None:
            if p1.val < p2.val:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
            p = p.next
        if p1 == None:
            p.next = p2
        else:
            p.next = p1
        
        return dumpy.next
