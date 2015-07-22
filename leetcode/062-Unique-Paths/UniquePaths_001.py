class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}

    def uniquePaths(self, m, n):
        if m == 1 or n == 1:
            return 1
        M = [[0 for x in range(n)] for x in range(m)] 

        for i in range(1, m):
            M[i][0] = 1
        
        for i in range(1, n):
            M[0][i] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                M[i][j] = M[i - 1][j] + M[i][j-1]
                
        return M[m-1][n-1]
