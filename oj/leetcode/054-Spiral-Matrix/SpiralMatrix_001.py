class Solution:
    # @param {integer[][]} matrix
    # @return {integer[]}
    def spiralOrder(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        res = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        while left < right and top < bottom:
            for j in range(left, right + 1):
                res.append(matrix[top][j])
            for i in range(top + 1, bottom):
                res.append(matrix[i][right])
            for j in range(right, left - 1, -1):
                res.append(matrix[bottom][j])
            for i in range(bottom - 1, top, -1):
                res.append(matrix[i][left])
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        if top == bottom:
            for j in range(left, right + 1):
                res.append(matrix[top][j])
        elif left == right:
            for i in range(top, bottom + 1):
                res.append(matrix[i][left])
        
        return res
