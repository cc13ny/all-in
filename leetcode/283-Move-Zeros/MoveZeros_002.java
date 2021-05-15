public class Solution {
    public void moveZeroes(int[] nums) {
        int j = -1;

        for (int i = 0; i < nums.length; i++) {
            if (j < 0 && nums[i] == 0) {
                j = i;
            }

            if (j >= 0 && nums[i] != 0) {
                nums[j] = nums[i];
                nums[i] = 0;
                j++;
            }
        }
    }
}
