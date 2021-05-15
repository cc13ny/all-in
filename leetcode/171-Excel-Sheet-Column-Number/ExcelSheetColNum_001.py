class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in range(len(s) - 1, -1, -1):
            res += (ord(s[i]) - ord('A') + 1) * 26 ** (len(s) - 1 - i)

        return res
