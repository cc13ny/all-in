/**
 * Definition of Interval:
 * public classs Interval {
 * int start, end;
 * Interval(int start, int end) {
 * this.start = start;
 * this.end = end;
 * }
 */

class Solution {
    /**
     * Insert newInterval into intervals.
     *
     * @param intervals:   Sorted interval list.
     * @param newInterval: A new interval.
     * @return: A new sorted interval list.
     */
    public ArrayList<Interval> insert(ArrayList<Interval> intervals, Interval newInterval) {
        // write your code here
        int start = newInterval.start;
        int end = newInterval.end;

        int head = start;
        int tail = end;

        int startid = intervals.size();
        int endid = -1;

        int l = 0, r = intervals.size() - 1;
        int m;

        while (l <= r) {
            m = (l + r) / 2;
            if (start <= intervals.get(m).end) {
                r = m - 1;
            } else {
                l = m + 1;
            }
        }

        if (l < intervals.size()) {
            startid = l;
            head = Math.min(start, intervals.get(l).start);
        }

        l = 0;
        r = intervals.size() - 1;
        while (l <= r) {
            m = (l + r) / 2;
            if (intervals.get(m).start <= end) {
                l = m + 1;
            } else {
                r = m - 1;
            }
        }
        if (-1 < r) {
            endid = r;
            tail = Math.max(end, intervals.get(r).end);
        }


        Interval tmp = new Interval(head, tail);
        if (startid <= endid) {
            intervals.subList(startid, endid + 1).clear();
            intervals.add(startid, tmp);
        } else {
            intervals.add(startid, tmp);
        }
        return intervals;
    }
}
