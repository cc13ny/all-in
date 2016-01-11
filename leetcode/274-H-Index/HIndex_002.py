class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        res = 0
        n = len(citations)
        l, r = 0, n - 1
        while l <= r:
            m = l + (r - l) / 2
            if citations[m] >=  n - m:
                r = m - 1
            else:
                l = m + 1
        return n - l
