import java.util.ArrayList;

public class Solution {
    public String convertToTitle(int n) {
        ArrayList<String> ls = new ArrayList<String>();
        String s = "";
        
        ls.add("Z");
        ls.add("A");
        ls.add("B");
        ls.add("C");
        ls.add("D");
        ls.add("E");
        ls.add("F");
        ls.add("G");
        ls.add("H");
        ls.add("I");
        ls.add("J");
        ls.add("K");
        ls.add("L");
        ls.add("M");
        ls.add("N");
        ls.add("O");
        ls.add("P");
        ls.add("Q");
        ls.add("R");
        ls.add("S");
        ls.add("T");
        ls.add("U");
        ls.add("V");
        ls.add("W");
        ls.add("X");
        ls.add("Y");
        
        while(n > 0){
            int reminder = n%26;
 
            s = ls.get(reminder) + s;
            if(reminder == 0){
                reminder = 26;
            }
        
            n = (n - reminder)/26;
        }
        
        return s;
        
    }
}
