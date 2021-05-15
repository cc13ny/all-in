public class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashMap<Character, Integer> mark = new HashMap<Character, Integer>();
        char c;
        int i = -1;
        int res = 0, tmp = 0;

        for (int j = 0; j < s.length(); j++) {
            c = s.charAt(j);
            if (mark.containsKey(c) && mark.get(c) > i) {
                if (tmp > res) {
                    res = tmp;
                }
                tmp = j - mark.get(c);
                i = mark.get(c);

            } else {
                tmp++;
            }

            mark.put(c, j);
        }

        if (tmp > res) {
            res = tmp;
        }

        return res;
    }
}
