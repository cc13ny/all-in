import java.util.ArrayList;

public class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> ls = new ArrayList<List<Integer>>();
        List<Integer> prerow = new ArrayList<Integer>();

        for (int i = 0; i < numRows; i++) {
            ArrayList<Integer> row = new ArrayList<Integer>();
            if (ls.isEmpty()) {
                row.add(1);
            } else {
                row.add(1);
                row.add(1);

                for (int j = 1; j < i; j++) {
                    int num = prerow.get(j - 1) + prerow.get(j);
                    row.add(j, num);
                }
            }

            prerow = row;
            ls.add(row);
        }

        return ls;
    }
}
