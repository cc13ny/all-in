class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        m, n = len(image), len(image[0])
        visited = [[False for j in range(n)] for i in range(m)]
        region = [y, x, y, x]
        [l, u, r, b] = self.bfs(image, x, y, visited, region)
        return (b - u + 1) * (r - l + 1)
    
    def bfs(self, image, i, j, visited, region):
        m, n = len(image), len(image[0])
        if i < 0 or i >= m:
            return region
        if j < 0 or j >= n:
            return region
        if visited[i][j]:
            return region
        if image[i][j] == '0':
            return region
        print i, j
        
        [l, u, r, b] = region
        region = [min(l, j), min(u, i), max(r, j), max(b, i)]
        visited[i][j] = True
        di = [-1, 1,  0, 0]
        dj = [ 0, 0, -1, 1]
        for idx in range(4):
            region = self.bfs(image, i + di[idx], j + dj[idx], visited, region)
        
        return region
