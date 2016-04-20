class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 4:
            return n - 1

        num3 = (n - 2) / 3
        rem = (n - 2) % 3
        return (3 ** num3) * (rem + 2)
