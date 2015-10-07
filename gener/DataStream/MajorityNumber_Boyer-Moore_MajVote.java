public class Solution {
    /**
     * @param nums: a list of integers
     * @return: find a  majority number
     */
    public int majorityNumber(ArrayList<Integer> nums) {
        // write your code
        int res = 0;
        int cnt = 0;
        for (int num : nums) {
            if (cnt == 0) {
                cnt ++;
                res = num;
            } else {
                cnt += num == res ? 1 : -1;
            }
        }
        return res;
    }
}