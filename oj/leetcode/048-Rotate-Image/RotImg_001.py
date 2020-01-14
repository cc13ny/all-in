class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        num = len(matrix)
        if num % 2 == 1:
            m = num/2
            n = m + 1
        else:
            m = num/2
            n = m

        for j in range(n):
            for i in range(m):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[num - 1 - j][i]
                matrix[num - 1 - j][i] = matrix[num - 1 - i][num - 1 - j]
                matrix[num - 1 - i][num - 1 - j] = matrix[j][num - 1 - i]
                matrix[j][num - 1 - i] = tmp
