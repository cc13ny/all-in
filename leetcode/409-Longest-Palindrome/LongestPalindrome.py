class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = len(s)
        nletters = [0] * 52
        a = ord('a')
        has_odd = False
        
        for w in s:
            nletters[ord(w) - a] += 1
        for num in nletters:
            res -= 1 if num % 2 else 0
            has_odd = has_odd or (True if num % 2 else False)
        res += 1 if has_odd else 0
        return res
