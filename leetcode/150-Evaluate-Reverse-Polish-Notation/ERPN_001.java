/*
 * @author: cchen
 */
public class Solution {
    public int evalRPN(String[] tokens) {
        ArrayList<String> wordlist = new ArrayList<String>(Arrays.asList(tokens));
        int loc = 0;
        int leftoperand;
        int rightoperand;
        int operandafter = 0;
        String symbol;

        if (wordlist.size() == 1) operandafter = Integer.parseInt(wordlist.get(loc));
        while (wordlist.size() != 1) {
            symbol = wordlist.get(loc);
            switch (symbol) {
                case "+":
                    leftoperand = Integer.parseInt(wordlist.get(loc - 2));
                    rightoperand = Integer.parseInt(wordlist.get(loc - 1));
                    operandafter = leftoperand + rightoperand;
                    wordlist.remove(loc - 2);
                    wordlist.remove(loc - 2);
                    wordlist.set(loc - 2, Integer.toString(operandafter));
                    loc--;
                    break;
                case "-":
                    leftoperand = Integer.parseInt(wordlist.get(loc - 2));
                    rightoperand = Integer.parseInt(wordlist.get(loc - 1));
                    operandafter = leftoperand - rightoperand;
                    wordlist.remove(loc - 2);
                    wordlist.remove(loc - 2);
                    wordlist.set(loc - 2, Integer.toString(operandafter));
                    loc--;
                    break;
                case "*":
                    leftoperand = Integer.parseInt(wordlist.get(loc - 2));
                    rightoperand = Integer.parseInt(wordlist.get(loc - 1));
                    operandafter = leftoperand * rightoperand;
                    wordlist.remove(loc - 2);
                    wordlist.remove(loc - 2);
                    wordlist.set(loc - 2, Integer.toString(operandafter));
                    loc--;
                    break;
                case "/":
                    leftoperand = Integer.parseInt(wordlist.get(loc - 2));
                    rightoperand = Integer.parseInt(wordlist.get(loc - 1));
                    operandafter = leftoperand / rightoperand;
                    wordlist.remove(loc - 2);
                    wordlist.remove(loc - 2);
                    wordlist.set(loc - 2, Integer.toString(operandafter));
                    loc--;
                    break;
                default:
                    loc++;
                    break;
            }
        }
        return operandafter;
    }
}
