/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        int l = 1, r = n;
        while (l <= r) {
            // key point: avoid overflow which causes strange behavior of m
            int m = l + (r - l) / 2; 
            if (isBadVersion(m)) {
                r = m - 1;
            } else {
                l = m + 1;
            }
        }
        
        return l;
    }
}
