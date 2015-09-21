class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}

    def uniquePaths(self, m, n):
        grid = [[1] * n] * m
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = grid[i][j - 1] + grid[i - 1][j]
            
        return grid[m - 1][n - 1]
