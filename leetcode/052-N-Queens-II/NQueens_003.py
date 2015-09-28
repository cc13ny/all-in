class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
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
