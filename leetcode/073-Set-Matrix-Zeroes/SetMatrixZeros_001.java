import java.util.Arrays;

public class Solution {
    public void setZeroes(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        int[] flags = new int[n];
        boolean flag = false;
        Arrays.fill(flags, 1);


        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == 0) {
                    flags[j] = 0;
                    flag = true;
                }

            }

            if (flag) {
                for (int k = 0; k < n; k++) {
                    matrix[i][k] = 0;
                }

                flag = false;
            }
        }

        for (int q = 0; q < n; q++) {
            if (flags[q] == 0) {
                for (int p = 0; p < m; p++) {
                    matrix[p][q] = 0;
                }
            }
        }
    }
}
