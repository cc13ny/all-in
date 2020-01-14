class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = ''
        tc = 0
        for i in range(max(len(a), len(b))):
            ta = int(a[-i - 1]) if i < len(a) else 0
            tb = int(b[-i - 1]) if i < len(b) else 0
            res = str((ta + tb + tc) % 2) + res
            tc = (ta + tb + tc) / 2
        if tc:
            res = '1' + res
        return res
