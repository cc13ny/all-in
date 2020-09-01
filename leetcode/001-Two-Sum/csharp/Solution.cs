public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int> numIdx = new Dictionary<int, int>();
        for(int i = 0; i < nums.Length; i++) {
            if (numIdx.ContainsKey(target - nums[i])) {
                return new int[]{numIdx[target - nums[i]], i};
            }
            numIdx[nums[i]] = i;
        }
        return new int[]{};
    }
}