class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        m = len(matrix)
        n = 0 if m == 0 else len(matrix[0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    matrix[0][j] += matrix[0][j - 1]
                elif j == 0:
                    matrix[i][0] += matrix[i - 1][0]
                else:
                    matrix[i][j] += matrix[i - 1][j] + matrix[i][j - 1] - matrix[i - 1][j - 1]
        self.cs_mat = matrix

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        mat = self.cs_mat
        m, n = len(mat), len(mat[0])
        assert -1 < row1 < m and -1 < row2 < m
        assert -1 < col1 < n and -1 < col2 < n
        assert row1 <= row2
        assert col1 <= col2

        if row1 == 0 and col1 == 0:
            return mat[row2][col2]
        elif row1 == 0:
            return mat[row2][col2] - mat[row2][col1 - 1]
        elif col1 == 0:
            return mat[row2][col2] - mat[row1 - 1][col2]
        else:
            return mat[row2][col2] + mat[row1 - 1][col1 - 1] - mat[row2][col1 - 1] - mat[row1 - 1][col2]
