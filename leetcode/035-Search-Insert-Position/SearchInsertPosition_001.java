public class Solution {
    public int searchInsert(int[] A, int target) {
        int a = 0;
        int b = A.length - 1;
        int mid = 0;
        int loc = 0;
        
        if(A.length == 0){
            return 0;
        }
        
        if (A.length == 1){
            if(A[0] >= target){
                return 0;
            }
            else{
                return 1;
            }
        }
        
        while(b - a != 1){
            mid = (a+b)/2;
            loc = A[mid];
            if(loc == target){
                return mid;
            }
            else if(loc < target){
                a = mid;
                
            }
            else{
                b = mid;
            }
        }
        
        if(target <= A[a]){
            return 0;
        }
        else if(target > A[b]){
            return b+1;
        }
        else{
            return a+1;
        }
    }
}
