class Solution:
    # @param {integer} n
    # @return {integer[][]}
    def generateMatrix(self, n):
        if n < 1:
            return []
        res = [[0 for _ in range(n)] for _ in range(n)]
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        num = 1
        while left < right and top < bottom:
            for j in range(left, right + 1):
                res[top][j] = num
                num += 1
            for i in range(top + 1, bottom):
                res[i][right] = num
                num += 1
            for j in range(right, left - 1, -1):
                res[bottom][j] = num
                num += 1
            for i in range(bottom - 1, top, -1):
                res[i][left] = num
                num += 1
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        if top == bottom:
            for j in range(left, right + 1):
                res[top][j] = num
        elif left == right:
            for i in range(top, bottom + 1):
                res[i][left] = num
        
        return res
