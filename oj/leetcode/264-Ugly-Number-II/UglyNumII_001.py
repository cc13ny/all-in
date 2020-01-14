class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        i2, i3, i5, res = 0, 0, 0, [1]
        for i in range(n - 1):
            m2, m3, m5 = res[i2] * 2, res[i3] * 3, res [i5] * 5
            mn = min(m2, m3, m5)
            if m2 == mn: i2 += 1
            if m3 == mn: i3 += 1
            if m5 == mn: i5 += 1
            res.append(mn)
        return res[-1]
