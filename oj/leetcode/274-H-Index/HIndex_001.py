class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        citations = [0] + citations
        res = 0
        n = len(citations)
        for i in xrange(n - 1):
            idx = n - 1 - i
            if citations[idx] < i + 1:
                break
            elif citations[idx - 1] <= i + 1:
                res = i + 1
        return res
