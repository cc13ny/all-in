/**
 * Definition of Interval:
 * public classs Interval {
 *     int start, end;
 *     Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 */

class Solution {
    /**
     * Insert newInterval into intervals.
     * @param intervals: Sorted interval list.
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
        
        
        for (int i = 0; i < intervals.size(); i++) {
            if (i < startid && start <= intervals.get(i).end) {
                startid = i;
                head = Math.min(start, intervals.get(i).start);
            }
            
            if (intervals.get(i).start <= end) {
                endid = i;
                tail = Math.max(end, intervals.get(i).end);
            } else {
                break;
            }
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