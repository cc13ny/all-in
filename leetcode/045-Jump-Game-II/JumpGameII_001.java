public class Solution {
    public int jump(int[] nums) {
        int n = nums.length;
        if (n == 1) {
            return 0;
        }

        int start = 1;
        int end = nums[0];
        int i = 0;
        while (start <= end) {
            i += 1;
            if (end >= n - 1) {
                return i;
            }

            int maxval = 0;
            for (int j = start; j <= end; j++) {
                if (j + nums[j] > maxval) {
                    maxval = j + nums[j];
                }
            }
            start = end + 1;
            end = maxval;
        }

        return 0;
    }
}
