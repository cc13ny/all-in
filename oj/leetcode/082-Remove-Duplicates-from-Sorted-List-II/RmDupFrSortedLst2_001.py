# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        if head == None:
            return None
        t = {}
        p = head
        while p != None:
            if p.val not in t:
                t[p.val] = False
            else:
                t[p.val] = True
            p = p.next
        dump = ListNode(0)
        dump.next = head
        p = dump
        while p.next != None:
            if t[p.next.val]:
                p.next = p.next.next
            else:
                p = p.next
        return dump.next
