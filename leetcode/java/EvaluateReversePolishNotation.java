/* Problem:
 *
 * Evaluate the value of an arithmetic expression in Reverse Polish Notation.
 * Valid operators are +, -, *, /. Each operand may be an integer or another expression.
 * Some examples:
 *  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
 *  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
 */
 
 
/* @author = Chi Chen
 * @email = chenchiapply@gmail.com
 * @version = 1.0
 * @runtime = 512ms
 */
public class Solution {
    public int evalRPN(String[] tokens) {
        ArrayList<String> wordlist = new ArrayList<String>(Arrays.asList(tokens));
        int loc = 0;
        int leftoperand;
        int rightoperand;
        int operandafter = 0;
        String symbol;

        if(wordlist.size()==1) operandafter = Integer.parseInt(wordlist.get(loc));
        while(wordlist.size()!=1){
            symbol = wordlist.get(loc);
            switch(symbol){
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
