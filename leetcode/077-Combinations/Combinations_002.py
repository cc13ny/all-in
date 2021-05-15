class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n < 1:
            return []

        if k == 1:
            return [[i] for i in range(1, n + 1)]

        res = self.combine(n - 1, k)
        tmp = self.combine(n - 1, k - 1)
        for t in tmp:
            res.append(t + [n])
        return res
