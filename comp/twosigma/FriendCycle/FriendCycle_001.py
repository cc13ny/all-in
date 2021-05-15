class UnionFind:
    def __init__(self, n):
        self.fathers = range(n)
        self.nsets = n

    def find(self, idx):
        return self.compressed_find(idx)

    def compressed_find(self, idx):
        fidx = self.fathers[idx]
        if fidx != idx:
            self.fathers[idx] = self.compressed_find(fidx)
        return self.fathers[idx]

    def union(self, i, j):
        fi = self.find(i)
        fj = self.find(j)
        if fi != fj:
            self.fathers[fi] = fj
            self.nsets -= 1

    def getnsets(self):
        return self.nsets


def findCircle(grid):
    # Assume that grid is like this
    #
    # ['ynyy', 'nyyn', 'yyyn', 'ynny']

    if len(grid) == 0 or len(grid[0]) == 0:
        return 0

    n = len(grid)
    uf = UnionFind(n)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if grid[i][j] == 'Y':
                uf.union(i, j)

    return uf.getnsets()


grid = ['ynn', 'nyy', 'nyy']
grid = ['YYNN', 'YYYN', 'NYYN', 'NNNY']
grid = ['YNNNN', 'NYNNN', 'NNYNN', 'NNNYN', 'NNNNY']

print
findCircle(grid)
