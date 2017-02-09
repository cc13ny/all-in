# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def treeSum(node, freq):
            if not node:
                return 0, freq
            lsum, freq = treeSum(node.left, freq)
            rsum, freq = treeSum(node.right, freq)
            nsum = node.val + lsum + rsum
            freq[nsum] = freq.get(nsum, 0) + 1
            return nsum, freq
            
        nsum, freq = treeSum(root, {})
        max_val = max([freq[k] for k in freq]) if freq else 0
        res = []
        for k in freq:
            if freq[k] == max_val:
                res.append(k)
        return res
