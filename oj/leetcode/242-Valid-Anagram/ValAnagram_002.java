public class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (map.containsKey(c)) {
                map.put(c, map.get(c) + 1);
            } else {
                map.put(c, 1);
            }
        }
        
        for (int j = 0; j < t.length(); j++) {
            char c = t.charAt(j);
            int idx = Character.getNumericValue(c);
            if (map.containsKey(c)) {
                if (map.get(c) < 1)
                    return false;
                map.put(c, map.get(c) - 1);
            } else {
                return false;
            }
        }
        
        return true;
    }
}
