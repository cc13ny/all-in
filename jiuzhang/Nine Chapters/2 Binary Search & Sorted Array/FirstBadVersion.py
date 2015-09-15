# class VersionControl:
#    @classmethod
#    def isBadVersion(cls, id)
#        # Run unit tests to check whether verison `id` is a bad version
#        # return true if unit tests passed else false.
# You can use VersionControl.isBadVersion(10) to check whether version 10 is a 
# bad version.


class Solution:
    """
    @param n: An integers.
    @return: An integer which is the first bad version.
    """
    def findFirstBadVersion(self, n):
        # write your code here
        vc = VersionControl()
        l, r = 0, n - 1
        while l <= r:
            m = (l + r) / 2
            if vc.isBadVersion(m):
                r = m - 1
            else:
                l = m + 1
        return l
