class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        diff = [0] * 26
        for w in s:
            diff[ord(w) - 97] += 1
        for w in t:
            diff[ord(w) - 97] -= 1
            
        for i in xrange(26):
            if diff[i] < 0:
                return chr(i + 97)
