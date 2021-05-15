# brute force, optimized later
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        maxv = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    area = self.getArea(i, j, matrix)
                    if area > maxv:
                        maxv = area
        return maxv

    def getArea(self, i, j, matrix):
        m, n = len(matrix), len(matrix[0])
        length, flag = 1, False
        for l in range(1, min(m - i, n - j)):
            # print 'len: ' + str(l)
            for k in range(j, j + l + 1):
                # print i + 1, k
                if matrix[i + l][k] == '0':
                    flag = True
                    break
            for k in range(i, i + l + 1):
                # print k, j + 1
                if matrix[k][j + l] == '0':
                    flag = True
                    break
            if flag:
                break
            length += 1

        # print i, j, length * length
        return length * length
