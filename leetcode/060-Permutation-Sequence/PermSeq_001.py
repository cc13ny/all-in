class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
        ls = range(1, n + 1)
        prod = 1

        for i in ls:
            prod *= i

        res = ''
        while n > 0:
            prod = prod / n
            idx = (k - 1) / prod

            num = ls.pop(idx)
            res += str(num)
            k -= prod * idx
            n -= 1
        return res
