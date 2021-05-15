# @author: cchen

class Solution:
    # @param {integer} x
    # @return {integer}

    def isoverflow(self, s):
        m = str(2 ** 31 - 1)
        if len(s) > len(m):
            return True
        if len(s) < len(m):
            return False
        if s > m:
            return True
        return False

    def reverse(self, x):
        t = x if x > -1 else -x
        s = str(t)
        s = s[::-1]
        res = 0 if self.isoverflow(s) else int(s)
        res = res if x > -1 else -res

        return res
