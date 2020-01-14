class Solution:
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
        left, right = 0, x / 2 + 1
        while left <= right:
            m = (left + right) / 2
            sq = m * m
            if sq == x:
                return m
            elif sq < x:
                left = m + 1
            else:
                right = m - 1
        return right
