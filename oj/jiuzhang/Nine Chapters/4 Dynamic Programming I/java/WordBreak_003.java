// To fix: cand & newcand [from Set -> ArrayList]

public class Solution {
    /**
     * @param s: A string s
     * @param dict: A dictionary of words dict
     */
    public boolean wordBreak(String s, Set<String> dict) {
        // write your code here   
        // write your code here   
        if (s.equals("") && dict.isEmpty()) {
            return true;
        }

        HashMap<Integer, Set<String>> lendict = new HashMap<Integer, Set<String>>();
        ArrayList<Integer> lenlist = new ArrayList<Integer>();

        for (String word : dict) {
            int l = word.length();
            if (lendict.containsKey(l)) {
                lendict.get(l).add(word);
            } else {
                HashSet<String> tmp = new HashSet<String>();
	        	tmp.add(word);
	        	lendict.put(l, tmp);
                lenlist.add(l);
            }
        }

        Collections.sort(lenlist);
        HashSet<Integer> cand = new HashSet<Integer>();
        for (int l : lenlist) {
            if (l <= s.length()) {
                String substr = s.substring(0, l);
                if (lendict.get(l).contains(substr)) {
                    if (l == s.length()) {
                        return true;
                    }
                    cand.add(l - 1);
                }
            } else {
                break;
            }
        }
        
        boolean[] isVisited = new boolean[s.length()];
    
        while (! cand.isEmpty()) {
            HashSet<Integer> newcand = new HashSet<Integer>();
            
            for (int c : cand) {
                for (int l : lenlist) {
                    int idx = c + l;
                    if (idx > s.length() - 1) {
                        break;
                    } else {
                        String word = s.substring(c + 1, idx + 1);
                        if ((! isVisited[idx]) && (lendict.get(l).contains(word))) {
                            newcand.add(idx);
                            isVisited[idx] = true;
                            if (idx == s.length() - 1) {
                                return true;
                            }
                        }
                        
                    }
                }
            }
            cand = newcand;
        }

        return false;
    }
}
