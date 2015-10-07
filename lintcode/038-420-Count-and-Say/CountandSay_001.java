public class Solution {
    /**
     * @param n the nth
     * @return the nth sequence
     */
    public String countAndSay(int n) {
        // Write your code here
        if (n < 1) {
            return null;
        }
        
        /*previous & current res for each round*/
        String res = "1";
        String s; // the new result which replaces the old one
        
        /*the cnts & the number to be saild*/
        int cnt;
        String num;
        
        for (int i = 1; i < n; i++) {
        	
        		/* Initialize conditions for each round*/
            s = "";
            cnt = 1;
            num = res.substring(0, 1);
            
            for (int j = 1; j < res.length(); j++) {
                if (res.substring(j, j + 1).equals(num)) {
                    cnt += 1; // just count
                } else {
                    s += cnt + num; // say!
                    
                    /*initialize conditions for the next number*/
                    cnt = 1;
                    num = res.substring(j, j + 1);
                }
            }
            res = s + cnt + num; /*the number at the last round to be counted and said*/
        }
        return res;
    }
}