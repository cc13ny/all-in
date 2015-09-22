// Forward
// O(n)

public class Solution {
    /**
     * @param A: A list of integers
     * @return: The boolean answer
     */
    public boolean canJump(int[] A) {
        // wirte your code here
        int n = A.length;
        if (n == 1) {
            return true;
        }

        int start = 1;
        int end = A[0];
        while (start <= end) {
            if (end >= n - 1) {
                return true;
            }

            int maxval = 0;
            for (int j = start; j <= end; j++) {
                if (j + A[j] > maxval) {
                    maxval = j + A[j];
                }
            }
            start = end + 1;
            end = maxval;
        }

        return false;
    }
}