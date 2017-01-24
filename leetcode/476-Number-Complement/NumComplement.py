class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        res = 0
        i = 0
        while num:
            res += (1 - (num & 1)) << i
            num = num >> 1
            i += 1
        return res
