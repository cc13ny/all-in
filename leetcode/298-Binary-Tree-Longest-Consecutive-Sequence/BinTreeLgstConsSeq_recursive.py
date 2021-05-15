# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def func(node, p_val, p_maxlen, res):
            if not node:
                return res
            n_maxlen = p_maxlen + 1 if node.val == p_val + 1 else 1
            res = max(res, n_maxlen)
            res = func(node.left, node.val, n_maxlen, res)
            res = func(node.right, node.val, n_maxlen, res)
            return res

        root_val = root.val if root else 0
        return func(root, root_val, 0, 0)
