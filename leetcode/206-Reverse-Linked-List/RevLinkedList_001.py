# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        a = []
        p = head
        while p != None:
            a.append(p)
            p = p.next
        if len(a) == 0:
            return None
            
        res = a[len(a) - 1]
        for i in range(len(a)):
            if i != len(a) - 1:
                a[len(a) - i - 1].next = a[len(a) - i - 2]
            else:
                a[0].next = None
        return res
