class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        diff = {}
        for w in s:
            diff[w] = diff.get(w, 0) + 1
        for w in t:
            if diff.get(w, 0) == 0:
                return w
            diff[w] -= 1
