class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        num_of_facs = [1 for i in range(n)]
        for j in range(2, n + 1):
            for k in range(1, n / j + 1):
                num_of_facs[j * k - 1] += 1

        res = 0
        for num in num_of_facs:
            res += num % 2

        return res
