class Solution:
    """
    Calculate the total number of distinct N-Queen solutions.
    @param n: The number of queens.
    @return: The total number of distinct solutions.
    """

    def totalNQueens(self, n):
        # write your code here
        if n < 1:
            return []
        res = self.search(n, [])
        return len(res)

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
