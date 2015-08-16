# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b


class UnionFind:
    def __init__(self, n, m):
        self.fathers = {}
        self.nsets = 0
        self.grid = [[0 for _ in range(m)] for _ in range(n)]
        self.n = n
        self.m = m

    def build_island(self, i, j):
        self.grid[i][j] = 1
        self.fathers[i * self.m + j] = i * self.m + j
        self.nsets += 1
        nbrs = []
        nbrs.append([i, j - 1])
        nbrs.append([i, j + 1])
        nbrs.append([i - 1, j])
        nbrs.append([i + 1, j])
        for nbr in nbrs:
            if -1 < nbr[0] < self.n and -1 < nbr[1] < self.m:
                if self.grid[nbr[0]][nbr[1]] == 1:
                    idx1 = i * self.m + j
                    idx2 = nbr[0] * self.m + nbr[1]
                    self.union(idx1, idx2)

    def find(self, idx):
        return self.compressed_find(idx)

    def compressed_find(self, idx):
        fidx = self.fathers[idx]
        if fidx != idx:
            self.fathers[idx] = self.find(fidx)
        return self.fathers[idx]

    def union(self, i, j):
        fi = self.find(i)
        fj = self.find(j)
        if fi != fj:
            self.fathers[fi] = fj
            self.nsets -= 1

    def get_nsets(self):
        return self.nsets


class Solution:
    # @param {int} n an integer
    # @param {int} m an integer
    # @param {Pint[]} operators an array of point
    # @return {int[]} an integer array
    def numIslands2(self, n, m, operators):
        # Write your code here
        if n == 0 or m == 0:
            return 0

        uf, res = UnionFind(n, m), []
        for oper in operators:
            i, j = oper.x, oper.y
            if -1 < i < n and -1 < j < m:
                uf.build_island(i, j)
                res.append(uf.get_nsets())
        return res
