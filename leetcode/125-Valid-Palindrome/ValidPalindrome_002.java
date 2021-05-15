public class Solution {
    public boolean isPalindrome(String s) {
        int i = 0, j = s.length() - 1;

        while (i < j) {
            char chari = s.charAt(i);
            char charj = s.charAt(j);

            while (!Character.isLetterOrDigit(chari)) {
                i++;
                if (i < j) {
                    chari = s.charAt(i);
                } else {
                    break;
                }
            }

            while (!Character.isLetterOrDigit(charj)) {
                j--;
                if (i < j) {
                    charj = s.charAt(j);
                } else {
                    break;
                }
            }

            if (i < j) {
                char chi = Character.toLowerCase(chari);
                char chj = Character.toLowerCase(charj);
                if (chi != chj) {
                    return false;
                } else {
                    i++;
                    j--;
                }
            } else {
                break;
            }
        }

        return true;
    }
}
