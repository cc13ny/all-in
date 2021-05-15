"""
# One benefit to use dump is, you don't have to handle head == None specifically.

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        old_new_dict = {}

        p = head
        dump = Node(0)
        prev_new_p = dump

        while p:
            new_p = Node(p.val)
            new_p.random = p.random
            old_new_dict[p] = new_p

            prev_new_p.next = new_p

            p = p.next
            prev_new_p = new_p
        new_p = dump.next
        while new_p:
            if new_p.random:
                new_p.random = old_new_dict[new_p.random]
            new_p = new_p.next
        return dump.next
