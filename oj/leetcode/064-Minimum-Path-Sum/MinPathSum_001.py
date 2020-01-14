class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        M = [[0 for x in range(n)] for x in range(m)] 
        
        M[0][0] = grid[0][0]
        
        for i in range(1, m):
            M[i][0] = grid[i][0] + M[i-1][0]
        
        for j in range(1, n):
            M[0][j] = grid[0][j] + M[0][j-1]
        
        for i in range(1,m):
            for j in range(1,n):
                M[i][j] = grid[i][j] + min(M[i-1][j], M[i][j-1])
        
        return M[m-1][n-1]
