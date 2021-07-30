'''
Leetcode
'''
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals or len(intervals) == 0 or len(intervals[0]) == 0:
            return 0

        intervals.sort()

        end_times = [intervals[0][1]]

        # print(intervals)
        res = 1
        for i in range(1, len(intervals)):
            interval = intervals[i]
            start_time, end_time = interval[0], interval[1]
            l, r = 0, len(end_times) - 1
            while l <= r:
                m = l + (r-l)//2
                if end_times[m] > start_time:
                    r = m - 1
                else:
                    l = m + 1

            res = max(res, len(end_times) - r)

            l, r = 0, len(end_times) - 1
            while l <= r:
                m = l + (r-l)//2
                if end_times[m] >= end_time:
                    r = m - 1
                else:
                    l = m + 1
            # print(end_times)
            end_times.insert(l, end_time)

        # print("--")
        # print(end_times)
        return res

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

"""
Lintcode
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        # Write your code here
        if not intervals or len(intervals) == 0 or intervals[0] == None:
            return 0

        intervals.sort(key=lambda interval: [interval.start, interval.end])

        end_times = [intervals[0].end]

        # print(intervals)
        res = 1
        for i in range(1, len(intervals)):
            interval = intervals[i]
            start_time, end_time = interval.start, interval.end
            l, r = 0, len(end_times) - 1
            while l <= r:
                m = l + (r-l)//2
                if end_times[m] > start_time:
                    r = m - 1
                else:
                    l = m + 1

            res = max(res, len(end_times) - r)

            l, r = 0, len(end_times) - 1
            while l <= r:
                m = l + (r-l)//2
                if end_times[m] >= end_time:
                    r = m - 1
                else:
                    l = m + 1
            # print(end_times)
            end_times.insert(l, end_time)

        # print("--")
        # print(end_times)
        return res



