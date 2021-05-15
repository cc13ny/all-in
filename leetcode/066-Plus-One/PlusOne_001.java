public class Solution {
    public int[] plusOne(int[] digits) {
        int len = digits.length;
        int cin = 1;

        for (int i = len - 1; i > -1; i--) {
            digits[i] = digits[i] + cin;
            if (digits[i] > 9) {
                digits[i] -= 10;
                cin = 1;
            } else {
                cin = 0;
            }
        }

        if (cin == 0) {
            return digits;
        } else {
            int[] newDigits = new int[len + 1];
            newDigits[0] = cin;
            for (int j = 1; j < len + 1; j++) {
                newDigits[j] = digits[j - 1];
            }
            return newDigits;
        }
    }
}
