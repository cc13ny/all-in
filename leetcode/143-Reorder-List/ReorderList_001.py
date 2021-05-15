# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {void} Do not return anything, modify head in-place instead.
    def reorderList(self, head):

        a = []
        b = []
        p = head
        while p != None:
            a.append(p)
            p = p.next
        i = 0
        j = len(a) - 1
        size = len(a)
        while i < j:
            b.append(i)
            b.append(j)
            i = i + 1
            j = j - 1
        if i == j:
            b.append(i)
        for k in range(size):
            if k != size - 1:
                a[b[k]].next = a[b[k + 1]]
            else:
                a[b[k]].next = None
