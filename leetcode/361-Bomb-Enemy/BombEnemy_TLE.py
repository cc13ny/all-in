class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        nkills = [[[0, 0] for _ in grid[0]] for _ in grid]

        # for row
        for i in range(len(grid)):
            cnt = 0
            idx_afw = 0
            for j in range(len(grid[0])):
                cnt += int(grid[i][j] == 'E')
                if grid[i][j] == 'W':
                    for k in range(idx_afw, j):
                        if grid[i][k] != 'E':
                            nkills[i][k][1] = cnt
                    idx_afw = j + 1
                    cnt = 0
            for k in range(idx_afw, len(grid[0])):
                if grid[i][k] != 'E':
                    nkills[i][k][1] = cnt

        # for col
        for j in range(len(grid[0])):
            cnt = 0
            idx_afw = 0
            for i in range(len(grid)):
                cnt += int(grid[i][j] == 'E')
                if grid[i][j] == 'W':
                    for k in range(idx_afw, i):
                        if grid[k][j] != 'E':
                            nkills[k][j][0] = cnt
                    idx_afw = i + 1
                    cnt = 0
            for k in range(idx_afw, len(grid)):
                if grid[k][j] != 'E':
                    nkills[k][j][0] = cnt
        res = 0
        for i in range(len(nkills)):
            for j in range(len(nkills[0])):
                nk = nkills[i][j]
                res = max(res, nk[0] + nk[1])
        return res
