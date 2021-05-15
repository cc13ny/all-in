class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        m, n = len(matrix), len(matrix[0])
        l, t, r, b = 0, 0, n - 1, m - 1
        return self.searchArea(l, t, r, b, matrix, target)

    def searchArea(self, l, t, r, b, matrix, target):
        if l > r or t > b:
            return False
        if target < matrix[t][l] or target > matrix[b][r]:
            return False

        while l <= r and t <= b:
            row = (t + b) / 2
            col = (l + r) / 2
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                res1 = self.searchArea(l, t, r, row - 1, matrix, target)
                if res1: return res1
                res2 = self.searchArea(l, row, col - 1, b, matrix, target)
                return res2
            else:
                res3 = self.searchArea(l, row + 1, r, b, matrix, target)
                if res3: return res3
                res4 = self.searchArea(col + 1, t, r, row, matrix, target)
                return res4
        return False
