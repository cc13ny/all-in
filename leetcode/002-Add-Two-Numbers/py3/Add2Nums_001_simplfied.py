'''
  Inspired by https://leetcode.com/articles/add-two-numbers/
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        dummy = ListNode(0);
        p = dummy
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            p.next = ListNode((x + y + carry) % 10)
            carry = (x + y + carry) / 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            p = p.next

        if carry == 1: p.next = ListNode(1)
        return dummy.next
