public class Solution {
    public boolean wordPattern(String pattern, String str) {
        String[] words = str.split("\\s+");
        if(pattern.length() != words.length) {
            return false;
        }
        
        HashMap<Character, String> p2s = new HashMap<Character, String>();
        HashMap<String, Character> s2p = new HashMap<String, Character>();
        
        for (int i = 0; i < words.length; i++) {
            char p = pattern.charAt(i);
            if (!p2s.containsKey(p)) {
                if (s2p.containsKey(words[i])) {
                    return false;
                }
                p2s.put(p, words[i]);
                s2p.put(words[i], p);
            } else if (!p2s.get(p).equals(words[i])){
                return false;
            }
        }
        
        return true;
    }
}
