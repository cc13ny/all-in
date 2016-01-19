class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        mul = 1
        for i in range(len(s) - 1, -1, -1):
            res += (ord(s[i]) - ord('A') + 1) * mul
            mul *= 26
        return res
