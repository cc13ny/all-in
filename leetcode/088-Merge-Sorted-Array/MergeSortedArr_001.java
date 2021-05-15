public class Solution {
    public void merge(int A[], int m, int B[], int n) {
        int size = A.length;
        int j = 0;
        int k = 0;
        int p = 0;


        for (int i = m - 1; i > -1; i--) {
            A[i + size - m] = A[i];

        }

        while ((j < m) && (k < n)) {
            if (A[j + size - m] < B[k]) {
                A[p] = A[j + size - m];
                j++;

            } else {
                A[p] = B[k];
                k++;
            }
            p++;
        }


        while (k < n) {
            A[p] = B[k];
            p++;
            k++;
        }
    }
}
