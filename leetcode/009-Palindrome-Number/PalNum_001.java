#author:cchen
        #This terrible code will be updated&simplified later.

public class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }

        if (x < 10) {
            return true;
        }

        int div = 10;
        int quo = x / div;

        if ((x - div * quo) == 0) {

            return false;

        }

        while (quo > 9) {
            div *= 10;
            quo = x / div;
        }

        int i = 1;

        int divl = div;
        int divr = 10;

        int l = 0;
        int r = 0;

        while (divl >= divr) {

            l = x / divl;
            r = x % divr;

            if (l != r) {
                return false;
            }

            x = (x - l * divl - r) / 10;

            divl /= 100;
        }

        return true;
    }
}
