class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(1, 10):
            tmp = self.comb(i, k, n)
            res += tmp
        return res

    def comb(self, init, k, n):
        lbound, ubound = (k - 1) * (init + 1) + init, (k - 1) * 9 + init
        if n < lbound or ubound < n:
            return []
        if k == 1:
            return [[n]]
        res = []
        for j in range(init + 1, 10):
            tmp = self.comb(j, k - 1, n - init)
            for t in tmp:
                res.append([init] + t)
        return res
