public class Solution {
    /**
     * @param triangle: a list of lists of integers.
     * @return: An integer, minimum path sum.
     */
    public int minimumTotal(ArrayList<ArrayList<Integer>> triangle) {
        // write your code here
        ArrayList<Integer> prelvl = triangle.get(0);
        for (int i = 1; i < triangle.size(); i++) {
            ArrayList<Integer> lvl = triangle.get(i);
            for (int j = 0; j < lvl.size(); j++) {
                int minsum = 0;
                if (j == 0) {
                    minsum = prelvl.get(j);
                } else if (j == lvl.size() - 1) {
                    minsum = prelvl.get(j - 1);
                } else {
                    minsum = Math.min(prelvl.get(j - 1), prelvl.get(j));
                }
                lvl.set(j, lvl.get(j) + minsum);
            }
            prelvl = lvl;
        }

        int endlen = triangle.size();
        ArrayList<Integer> lastlvl = triangle.get(endlen - 1);
        int res = lastlvl.get(0);
        for (int k = 1; k < endlen; k++) {
            if (lastlvl.get(k) < res) {
                res = lastlvl.get(k);
            }
        }

        return res;
    }
}
