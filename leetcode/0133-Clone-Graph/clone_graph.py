"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

"""
Solution 1: iter, bfs, queue, node first edge later
"""


class Solution1:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None

        root = node
        old_to_new_map = {}

        queue = [root]

        while queue:
            node = queue.pop(0)
            old_to_new_map[node] = Node(node.val)
            for neighbor in node.neighbors:
                if neighbor not in old_to_new_map:
                    queue.append(neighbor)

        for old_node, new_node in old_to_new_map.items():
            new_node.neighbors = [old_to_new_map[neighbor] for neighbor in old_node.neighbors]

        return old_to_new_map[node]


"""
Solution 2: recu, dfs, node followed by edge
"""


class Solution2:
    def cloneGraph(self, node: 'Node') -> 'Node':

        def cloneG(graph_node, vstd):
            if graph_node is None:
                return None

            if graph_node.val in vstd:
                return visited[graph_node.val]

            new_node = Node(graph_node.val)
            vstd[graph_node.val] = new_node

            for neighbor in graph_node.neighbors:
                new_neighbor = cloneG(neighbor, vstd)
                new_node.neighbors.append(new_neighbor)

            return new_node

        visited = {}

        return cloneG(node, visited)
