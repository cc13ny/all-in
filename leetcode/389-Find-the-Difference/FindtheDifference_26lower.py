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
            i = ord(w) - 97
            diff[i] -= 1
            if diff[i] < 0:
                return w
