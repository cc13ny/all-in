# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @param {Interval} newInterval
    # @return {Interval[]}
    def insert(self, intervals, newInterval):
        if intervals == []:
            intervals.append(newInterval)
            return intervals
        l = 0
        r = len(intervals) - 1
        a = newInterval.start
        b = newInterval.end

        while l <= r:
            m = (l + r)/2
        #print l, r
        #print m
            tmp = intervals[m]
            if tmp.start <= a <= tmp.end:
                ln = tmp.start
                ll = m
            #print 'a'
                break
            elif 0 <= m-1 and intervals[m - 1].end < a < tmp.start:
                ln = a
                ll = m
            #print 'b'
                break
            elif m == 0 and a < tmp.start:
                ln = a
                ll = 0
            #print 'c'
                break
            elif a < tmp.end: #whatever
                r = m - 1
            #print 'd'
            elif m == len(intervals) - 1:
                ll = m + 1
            #print 'e'
                break
            else:
                l = m + 1
            #print 'f'

        if ll == len(intervals):
            intervals.append(newInterval)
            return intervals

        l = 0
        r = len(intervals) - 1
        while l <= r:
            m = (l + r)/2
            tmp = intervals[m]
            if tmp.start <= b <= tmp.end:
                rn = tmp.end
                rr = m
                break
            elif m+1 <=  len(intervals) - 1 and tmp.end < b < intervals[m+1].start:
                rn = b
                rr = m
                break
            elif m == len(intervals) - 1 and tmp.end < b:
                rn = b
                rr = m
                break
            elif tmp.start < b: #whatever
                l = m + 1
            elif m == 0:
                rr = -1
                break
            else:
                r = m - 1

        if rr == -1:
            intervals.insert(0, newInterval)
            return intervals

        insertInterval = Interval(ln, rn)

        intervals.insert(ll, insertInterval)
        del intervals[ll+1:rr+2]
    
        return intervals
