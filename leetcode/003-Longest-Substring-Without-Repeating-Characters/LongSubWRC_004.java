// Avoidance of using HashMap can make it a lot quicker

public class Solution {
    public int lengthOfLongestSubstring(String s) {
        int[] mark = new int[128];
        int idx = 0, tmp = 0, res = 0, left = -1;

        for (int i = 0; i < s.length(); i++) {
            idx = (int) s.charAt(i);
            if (mark[idx] > 0 && mark[idx] > left) {
                tmp = i - mark[idx] + 1;
                left = mark[idx];
            } else {
                tmp++;
            }

            mark[idx] = i + 1;

            if (tmp > res) {
                res = tmp;
            }
        }

        return res;
    }
}
