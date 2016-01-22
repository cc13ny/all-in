class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        r2i = {'I':1, 'V':5, 'X':10, 'L':50, 
               'C':100, 'D':500, 'M':1000}

        res = 0
        for i in range(len(s)):
            if i == len(s) - 1 or r2i[s[i]] >= r2i[s[i + 1]]:
                res += r2i[s[i]]
            else:
                res -= r2i[s[i]]
        return res
