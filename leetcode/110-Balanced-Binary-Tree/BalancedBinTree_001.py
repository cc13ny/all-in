class Solution:
    # @param root, a tree node
    # @return a boolean
    def Height(self, root):
        if root == None:
            return 0
        return max(self.Height(root.left), self.Height(root.right)) + 1

    def isBalanced(self, root):
        if root == None:
            return True
        if abs(self.Height(root.left) - self.Height(root.right)) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False
