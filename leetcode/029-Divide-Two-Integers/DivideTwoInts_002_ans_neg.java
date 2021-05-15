public class Solution {
    public int divide(int dividend, int divisor) {
        if (dividend == Integer.MIN_VALUE && divisor == -1) {
            return Integer.MAX_VALUE;
        }

        if (dividend == Integer.MIN_VALUE && divisor == 1) {
            return Integer.MIN_VALUE;
        }

        boolean isdiff = (dividend > 0 && divisor < 0) ||
                (dividend < 0 && divisor > 0);
        long a = -Math.abs((long) dividend);
        long b = -Math.abs((long) divisor);

        int res = 0;
        while (a <= b) {
            int shift = 0;
            while (a <= (b << shift)) {
                shift++;
            }

            a -= b << (shift - 1);
            res += 1 << (shift - 1);
        }
        return isdiff ? -res : res;
    }
}