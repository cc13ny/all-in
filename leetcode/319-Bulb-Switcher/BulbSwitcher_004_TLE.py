class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 1
        num_of_facs = [2 for i in range(n)]
        for j in range(2, int(math.sqrt(n)) + 1):
            for k in range(j, n / j + 1):
                num_of_facs[j * k - 1] += 2
            num_of_facs[j * j - 1] -= 1
            res += num_of_facs[j - 1] % 2
        for j in range(int(math.sqrt(n)) + 1, n + 1):
            res += num_of_facs[j - 1] % 2
            
        return res
