public class Solution {
    public int findPeakElement(int[] num) {

        int size = num.length;
        int idx = size - 1;

        for (int i = 0; i < size; i++) {
            if ((i > 0) && (num[i] < num[i - 1])) {
                idx = i - 1;
                return idx;
            }
        }

        return idx;
    }
}
