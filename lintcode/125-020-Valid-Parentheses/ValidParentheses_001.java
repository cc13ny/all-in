public class Solution {
    /**
     * @param s A string
     * @return whether the string is a valid parentheses
     */
    public boolean isValidParentheses(String s) {
        // Write your code here
        Stack<String> stack = new Stack<String>();
        HashMap<String, String> map = new HashMap<String, String>();
        map.put(")", "(");
        map.put("]", "[");
        map.put("}", "{");
        
        for (int i = 0; i < s.length(); i++) {
            String symbol = s.substring(i, i + 1);
            if (!symbol.equals("(") && !symbol.equals("[") && !symbol.equals("{")) {
                if (stack.empty()) {
                    return false;
                }
                String last = stack.pop();
                if (!map.get(symbol).equals(last)) {
                    return false;
                }
            } else {
                stack.push(symbol);
            }
        }
        if (!stack.empty()) {
            return false;
        }
        return true;
    }
}