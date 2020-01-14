class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dp = [False] * 4
        cur = 0
        for i in xrange(n):
            dp[-1] = (not dp[0]) or (not dp[1]) or (not dp[2])
            dp[cur] = dp[-1]
            cur = (cur + 1) % 3
        
        return dp[-1]
