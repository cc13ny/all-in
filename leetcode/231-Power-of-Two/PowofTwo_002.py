class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        res = 0
        while n > 0:
            res += n & 1
            n = n >> 1

        return res == 1
