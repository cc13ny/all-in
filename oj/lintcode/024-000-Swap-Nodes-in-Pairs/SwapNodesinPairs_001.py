# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        # Write your code here
        dumpy = ListNode(0)
        dumpy.next = head
        pre = dumpy
        while pre.next is not None and pre.next.next is not None:
            fst = pre.next
            snd = pre.next.next
            pre.next = snd
            fst.next = snd.next
            snd.next = fst
            pre = fst
        return dumpy.next
