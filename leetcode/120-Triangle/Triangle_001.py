class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer

    # Follow Up: Find the path
    def minimumTotal(self, triangle):
        m = len(triangle)
        for i in range(1, m):
            for j in range(i + 1):
                if j == 0:
                    triangle[i][0] += triangle[i - 1][0]
                elif j == i:
                    triangle[i][j] += triangle[i - 1][j - 1]
                else:
                    triangle[i][j] += min(triangle[i - 1][j - 1], triangle[i - 1][j])

        return min(triangle[m - 1])
