// Backward
// O(n)

public class Solution {
    /**
     * @param A: A list of integers
     * @return: The boolean answer
     */
    public boolean canJump(int[] A) {
        // wirte your code here
        int n = A.length;

        boolean[] flags = new boolean[n];
        flags[n - 1] = true;

        int nearestrue = n - 1;
        for (int i = n - 2; i > -1; i--) {
            if (nearestrue <= Math.min(i + A[i], n - 1)) {
                flags[i] = true;
                nearestrue = i;
            }
        }
        return flags[0];
    }
}