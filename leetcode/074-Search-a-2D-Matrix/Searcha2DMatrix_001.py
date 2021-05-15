class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        m, n = len(matrix), len(matrix[0])

        l, r = 0, m * n - 1
        while l <= r:
            mid = (l + r) / 2
            i, j = mid / n, mid % n
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                l += 1
            else:
                r -= 1

        return False
