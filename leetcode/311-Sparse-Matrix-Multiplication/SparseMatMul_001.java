public class Solution {
    public int[][] multiply(int[][] A, int[][] B) {
        int nrows = A.length, ncols = B[0].length, nmed = A[0].length;
        int[][] C = new int[nrows][ncols];

        ArrayList<ArrayList<Integer>> a = new ArrayList<ArrayList<Integer>>();
        ArrayList<ArrayList<Integer>> b = new ArrayList<ArrayList<Integer>>();
        ArrayList<Integer> tmp;

        for (int i = 0; i < nrows; i++) {
            tmp = new ArrayList<Integer>();
            for (int j = 0; j < nmed; j++) {
                if (A[i][j] != 0) {
                    tmp.add(j);
                }
            }
            a.add(tmp);
        }

        for (int j = 0; j < ncols; j++) {
            tmp = new ArrayList<Integer>();
            for (int i = 0; i < nmed; i++) {
                if (B[i][j] != 0) {
                    tmp.add(i);
                }
            }
            b.add(tmp);
        }

        for (int i = 0; i < nrows; i++) {
            for (int j = 0; j < ncols; j++) {
                int asize = a.get(i).size(), bsize = b.get(j).size();
                tmp = (asize < bsize) ? a.get(i) : b.get(j);
                int size = (asize < bsize) ? asize : bsize;
                for (int k = 0; k < size; k++) {
                    C[i][j] += A[i][tmp.get(k)] * B[tmp.get(k)][j];
                }
            }
        }

        return C;
    }
}
