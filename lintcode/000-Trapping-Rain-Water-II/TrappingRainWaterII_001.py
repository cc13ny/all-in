import heapq


class Solution:
    # @param heights: a matrix of integers
    # @return: an integer
    def trapRainWater(self, heights):
        # write your code here
        n = len(heights)
        if n < 3:
            return 0

        m = len(heights[0])
        if m < 3:
            return 0

        hp = self.heapInialize(heights)
        visited = self.visitedInialize(heights)
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        res = 0
        while len(hp) != 0:
            minval, minx, miny = heapq.heappop(hp)
            for i in range(4):
                x = minx + dx[i]
                y = miny + dy[i]
                if -1 < x < n and -1 < y < m and not visited[x][y]:
                    visited[x][y] = True
                    if heights[x][y] < minval:
                        res += minval - heights[x][y]
                        heights[x][y] = minval
                    heapq.heappush(hp, (heights[x][y], x, y))

        return res

    def heapInialize(self, heights):
        n, m = len(heights), len(heights[0])
        h = []
        for j in range(1, m - 1):
            heapq.heappush(h, (heights[0][j], 0, j))
            heapq.heappush(h, (heights[n - 1][j], n - 1, j))
        for i in range(1, n - 1):
            heapq.heappush(h, (heights[i][0], i, 0))
            heapq.heappush(h, (heights[i][m - 1], i, m - 1))
        return h

    def visitedInialize(self, heights):
        n, m = len(heights), len(heights[0])
        visited = [[False for _ in range(m)] for _ in range(n)]

        for j in range(0, m):
            visited[0][j] = True
            visited[n - 1][j] = True
        for i in range(1, n - 1):
            visited[i][0] = True
            visited[i][m - 1] = True
        return visited
