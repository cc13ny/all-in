"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: Level order in a list of lists of integers
    """
    def levelOrder(self, root):
        # write your code here
        if root is None:
            return []

        res, q_lvl = [], [root]
        while q_lvl != []:
            pre, tmp = [], []
            for node in q_lvl:
                pre.append(node.val)
                l, r = node.left, node.right
                if l:
                    tmp.append(l)
                if r:
                    tmp.append(r)
            res.append(pre)
            q_lvl = tmp
        return res
