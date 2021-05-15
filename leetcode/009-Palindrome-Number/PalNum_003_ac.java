public class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }

        int left = 1;
        int t = x;
        while (t > 9) { // accepted because of it
            left *= 10;
            t /= 10;
        }

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
