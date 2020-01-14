public class Solution {
    /**
     * @param A: A list of lists of integers
     * @return: An integer
     */
    public int jump(int[] A) {
        // write your code here
        int n = A.length;
        if (n == 1) {
            return 0;
        }

        int start = 1;
        int end = A[0];
        int i = 0;
        while (start <= end) {
            i += 1;
            if (end >= n - 1) {
                return i;
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

        return 0;
    }
}