class Solution:
    # @param {integer} n
    # @return {integer[]}
    def grayCode(self, n):
        res = [0]
        seed = 1
        for i in range(n):
            tmp = []
            for j in range(len(res) - 1, -1, -1):
                tmp.append(res[j] + seed)
            res += tmp
            seed = seed << 1
        return res
