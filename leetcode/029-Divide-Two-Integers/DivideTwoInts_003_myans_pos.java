public class Solution {
    public int divide(int dividend, int divisor) {
        if (dividend == Integer.MIN_VALUE && divisor == -1) {
            return Integer.MAX_VALUE;
        }

        boolean isdiff = (dividend > 0 && divisor < 0) ||
                (dividend < 0 && divisor > 0);
        long a = Math.abs((long) dividend);
        long b = Math.abs((long) divisor);

        int i = -1;
        while (a >= b) {
            b = b << 1;
            i++;
        }

        int one = 1;
        if (i > -1) {
            one = one << i;
            b = b >> 1;
        }

        int res = 0;
        for (; i > -1; i--) {
            if (a >= b) {
                res += one;
                a -= b;
            }

            one = one >> 1;
            b = b >> 1;
        }
        return isdiff ? -res : res;
    }
}