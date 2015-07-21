public class Solution {
    public int search(int[] A, int target) {
        int i;
        int valuereturned = -1;
        for(i = 0; i < A.length; i++){
            if(target == A[i]){
                valuereturned = i;
                break;
            }
        }

        return valuereturned;
    }
}
