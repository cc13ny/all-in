# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def rotateRight(self, head, k):
        if head == None or head.next == None or k == 0:
            return head
        
        p = head
        q = None
        cnt = 0
        while p != None:
            cnt += 1
            if p.next == None:
                q = p
            p = p.next
        
        k = k % cnt
        
        if k == 0:
            return head
        
        p = head
        for i in range(cnt - k - 1):
            p = p.next
        res = p.next
        p.next = None
        q.next = head
        
        return res
