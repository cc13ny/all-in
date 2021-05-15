class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res = 0
        if not grid or not grid[0]:
            return 0
        nrow_kills = [[0 for _ in grid[0]] for _ in grid]

        # for row
        for i in range(len(grid)):
            cnt = 0
            idx_afw = 0
            for j in range(len(grid[0])):
                cnt += int(grid[i][j] == 'E')
                if grid[i][j] == 'W':
                    for k in range(idx_afw, j):
                        if grid[i][k] != 'E':
                            nrow_kills[i][k] = cnt
                    idx_afw = j + 1
                    cnt = 0
            for k in range(idx_afw, len(grid[0])):
                if grid[i][k] != 'E':
                    nrow_kills[i][k] = cnt

        # for col and calcuate res
        for j in range(len(grid[0])):
            cnt = 0
            idx_afw = 0
            for i in range(len(grid)):
                cnt += int(grid[i][j] == 'E')
                if grid[i][j] == 'W':
                    for k in range(idx_afw, i):
                        if grid[k][j] != 'E':
                            res = max(res, nrow_kills[k][j] + cnt)
                    idx_afw = i + 1
                    cnt = 0
            for k in range(idx_afw, len(grid)):
                if grid[k][j] != 'E':
                    res = max(res, nrow_kills[k][j] + cnt)
        return res
