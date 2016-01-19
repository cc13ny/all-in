# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            tmp = fast.next
            fast.next = tmp.next
            fast = fast.next 
            tmp.next = slow.next
            slow.next = tmp
            slow = tmp
        return head
