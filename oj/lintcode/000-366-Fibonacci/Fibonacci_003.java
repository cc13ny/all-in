class Solution {
    /**
     * @param n: an integer
     * @return an integer f(n)
     */
    public int fibonacci(int n) {
        // write your code here
        if (n == 1 || n == 2) {
            return n - 1;
        }
        
        // record the last two items each for calculation of the next items
        int a = 0, b = 1, tmp = 0;
        while (n > 2) {
            tmp = a + b;
            a = b;
            b = tmp;
            n -= 1;
        }
        
        return b;
    }
}