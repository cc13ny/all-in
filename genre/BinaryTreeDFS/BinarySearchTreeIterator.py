"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = Solution(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node 
"""


class Solution:
    # @param root: The root of binary tree.
    def __init__(self, root):
        # write your code here
        self.stack = []
        self.curt = root

    # @return: True if there has next node, or false
    def hasNext(self):
        # write your code here
        return len(self.stack) != 0 or self.curt


    # @return: return next node
    def next(self):
        # write your code here
        stack = self.stack
        curt = self.curt
        while curt:
            stack.append(curt)
            curt = curt.left
        curt = stack.pop()
        self.curt = curt.right
        return curt
