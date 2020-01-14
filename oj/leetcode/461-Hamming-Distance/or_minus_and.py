class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        res = 0
        for i in bin(x|y):
            if i == '1':
                res += 1
        for i in bin(x&y):
            if i == '1':
                res -= 1
        return res
