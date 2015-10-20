# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if root is not None:
            l, r = root.left, root.right
            self.connect(l)
            self.connect(r)
            while l is not None:
                l.next = r
                l = l.right
                r = r.left
