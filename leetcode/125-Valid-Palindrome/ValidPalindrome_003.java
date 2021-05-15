public class Solution {
    public boolean isPalindrome(String s) {
        String str = s.replaceAll("[^A-Za-z0-9]", "").toLowerCase();
        System.out.println(str);

        int i = 0, j = str.length() - 1;

        while (i < j) {
            char chi = str.charAt(i), chj = str.charAt(j);

            if (chi != chj)
                return false;
            i++;
            j--;
        }

        return true;
    }
}
