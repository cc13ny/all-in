/* *
 * Given an array of integers, every element appears twice except for one. Find that single one.
 *
 * Note:
 *      Your algorithm should have a linear runtime complexity.
 *      Could you implement it without using extra memory?
 */

/* *
 * I can't figure out the solution without using the extra memory. This problem can be solved with hash map.
 *
 * The code below is modified from --
 *          http://www.programcreek.com/2012/12/leetcode-solution-of-single-number-in-java
 */

public class SingleNumber {
    public static void main(String[] args) {

    }

    public static int singleNumber(int[] A) {
        int single_num = 0;

        for (int num : A) {
            single_num = single_num ^ num;
        }

        return single_num;
    }
}
