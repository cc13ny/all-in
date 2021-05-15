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

        # Step 1: bfs traverse the graph, and create the mapping between old nodes and new nodes
        self.bfs(root, mapping)

        # Step 2: create neighbors for copied node
        for node in mapping:
            new_node = mapping[node]
            for neighbor in node.neighbors:
                new_node.neighbors.append(mapping[neighbor])

        return mapping[root]

    def bfs(self, root, mapping):
        q = collections.deque([root])
        while q:
            node = q.popleft()
            mapping[node] = Node(node.val)
            for neighbor in node.neighbors:
                if neighbor not in mapping:
                    q.append(neighbor)
