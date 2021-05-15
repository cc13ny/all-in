# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return -1

        candidates = range(n)
        while candidates != []:
            i = candidates.pop(0)
            tmp = []
            for j in candidates:
                if knows(i, j):
                    tmp.append(j)
            if tmp == []:
                for k in range(n):
                    if k != i and (knows(i, k) or not knows(k, i)):
                        return -1
                return i

            candidates = tmp
        return -1
