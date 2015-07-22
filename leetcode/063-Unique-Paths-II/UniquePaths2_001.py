class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        if obstacleGrid[0][0] == 1:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        if m == 1 and n == 1:
            return 1
        M = [[0 for x in range(n)] for x in range(m)] 
        
        flag1 = False
        for i in range(1, m):
            if flag1:
                M[i][0] = 0
            else:
                M[i][0] = 1
                if obstacleGrid[i][0] == 1:
                    M[i][0] = 0
                    flag1 = True
        
        flag2 = False
        for i in range(1, n):
            if flag2:
                M[0][i] = 0
            else:
                M[0][i] = 1
                if obstacleGrid[0][i] == 1:
                    M[0][i] = 0
                    flag2 = True
        
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] != 1:
                    M[i][j] = M[i - 1][j] + M[i][j-1]
                
        return M[m-1][n-1]
