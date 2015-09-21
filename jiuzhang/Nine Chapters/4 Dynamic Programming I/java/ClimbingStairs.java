public class Solution {
    /**
     * @param n: An integer
     * @return: An integer
     */
    public int climbStairs(int n) {
        // write your code here
        if (n < 1) {
            return 0;
        }
        int[] stairs = new int[n + 1];
        stairs[0] = 1;
        stairs[1] = 1;

        for (int i = 2; i < n + 1; i++) {
            stairs[i] = stairs[i - 1] + stairs[i - 2];
        }
        return stairs[n];
    }
}