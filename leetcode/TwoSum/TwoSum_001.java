import java.util.Hashtable;

public class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int len = numbers.length;
        int[] anArray;
        boolean flag = false;
        Integer pre;
        Integer next;

        // allocates memory for 2 integers
        anArray = new int[2];
        
        Hashtable <Integer, Integer> nums = new Hashtable <Integer, Integer>();
        
        for(int i = 0; i < len; i++){
            if(nums.get(numbers[i]) == null){
                nums.put(numbers[i], i);
            }
            else if (2 * numbers[i] == target){
                flag = true;
                anArray[0] = nums.get(numbers[i]) + 1;
                anArray[1] = i + 1;
            }
        }
        
        if(!flag){
            for(int j = 0; j < len; j++){
              next = nums.get(target - numbers[j]);
              if((next != null)&&(j!= next)){
                  anArray[0] = j + 1;
                  anArray[1] = next + 1;
                  break;
              }
            }
        }
        
        return anArray;
    }
}
