# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @return {Interval[]}

    def sortmeg(self, intervals):
        ls = []
        for i in intervals:
            ls.append(i.start)
        idx = sorted(range(len(ls)), key=lambda x: ls[x])

        sortedintv = []
        for i in idx:
            sortedintv.append(intervals[i])

        return sortedintv

    def merge(self, intervals):
        if len(intervals) < 2:
            return intervals

        intervals = self.sortmeg(intervals)
        p = 0
        while p + 1 <= len(intervals) - 1:
            if intervals[p + 1].start <= intervals[p].end:
                if intervals[p + 1].end > intervals[p].end:
                    intervals[p].end = intervals[p + 1].end
                del intervals[p + 1]
            else:
                p += 1
        return intervals
