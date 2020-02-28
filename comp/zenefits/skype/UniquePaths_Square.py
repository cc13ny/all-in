def uniquePaths(n):
    grid = [[1 for j in range(n)] for i in range(n)]

    for i in range(1, n):
        for j in range(1, n):
            grid[i][j] = grid[i][j - 1] + grid[i - 1][j]
    return grid

grid = uniquePaths(10)

for row in grid:
    print row
