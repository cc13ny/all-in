public class Solution {
    public int shortestDistance(String[] words, String word1, String word2) {
        String pre = null;
        int preidx = 0;
        int res = words.length;
        
        for (int i = 0; i < words.length; i++) {
            String word = words[i];
            if (word.equals(word1) || word.equals(word2)) {
                if (pre != null && !pre.equals(word) && i - preidx < res) {
                    res = i - preidx;
                }
                
                pre = word;
                preidx = i;
            }
        }
        return res;
    }
}
