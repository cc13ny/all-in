/*
 * Faster than 001
 * {Leetcode : AC, Lintcode : Runtime Error}
 * Runtime Error due to limitation of Java Recursive Depth
 */


public class Solution {
    public boolean wordBreak(String s, Set<String> wordDict) {
        if (s.equals("") && wordDict.isEmpty()) {
            return true;
        }

        HashMap<Integer, Set<String>> lendict = new HashMap<Integer, Set<String>>();
        ArrayList<Integer> lenlist = new ArrayList<Integer>();

        for (String word : wordDict) {
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
        int[] ladder = new int[s.length()];

        ladder = wordladder(s, 0, lendict, lenlist, ladder);

        return ladder[s.length() - 1] == 1;
    }

    public static int[] wordladder(String w, int start, HashMap<Integer, Set<String>> tb, ArrayList<Integer> ls, int[] ladder) {
        for (int l : ls) {
            int idx = start + l - 1;
            if (idx + 1 > w.length()) {
                break;
            } else {
                int flag = ladder[idx];
                String substr = w.substring(start, idx + 1);
                if (flag == 0 && tb.get(l).contains(substr)) {
                    ladder[idx] = 1;
                    ladder = wordladder(w, idx + 1, tb, ls, ladder);
                    if (ladder[w.length() - 1] == 1) {
                        return ladder;
                    }
                }
            }
            
        }
        
        return ladder;
    }

}