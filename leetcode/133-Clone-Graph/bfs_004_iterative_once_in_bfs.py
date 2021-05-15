'''
Good Point:
    1. In one bfs

Bad Point:
    1. in fact the if-elses really took time. Don't do that
    2. not clear enough
'''


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=[]):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None

        root = node
        mapping = {}

        q = [node]
        while q:
            node = q.pop()
            if node not in mapping:
                mapping[node] = Node(node.val)

            new_node = mapping[node]
            for neighbor in node.neighbors:
                to_add = False
                if neighbor not in mapping:
                    mapping[neighbor] = Node(neighbor.val)
                    to_add = True
                new_node.neighbors.append(mapping[neighbor])

                if to_add:
                    q.append(neighbor)

        return mapping[root]
