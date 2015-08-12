import java.util.HashMap;


public class Solution {
	public int lengthOfLongestSubstring(String s) {
        HashMap<String, Integer> map = new HashMap<String, Integer>();
        int res = 0;
        int i = 0;
        for(int j = 0; j < s.length(); j++){
            String sub = s.substring(j, j + 1);
            if(map.containsKey(sub)) {
                if(j - i > res) res = j - i;
                int r = map.get(sub);
                for(int k = i; k <= r; k++) {
                	map.remove(s.substring(k, k + 1));
                }
                i = r + 1;
            }
            
            map.put(sub, j);
            
            if(j == s.length() - 1 && j - i + 1 > res) {
                res = j - i + 1;
            }
        }
        
        return res;
    }
}
