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
            while (l is not None) and (r is not None):
                ltree_rmost = l
                while ltree_rmost.next is not None:
                    ltree_rmost = ltree_rmost.next
               
                while (l.left is None) and (l.right is None) and (l.next is not None):
                    l = l.next
                l = l.left if l.left is not None else l.right
                
                ltree_rmost.next = r
                
                while (r.left is None) and (r.right is None) and (r.next is not None):
                    r = r.next
                r = r.left if r.left is not None else r.right
