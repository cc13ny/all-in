import java.util.Hashtable;

public class Solution {
    public int majorityElement(int[] num) {
        int len = num.length;
        Hashtable<Integer, Integer> tb = new Hashtable<Integer, Integer>();
        int max = 0;

        for (int i = 0; i < len; i++) {
            int digit = num[i];

            if (!tb.containsKey(digit)) {
                tb.put(digit, 1);
            } else {

                int val = tb.get(digit) + 1;
                tb.put(digit, val);
            }
        }

        int target = 0;

        for (Integer key : tb.keySet()) {
            int tmp = tb.get(key);
            if (tmp > max) {
                max = tmp;
                target = key;
            }
        }

        return target;

    }
}
