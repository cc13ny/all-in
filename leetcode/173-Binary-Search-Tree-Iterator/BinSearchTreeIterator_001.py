# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.curt = root
        self.stack = []

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return self.curt or len(self.stack) != 0

    # @return an integer, the next smallest number
    def next(self):
        curt = self.curt
        stack = self.stack
        while curt:
            stack.append(curt)
            curt = curt.left
        curt = stack.pop()
        self.curt = curt.right
        return curt.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
