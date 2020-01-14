# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
# @param head, a ListNode
# @return a ListNode
    def insertionSortList(self, head):
        if not head:
            return head
        dummy = ListNode(0)                         
        dummy.next = head
        curr = head
        while curr.next:
            if curr.next.val < curr.val:            
                pre = dummy                         
                while pre.next.val < curr.next.val: 
                    pre = pre.next
                tmp = curr.next
                curr.next = tmp.next
                tmp.next = pre.next
                
                pre.next = tmp
            else:
                curr = curr.next
        return dummy.next
