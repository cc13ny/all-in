class Solution:
    # @param n: an integer
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, n):
        # write your code here
        dp = [False] * 3

        cur = 0
        for i in xrange(n):
            dp[-1] = not (dp[0] and dp[1])
            dp[cur] = dp[-1]
            cur = (cur + 1) % 2
        
        return dp[-1]
