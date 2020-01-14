# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def isPalindrome(self, head):
        # Write your code here
        if head is None:
            return True
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        p = second
        print 'slow ' + str(slow.val)
        while p:
            print p.val
            p = p.next
            
        dumpy = ListNode(0)
        dumpy.next = head

        
        
        while head.next:
            if fast.next and head.next == second:
                head.next = None
                break
            if not fast.next and head.next == slow:
                head.next = None
                break
            tmp = head.next
            head.next = tmp.next
            tmp.next = dumpy.next
            dumpy.next = tmp
        
        first = dumpy.next

        p = first
        print
        while p:
            print p.val
            p = p.next
        
        
        while first and second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        return True