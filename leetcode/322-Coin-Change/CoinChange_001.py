class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort()
        dp = [amount + 1 for i in range(amount + 1)]
        dp[0] = 0
        for i in xrange(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i - c] + 1, dp[i])
                else:
                    break

        return -1 if dp[-1] == amount + 1 else dp[-1]
