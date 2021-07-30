'''
DFS, Recursive, set grid[i][j] as 0 instead of using visited
'''

class SolutionRecursive1:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        res = 0
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                res = max(res, self.dfs(grid, i, j, m, n))
        return res

    def dfs(self, board, i, j, m, n):
        if not (0 <= i < m and 0 <= j < n) or board[i][j] != 1:
            return 0

        board[i][j] = 0

        res = 1
        for y, x in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            res += self.dfs(board, i+y, j+x, m, n)

        return res


'''
DFS, Iterative, note that you should set grid[i][j] when you put into stack instead when poping it out.
'''

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(board, i, j, m, n):
            board[i][j] = 0

            res = 0
            stack = [(i, j)]
            diff = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            while stack:
                res += 1
                y, x = stack.pop()

                for d1, d2 in diff:
                    if (0 <= y+d1 < m and 0 <= x+d2 < n) and board[y+d1][x+d2] == 1:
                        board[y+d1][x+d2] = 0
                        stack.append((y+d1, x+d2))

            return res

        if len(grid) == 0 or len(grid[0]) == 0:
            return 0

        res = 0
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(res, dfs(grid, i, j, m, n))

        return res


'''
BFS, Iterative, note that you should set grid[i][j] when you put into stack instead when poping it out.
'''

from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def bfs(board, i, j, m, n):
            board[i][j] = 0

            res = 0
            dq = deque([(i, j)])
            diff = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            while dq:
                res += 1
                y, x = dq.popleft()

                for d1, d2 in diff:
                    if (0 <= y+d1 < m and 0 <= x+d2 < n) and board[y+d1][x+d2] == 1:
                        board[y+d1][x+d2] = 0
                        dq.append((y+d1, x+d2))

            return res

        if len(grid) == 0 or len(grid[0]) == 0:
            return 0

        res = 0
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(res, bfs(grid, i, j, m, n))

        return res

