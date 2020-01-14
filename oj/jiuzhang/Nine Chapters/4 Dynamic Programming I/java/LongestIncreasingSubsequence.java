public class Solution {
    /**
     * @param nums: The integer array
     * @return: The length of LIS (longest increasing subsequence)
     */
    public int longestIncreasingSubsequence(int[] nums) {
        // write your code here
        int n = nums.length;

        int[] res = new int[n];
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[i] >= nums[j] && res[j] + 1 > res[i]) {
                    res[i] = res[j] + 1;
                }
            }
        }

        int maxlen = -1;
        for (int k = 0; k < n; k++) {
            if (res[k] > maxlen) {
                maxlen = res[k];
            }
        }

        return maxlen + 1;
    }
}