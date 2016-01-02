class Solution:
    """
    @param A, B: Two strings.
    @return: The length of longest common subsequence of A and B.
    """
    def longestCommonSubsequence(self, A, B):
        # write your code here
        m, n = len(A), len(B)
        if m == 0 or n == 0:
            return 0
        
        maxlen = [[0 for j in range(n)] for i in range(m)]
        
        for j in range(n):
            if A[0] == B[j]:
                maxlen[0][j] = 1
        
        for i in range(m):
            if A[i] == B[0]:
                maxlen[i][0] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                diag = maxlen[i - 1][j - 1] 
                diag = diag + 1 if A[i] == B[j] else diag
                maxlen[i][j] = max(diag, maxlen[i - 1][j], maxlen[i][j - 1])
        
        return maxlen[m - 1][n - 1]
