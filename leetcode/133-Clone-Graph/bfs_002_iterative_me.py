"""
Key Points:
    mapping -> old node to new node (instead of val to new node)

Good Points:
    1. mapping is filled with BFS

Bad Points:
    1. I think I should separate BFS as a module/method?
    2. use q = [] instead of collections.deque
"""

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None

        root = node
        mapping = {}

        q = [root]
        while len(q) > 0:
            node = q.pop()
            mapping[node] = Node(node.val)
            for neighbor in node.neighbors:
                if neighbor not in mapping:
                    mapping[neighbor] = Node(neighbor.val)
                    q.append(neighbor)

        for node in mapping:
            new_node = mapping[node]
            for neighbor in node.neighbors:
                new_node.neighbors.append(mapping[neighbor])

        return mapping[root]