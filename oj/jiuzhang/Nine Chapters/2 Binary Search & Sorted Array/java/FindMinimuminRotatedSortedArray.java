public class Solution {
    /**
     * @param num: a rotated sorted array
     * @return: the minimum number in the array
     */
    public int findMin(int[] num) {
        // write your code here
        int l = 0;
        int r = num.length - 1;
        int m;
        while (l <= r) {
            m = (l + r) / 2;
            if (num[m] < num[r]) {
                r = m;
            } else {
                l = m + 1;
            }
        }
        return num[r];
    }
}