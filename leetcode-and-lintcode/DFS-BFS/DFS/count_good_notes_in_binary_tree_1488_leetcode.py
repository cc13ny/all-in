# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class SolutionRecursive:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            if not node:
                return 0

            res = 1 if node.val >= max_val else 0
            max_val = max(max_val, node.val)

            res += dfs(node.left, max_val) + dfs(node.right, max_val)

            return res

        return 1 + dfs(root.left, root.val) + dfs(root.right, root.val)


'''
Recursive, there're two ways to count for the result. When appending/ popping. 
Usually there's no difference, and popping will make code clearer 
while something is needed to be done when appending (like visited).
'''


class SolutionInterative:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        res = 0
        stack = [(root, root.val)]

        while stack:
            node, max_val = stack.pop()
            res += 1 if node.val >= max_val else 0
            max_val = max(max_val, node.val)
            if node.left:
                stack.append((node.left, max_val))
            if node.right:
                stack.append((node.right, max_val))
        return res