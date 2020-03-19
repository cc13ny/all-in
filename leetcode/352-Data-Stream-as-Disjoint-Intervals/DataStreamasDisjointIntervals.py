# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.intervals = []
        

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        intv = self.intervals
        l, r = 0, len(self.intervals) - 1
        
        while l <= r:
            m = l + (r - l) / 2
            if val < intv[m].start:
                r = m - 1
            elif val <= intv[m].end:
                break
            else:
                l = m + 1
        
        if l > r:
            if 0 < l < len(intv) and intv[l - 1].end + 1 == val and intv[l].start - 1 == val:
                intv[l - 1].end = intv[l].end
                intv.pop(l)
            elif l < len(intv) and intv[l].start - 1 == val:
                intv[l].start = val
            elif 0 < l and intv[l - 1].end + 1 == val:
                intv[l - 1].end = val
            else:
                intv.insert(l, Interval(val, val))
            

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        return self.intervals
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
