class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ''
        base = ord('A') - 1
        while n > 0:
            rem = n % 26
            rem = 26 if rem == 0 else rem
            res = chr(rem + base) + res
            n = (n - rem) / 26
        return res
