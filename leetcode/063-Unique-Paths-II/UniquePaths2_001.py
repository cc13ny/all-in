class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        grid = [[1 for j in range(n)] for i in range(m)]
        grid[0][0] = 0 if obstacleGrid[0][0] == 1 else 1

        for i in range(1, m):
            grid[i][0] = 0 if obstacleGrid[i][0] == 1 else grid[i - 1][0]

        for j in range(1, n):
            grid[0][j] = 0 if obstacleGrid[0][j] == 1 else grid[0][j - 1]

        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = 0 if obstacleGrid[i][j] == 1 else grid[i][j - 1] + grid[i - 1][j]

        return grid[m - 1][n - 1]
