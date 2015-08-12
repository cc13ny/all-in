import java.util.Hashtable;

public class Solution {
    public int[] twoSum(int[] nums, int target) {
        Hashtable<Integer, Integer> dict = new Hashtable<Integer, Integer>();
        int[] res = new int[2];
        for(int i = 0; i < nums.length; i++){
            if(dict.containsKey(target - nums[i])){
                res[0] = dict.get(target - nums[i]) + 1;
                res[1] = i + 1;
                return res;
            }
            dict.put(nums[i], i);
        }
        
        return res;
    }
}
