class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res = 0
        nrows, ncols = len(grid), len(grid[0])
        
        start_l, start_r = 0, nrows-1
        for i in range(ncols-1, -1, -1):
            l, r = start_l, start_r
            while l <= r:
                m = l + int((r-l)/2)
                if grid[m][i] >= 0:
                    l = m + 1
                else:
                    r = m - 1
            res += nrows - l
            start_l = l
        return res
