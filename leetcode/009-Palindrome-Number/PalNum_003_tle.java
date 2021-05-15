public class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }

        int left = 10;
        while (left <= x) {
            left *= 10;
        }
        left /= 10;

        while (x != 0) {
            int ldigit = x / left;
            int rdigit = x % 10;
            if (ldigit != rdigit) {
                return false;
            }
            x = (x % left) / 10;
            left /= 100;
        }

        return true;
    }
}
