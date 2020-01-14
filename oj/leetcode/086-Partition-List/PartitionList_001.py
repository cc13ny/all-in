#@author: cchen

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} x
    # @return {ListNode}
    def partition(self, head, x):
        if head == None or head.next == None:
            return head
        dump = ListNode(0)
        dump.next = head
        p = dump
        
        dump1 = ListNode(0)
        q = dump1
        while p.next != None:
            if p.next.val < x:
                p = p.next
            else:
                q.next = p.next
                q = q.next
                p.next = p.next.next
        
        q.next = None
        p.next = dump1.next
        return dump.next
