import java.util.ArrayList;
import java.util.Hashtable;
import java.util.Arrays;

public class Solution {
    public List<String> letterCombinations(String digits) {

        Hashtable<String, String> dic = buildDict();

        int len = digits.length();

        if (len == 0) {
            ArrayList<String> emptyone = new ArrayList<String>();
            emptyone.add(digits);
            return (List<String>) emptyone;
        }

        if (len == 1) {
            ArrayList<String> ends = new ArrayList<String>();
            String[] letts = dic.get(digits).split("");
            int leng = letts.length;

            for (int k = 0; k < leng; k++) {
                ends.add(letts[k]);
            }
            return (List<String>) ends;
        }

        char head = digits.charAt(0);
        String h = String.valueOf(head);
        String letters = dic.get(h);
        int size = letters.length();

        String poststr = digits.substring(1);
        ArrayList<String> ls = (ArrayList<String>) letterCombinations(poststr);
        int num = ls.size();
        List<String> newls = new ArrayList<String>();

        for (int i = 0; i < size; i++) {
            char letter = letters.charAt(i);
            String l = String.valueOf(letter);


            for (int j = 0; j < num; j++) {
                newls.add(l + ls.get(j));

            }

        }

        return newls;
    }

    public Hashtable<String, String> buildDict() {
        Hashtable<String, String> dic = new Hashtable<String, String>();
        dic.put("2", "abc");
        dic.put("3", "def");
        dic.put("4", "ghi");
        dic.put("5", "jkl");
        dic.put("6", "mno");
        dic.put("7", "pqrs");
        dic.put("8", "tuv");
        dic.put("9", "wxyz");
        return dic;
    }
}
