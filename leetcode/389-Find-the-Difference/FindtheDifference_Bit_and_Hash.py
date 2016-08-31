class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        chrs = {}
        res = 0
        for w in t:
            if w not in chrs:
                chrs[w] = 1 << (ord(w) - 97)
            res += chrs[w]
        for w in s:
            res -= chrs[w]
        return chr(len(bin(res)) + 94)
