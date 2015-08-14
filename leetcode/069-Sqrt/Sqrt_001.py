# What's the problem of Newton's method

class Solution:
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
        if x == 0:
            return 0;
        res, pre = 1.0, 0;
        while res != pre:
            pre = res
            res = (res + x / res) / 2
        return int(res)
