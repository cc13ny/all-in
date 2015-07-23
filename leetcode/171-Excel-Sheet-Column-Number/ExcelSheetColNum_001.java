import java.util.Hashtable;

public class Solution {
    public int titleToNumber(String s) {
        int num = 0;
        
        Hashtable<String, Integer> tb = new Hashtable<String, Integer>();
        
        tb.put("A", 1);
        tb.put("B", 2);
        tb.put("C", 3);
        tb.put("D", 4);
        tb.put("E", 5);
        tb.put("F", 6);
        tb.put("G", 7);
        tb.put("H", 8);
        tb.put("I", 9);
        tb.put("J", 10);
        tb.put("K", 11);
        tb.put("L", 12);
        tb.put("M", 13);
        tb.put("N", 14);
        tb.put("O", 15);
        tb.put("P", 16);
        tb.put("Q", 17);
        tb.put("R", 18);
        tb.put("S", 19);
        tb.put("T", 20);
        tb.put("U", 21);
        tb.put("V", 22);
        tb.put("W", 23);
        tb.put("X", 24);
        tb.put("Y", 25);
        tb.put("Z", 26);
        
        int len = s.length();
        int power = 1;
        
        for(int i = 0; i < len; i++){
            String sym = String.valueOf(s.charAt(len - 1 - i));
            int amount = tb.get(sym) * power;
            num += amount;
            power *= 26;
        }
        
        return num;
        
    }
}
