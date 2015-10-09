class Solution {
    /**
     * @param nums: The integer array.
     * @param target: Target to find.
     * @return: The first position of target. Position starts from 0.
     */
    public int binarySearch(int[] nums, int target) {
        //write your code here
        int l = 0;
        int r = nums.length - 1;
        int m;
        
        while (l <= r) {
            m = (l + r) / 2;
            if (nums[m] < target) {
                l = m + 1;
                
            } else {
                r = m - 1;
            }
        }
        if (nums[l] != target) {
            return -1;
        }
        
        return l;
    }
}
