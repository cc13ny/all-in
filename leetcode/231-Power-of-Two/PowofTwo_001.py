class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        if n < 1:
            return False

        while n != 1:
            after = n >> 1
            new = after << 1
            if new != n:
                return False
            else:
                n = after

        return True
