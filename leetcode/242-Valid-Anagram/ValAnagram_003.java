public class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        
        int[] chars = new int[128];
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            int idx = Character.getNumericValue(c);
            chars[idx] += 1;
        }
        
        for (int j = 0; j < t.length(); j++) {
            char c = t.charAt(j);
            int idx = Character.getNumericValue(c);
            if (chars[idx] == 0) {
                return false;
            }
            chars[idx] -= 1;
        }
        
        return true;
    }
}
