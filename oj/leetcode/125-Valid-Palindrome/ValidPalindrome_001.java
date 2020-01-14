public class Solution {
    public boolean isPalindrome(String s) {
        int i = 0, j = s.length() - 1;
        
        while (i < j) {
            char chari = s.charAt(i);
            char charj = s.charAt(j);
            
            if (Character.isLetterOrDigit(chari)) {
                if (Character.isLetterOrDigit(charj)) {
                    char chi = Character.toLowerCase(chari);
                    char chj = Character.toLowerCase(charj);
                    if (chi != chj) {
                        return false;
                    } else {
                        i++;
                        j--;
                    }
                } else {
                    j--;
                }
            } else {
                i++;
            }
        }
        
        return true;
    }
}
