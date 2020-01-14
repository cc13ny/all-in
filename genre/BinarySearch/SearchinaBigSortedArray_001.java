public class Solution {
    /**
     * @param A: An integer array
     * @param target: An integer
     * @return : An integer which is the index of the target number
     */
    public int searchBigSortedArray(int[] A, int target) {
        // write your code here
        int l = 0;
        int r = 0;
        int m;
        
        while (r < A.length && A[r] < target) {
            r = 2 * r + 1;
        }
        r = Math.min(r, A.length - 1);
        
        while (l <= r) {
            m = (l + r) / 2;
            if (A[m] < target) {
                l = m + 1;
            } else {
                r = m - 1;
            }
        }
        
        if (l < A.length && A[l] == target) {
            return l;
        }
        
        return -1;
    }
}