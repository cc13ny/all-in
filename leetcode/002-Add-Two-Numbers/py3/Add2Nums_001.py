# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param l1: the first list
    # @param l2: the second list
    # @return: the sum list of l1 and l2 
    def addLists(self, l1, l2):
        # write your code here
        if l1 == None: return l2
        if l2 == None: return l1
        flag = 0
        dummy = ListNode(0);
        p = dummy
        while l1 and l2:
            p.next = ListNode((l1.val + l2.val + flag) % 10)
            flag = (l1.val + l2.val + flag) / 10
            l1 = l1.next;
            l2 = l2.next;
            p = p.next
        while l2:
            p.next = ListNode((l2.val + flag) % 10)
            flag = (l2.val + flag) / 10
            l2 = l2.next;
            p = p.next
        while l1:
            p.next = ListNode((l1.val + flag) % 10)
            flag = (l1.val + flag) / 10
            l1 = l1.next;
            p = p.next

        if flag == 1: p.next = ListNode(1)
        return dummy.next
