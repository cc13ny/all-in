class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        from math import sqrt
        
        t = int(sqrt(n))
        if t * t == n:
            return 1
        
        while n % 4 == 0:
            n /= 4
        
        if n % 8 == 7:
            return 4
        
        t = int(sqrt(n / 2))
        for i in range(1, t + 1):
            j = int(sqrt(n - i * i))
            if i * i + j * j == n:
                return 2
        
        return 3
