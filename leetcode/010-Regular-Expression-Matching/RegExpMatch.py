class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        n_s = len(s)
        n_star = 0

        seg = []
        i = len(p) - 1
        while i > -1:
            if p[i] == '*':
                n_star += 1
                seg.insert(0, p[i - 1:i + 1])
                i -= 2
            else:
                seg.insert(0, p[i])
                i -= 1

        n_p = len(p) - n_star
        m, n = n_p + 1, n_s + 1

        dp = [[False for j in xrange(n)] for i in xrange(m)]
        dp[0][0] = True

        for i in xrange(1, m):
            if len(seg[i - 1]) == 2:
                dp[i][0] = True
            else:
                break

        for i in xrange(1, m):
            for j in xrange(1, n):
                if dp[i][j - 1] and len(seg[i - 1]) == 2 and (seg[i - 1][0] == '.' or seg[i - 1][0] == s[j - 1]):
                    dp[i][j] = True
                    continue
                if dp[i - 1][j] and len(seg[i - 1]) == 2:
                    dp[i][j] = True
                    continue
                if dp[i - 1][j - 1] and (seg[i - 1][0] == '.' or seg[i - 1][0] == s[j - 1]):
                    dp[i][j] = True
                    continue
        return dp[-1][-1]
