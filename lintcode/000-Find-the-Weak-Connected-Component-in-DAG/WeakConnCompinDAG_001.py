# Definition for a directed graph node
# class DirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
class Solution:
    # @param {DirectedGraphNode[]} nodes a array of directed graph node
    # @return {int[][]} a connected set of a directed graph
    def connectedSet2(self, nodes):
        # Write your code here
        fathers = {}
        for node in nodes:
            fathers[node.label] = node.label

        for node in nodes:
            for n in node.neighbors:
                fathers = self.union(node.label, n.label, fathers)

        res = {}
        for child in fathers:
            f = self.find(child, fathers)
            if f in res:
                res[f].add(child)
            else:
                res[f] = set([child])
        ans = []
        for i in res:
            tmp = list(res[i])
            tmp.sort()
            ans.append(tmp)
        return ans

    def find(self, label, fathers):
        if label != fathers[label]:
            return self.find(fathers[label], fathers)
        return label

    def union(self, label1, label2, fathers):
        f1, f2 = self.find(label1, fathers), self.find(label2, fathers)
        if f1 != f2:
            fathers[f2] = f1
        return fathers
