public class Solution {
    public int findMin(int[] num) {
        int len = num.length;
        
        if(len == 1){
            return num[0];
        }
        
        int a = 0;
        int b = len - 1;
        int mid = 0;
        boolean descent = true;
        
        if(num[a] > num[b]){
        
            while(b - a != 1){
                mid = (a+b)/2;
            
                if(num[mid] >= num[a]){
                    a = mid;
                }
                else{
                    b = mid;
                }
            }
            
            if(num[len -1] > num[b]){
                return num[b];
            }
            else{
                return num[len - 1];
            }
        }
        else{
            while(b - a != 1){
                mid = (a+b)/2;
            
                if(num[mid] <= num[a]){
                    a = mid;
                }
                else{
                    b = mid;
                }
            
            
            }
            
            return num[a];
        }
    }
}
