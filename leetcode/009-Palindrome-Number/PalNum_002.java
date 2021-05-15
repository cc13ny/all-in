public class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }

        int t = x;
        int lloc = 1, rloc = 1;

        while (t > 9) {
            t /= 10;
            rloc *= 10;
        }

        int lnum = 0, rnum = 0;
        while (lloc < rloc) {
            lnum = (x / lloc) % 10;
            rnum = (x / rloc) % 10;

            if (lnum != rnum) {
                return false;
            }

            lloc *= 10;
            rloc /= 10;
        }

        return true;
    }
}
