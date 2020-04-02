class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set([n])
        while n != 1:
            new_n = 0
            while n > 0:
                new_n += (n % 10) ** 2
                n = int(n/10)
            if new_n in visited:
                return False
            visited.add(new_n)
            n = new_n
        return True
