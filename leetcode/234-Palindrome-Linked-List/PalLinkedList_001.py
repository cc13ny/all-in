'''
  based on solution 1 of the link: http://www.cnblogs.com/grandyang/p/4635425.html
  O(n) time, O(n) space
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
        stack = [head.val]
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            stack.append(slow.val)
        
        if not fast.next: stack.pop()
        
        while slow.next:
            slow = slow.next
            top = stack.pop()
            if top != slow.val: # it can't pass if 'top is not slow.val'
                return False
        
        return True
