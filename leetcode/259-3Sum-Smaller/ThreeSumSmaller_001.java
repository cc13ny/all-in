public class Solution {
    public int threeSumSmaller(int[] nums, int target) {
        Arrays.sort(nums);
        int size = nums.length, res = 0;
        for (int i = 0; i < size - 2; i++) {
            int newtarget = target - nums[i];
            int j = i + 1, k = size - 1;
            while (j < k) {
                int twosum = nums[j] + nums[k];
                if (twosum < newtarget) {
                    res += k - j;
                    j++;
                } else {
                    k--;
                }
            }
        }

        return res;
    }
}
