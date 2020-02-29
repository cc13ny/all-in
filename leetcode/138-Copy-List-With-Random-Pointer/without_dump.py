"""
# Be careful about when head is None

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None

        old_to_new = {}
        node = head
        while node:
            n_node = Node(node.val, node.next, node.random)
            old_to_new[node] = n_node
            node = node.next

        node = head
        while node:
            n_node = old_to_new[node]
            if n_node.random:
                n_node.random = old_to_new[n_node.random]
            if n_node.next:
                n_node.next = old_to_new[n_node.next]
            node = node.next

        return old_to_new[head]