public class Solution {
    public int singleNumber(int[] A) {
        int single_num = 0;
        for(int num : A){
            single_num = single_num ^ num;
        }
        return single_num;
    }
}
