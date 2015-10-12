def findPath(grid, money):
    grid[0][0] = money
    n = len(grid)
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            if i == 0:
                grid[i][j] = grid[i][j - 1] - grid[i][j]
            elif j == 0:
                grid[i][j] = grid[i - 1][j] - grid[i][j]
            else:
                grid[i][j] = max(grid[i][j - 1], grid[i - 1][j]) - grid[i][j]
    #if grid[m - 1][n - 1] < 0:
    #    return -1
    return grid

grid = [[0, 1, 0], [3, 2, 8], [1, 0, 4]]
res = findPath(grid, 5)

for row in res:
    print row
            
                
