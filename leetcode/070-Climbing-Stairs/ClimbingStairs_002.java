public class Solution {
    public int climbStairs(int n) {
        int pre = 1, cur = 1;

        for (int i = 0; i < n - 1; i++) {
            cur += pre;
            pre = cur - pre;
        }
        return cur;
    }
}
