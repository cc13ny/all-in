class Solution:
    # @param {integer} n
    # @return {integer}
    def numTrees(self, n):
        a = [1] + [0] * n
        for i in range(1, n + 1):
            for j in range(i):
                a[i] += a[j] * a[i - 1 - j]

        return a[n]
