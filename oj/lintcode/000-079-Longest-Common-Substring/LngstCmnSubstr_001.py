class Solution:
    # @param A, B: Two string.
    # @return: the length of the longest common substring.
    def longestCommonSubstring(self, A, B):
        # write your code here
        m, n = len(A), len(B)
        dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
        mx = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    mx = max(mx, dp[i][j])
        return mx
