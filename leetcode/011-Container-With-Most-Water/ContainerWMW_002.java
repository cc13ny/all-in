public class Solution {
    public int maxArea(int[] height) {
        int size = height.length;
        int i = 0, j = size - 1;
        int res = 0, tmp = 0, h = 0;

        while (i < j) {
            tmp = Math.min(height[i], height[j]) * (j - i);
            if (tmp > res) {
                res = tmp;
            }
            if (height[i] < height[j]) {
                h = height[i];
                while (i < size && height[i] <= h) {
                    i++;
                }
            } else {
                h = height[j];
                while (-1 < j && height[j] <= h) {
                    j--;
                }
            }
        }

        return res;
    }
}
