class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        cnt = 0
        visited = [[False for j in range(len(grid[0]))] for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j] and grid[i][j] == '1':
                    cnt += 1
                    visited = self.dfs(i, j, grid, visited)
        return cnt
    
    def dfs(self, i, j, grid, visited):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return visited
        if visited[i][j] or grid[i][j] == '0': 
            return visited
        
        visited[i][j] = True
        di = [-1, 1,  0, 0]
        dj = [ 0, 0, -1, 1]
        
        for k in range(4):
            visited = self.dfs(i + di[k], j + dj[k], grid, visited)
        return visited
