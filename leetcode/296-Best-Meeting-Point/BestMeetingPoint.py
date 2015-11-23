class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0
        rowOne = [0 for i in range(m)]
        colOne = [0 for j in range(n)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rowOne[i] += 1
                    colOne[j] += 1

        rdist, cdist = 0, 0
        rOneNum, cOneNum = 0, 0
        for i in range(m):
            if rowOne[i] > 0:
                rOneNum += rowOne[i]
                rdist += i * rowOne[i]
        for j in range(n):
            if colOne[j] > 0:
                cOneNum += colOne[j]
                cdist += j * colOne[j]
        rRiOneNum = rOneNum - rowOne[0] 
        cRiOneNum = cOneNum - colOne[0]

        for i in range(1, m):
            if rOneNum - rRiOneNum >= rRiOneNum:
                break
            rdist += (rOneNum - rRiOneNum) - rRiOneNum
            rRiOneNum -= rowOne[i]
            
        for j in range(1, n):
            if cOneNum - cRiOneNum >= cRiOneNum:
                break
            cdist += (cOneNum - cRiOneNum) - cRiOneNum
            cRiOneNum -= colOne[j]
                
        return rdist + cdist
