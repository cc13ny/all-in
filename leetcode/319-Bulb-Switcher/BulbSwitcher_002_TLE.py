class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        num_of_facs = [0 for i in range(n)]
        for j in range(1, n + 1):
            for k in range(1, n / j + 1):
                num_of_facs[j * k - 1] += 1
            res += num_of_facs[j - 1] % 2
        return res
