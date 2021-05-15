# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq


class Solution:
    # @param {ListNode[]} lists
    # @return {ListNode}
    def mergeKLists(self, lists):
        hq = []
        for ls in lists:
            if ls:
                heapq.heappush(hq, (ls.val, ls))
        dump = ListNode(0)
        p = dump
        while hq:
            _, minnode = heapq.heappop(hq)
            nextnode = minnode.next
            if nextnode:
                heapq.heappush(hq, (nextnode.val, nextnode))
            p.next = minnode
            p = p.next

        return dump.next
