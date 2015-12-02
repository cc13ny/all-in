# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
#     target = 3
#     return version >= target

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n # l, r = 0, n - 1 also works
        while l <= r:
            m = (l + r) / 2
            if isBadVersion(m):
                r = m - 1
            else:
                l = m + 1
        return l
