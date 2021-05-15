# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def leftMost(node, r_ancestor):
            if not node:
                return None

            r_min = leftMost(node.right, r_ancestor)
            if r_min:
                node.val += r_min.val
            elif r_ancestor:
                node.val += r_ancestor.val

            l_min = leftMost(node.left, node)
            return l_min if node.left else node

        leftMost(root, None)
        return root
