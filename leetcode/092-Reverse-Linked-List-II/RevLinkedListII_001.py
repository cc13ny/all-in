# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param {ListNode} head
    # @param {integer} m
    # @param {integer} n
    # @return {ListNode}
    def reverseBetween(self, head, m, n):
        dumpy = ListNode(0)
        dumpy.next = head
        pre = dumpy

        diff = n - m

        while m > 1:
            pre = pre.next
            m -= 1
        p = pre.next
        while diff > 0 and p and p.next:
            # print p.val
            diff -= 1
            tmp = p.next
            p.next = tmp.next
            q = pre.next
            pre.next = tmp
            tmp.next = q
        return dumpy.next
