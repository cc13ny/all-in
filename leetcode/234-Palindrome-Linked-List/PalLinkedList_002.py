'''
  based on solution 2 of the link: http://www.cnblogs.com/grandyang/p/4635425.html
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        if not head or not head.next:
            return True
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        last = slow.next
        while last.next:
            tmp = last.next
            last.next = tmp.next
            tmp.next = slow.next
            slow.next = tmp

        pre = head
        while slow.next:
            slow = slow.next
            if slow.val != pre.val:
                return False
            pre = pre.next

        return True
