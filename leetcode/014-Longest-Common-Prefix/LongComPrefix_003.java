public class Solution {
    public String longestCommonPrefix(String[] strs) {
        int size = strs.length;
        int minlen = Integer.MAX_VALUE;

        if (size == 0) {
            return "";
        }

        for (int i = 0; i < size; i++) {
            if (strs[i].length() < minlen) {
                minlen = strs[i].length();
            }
        }

        int i, j;
        for (j = 0; j < minlen; j++) {
            for (i = 1; i < size; i++) {
                if (strs[i].charAt(j) != strs[i - 1].charAt(j)) {
                    break;
                }
            }
            if (i < size) {
                break;
            }
        }

        return strs[0].substring(0, j);
    }
}
