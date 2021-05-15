public class Solution {
    public int lengthOfLastWord(String s) {
        int res = 0;
        for (int i = s.length() - 1; i > -1; i--) {
            if (res == 0) {
                if (s.charAt(i) != ' ') {
                    res++;
                }
            } else {
                if (s.charAt(i) != ' ') {
                    System.out.println(i);
                    res++;
                } else {
                    return res;
                }
            }
        }

        return res;
    }
}
