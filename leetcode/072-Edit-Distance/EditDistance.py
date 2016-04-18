class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n1 = len(word1) + 1
        n2 = len(word2) + 1
        
        dp = [[0 for j in xrange(n2)] for i in xrange(n1)]
        
        for j in xrange(1, n2):
            dp[0][j] = j
            
        for i in xrange(1, n1):
            dp[i][0] = i
        
        for i in xrange(1, n1):
            for j in xrange(1, n2):
                cand1 = dp[i - 1][j] + 1
                cand2 = dp[i][j - 1] + 1
                if word1[i - 1] == word2[j - 1]:
                    cand3 = dp[i - 1][j - 1] 
                else:
                    cand3 = dp[i - 1][j - 1] + 1
                dp[i][j] = min(cand1, cand2, cand3)
        
        return dp[-1][-1]
