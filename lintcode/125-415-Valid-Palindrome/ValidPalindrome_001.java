public class Solution {
    /**
     * @param s A string
     * @return Whether the string is a valid palindrome
     */
    public boolean isPalindrome(String s) {
        // Write your code here
        if (s == null) {
            return true;
        }
        int p = 0;
        int q = s.length() - 1;
        char left;
        char right;

        while (p < q) {
            while (p < s.length() && !Character.isLetterOrDigit(s.charAt(p))) {
                p++;
            }
            while (-1 < q && !Character.isLetterOrDigit(s.charAt(q))) {
                q--;
            }
            if (p < q) {
                left = Character.toLowerCase(s.charAt(p));
                right = Character.toLowerCase(s.charAt(q));
                if (left != right) {
                    return false;
                }
                p++;
                q--;
            }
        }

        return true;
    }
}