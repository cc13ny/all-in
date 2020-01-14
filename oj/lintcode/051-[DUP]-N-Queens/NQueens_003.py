# The idea is the same as the answer: http://www.jiuzhang.com/solutions/n-queens/
# Just BRUTE FORCE, in fact, it's my first idea I had never tried until I take a look at the answer
# What I learned from this problem is that SET operation is not necessarily fast!!!!

class Solution:
    """
    Get all distinct N-Queen solutions
    @param n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        # write your code here
        if n < 1:
            return []
        res = self.search(n, [])
        return self.draw(n, res)

    def isValid(self, cols, row):
        m = len(cols)
        for i in range(m):
            if abs(row - cols[i]) == m - i:
                return False
            if row == cols[i]:
                return False
        return True

    def search(self, n, cols):
        if len(cols) == n:
            return [cols[:]]

        res = []
        for i in range(n):
            if not self.isValid(cols, i):
                continue
            cols.append(i)
            tmp = self.search(n, cols)
            res.extend(tmp)
            cols.pop()
        return res

    def draw(self, n, res):
        pics = []
        for cols in res:
            pic = []
            for col in cols:
                pic.append('.' * col + 'Q' + '.' * (n - col - 1))
            pics.append(pic)
        return pics
