# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        stack = []
        p = head
        while p:
            stack.append(p)
            p = p.next
            
        dummy = ListNode(0)
        p = dummy
        while stack:
            p.next = stack.pop()
            p = p.next
        p.next = None
        return dummy.next
