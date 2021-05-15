class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) > len(t):
            return False

        if s == '':
            return True

        i = 0
        n = len(s)
        for c in t:
            if c == s[i]:
                i += 1
                if i == n:
                    return True
        return False
