/*
 * AC in lintcode; TLE in leetcode
 */

public class Solution {
    /**
     * @param A: A list of lists of integers
     * @return: An integer
     */
    public int jump(int[] A) {
        // write your code here
        int n = A.length;
        int[] minnums = new int[n];
        minnums[n - 1] = 1;

        ArrayList<Integer> trueloc = new ArrayList<Integer>();

        int nearestrue = n - 1;
        trueloc.add(nearestrue);
        for (int i = n - 2; -1 < i; i--) {
            int upbound = Math.min(i + A[i], n - 1);
            if (nearestrue <= upbound) {
                trueloc.add(0, nearestrue);
                int minval = minnums[nearestrue];

                for (int j = 1; j < trueloc.size(); j++) {
                    int next = trueloc.get(j);
                    if (next > i + A[i]) {
                        break;
                    } else if (minnums[next] < minval) {
                        minval = minnums[next];
                    }
                }
                minnums[i] = minval + 1;
                nearestrue = i;
            }
        }
        return minnums[0] - 1;
    }
}