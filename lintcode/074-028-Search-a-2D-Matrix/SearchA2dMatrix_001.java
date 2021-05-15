public class Solution {
    /**
     * @param matrix, a list of lists of integers
     * @param target, an integer
     * @return a boolean, indicate whether matrix contains target
     */
    public boolean searchMatrix(int[][] matrix, int target) {
        // write your code here
        if (matrix.length == 0 || matrix[0].length == 0) {
            return false;
        }

        int nrows = matrix.length;
        int ncols = matrix[0].length;
        int l = 0;
        int r = nrows * ncols - 1;
        int m;
        int i;
        int j;

        while (l <= r) {
            m = (l + r) / 2;
            i = m / ncols;
            j = m % ncols;
            if (matrix[i][j] == target) {
                return true;
            } else if (matrix[i][j] < target) {
                l = m + 1;
            } else {
                r = m - 1;
            }
        }

        return false;
    }
}