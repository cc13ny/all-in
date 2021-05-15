public class Solution {
    public int searchInsert(int[] nums, int target) {
        int l = 0, r = nums.length - 1;
        int m = 0;

        if (r < 0) {
            return 0;
        }

        while (l < r) {
            m = (l + r) / 2;
            if (nums[m] == target) {
                return m;
            } else if (nums[m] < target) {
                l = m + 1;
            } else {
                r = m - 1;
            }
        }

        if (nums[l] < target) {
            return l + 1;
        } else {
            return l;
        }
    }
}
