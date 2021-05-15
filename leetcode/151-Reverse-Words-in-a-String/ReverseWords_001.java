public class Solution {
    public String reverseWords(String s) {
        String[] strs = s.trim().split("\\s+");
        String newStr;

        if (strs.length > 0) {
            newStr = strs[strs.length - 1];
            for (int i = strs.length - 2; i > -1; i--) {
                newStr = newStr + " " + strs[i];
            }
        } else {
            newStr = "";
        }
        return newStr;

    }
}
