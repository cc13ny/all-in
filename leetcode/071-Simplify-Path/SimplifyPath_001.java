public class Solution {
    public String simplifyPath(String path) {

        StringBuilder result = new StringBuilder();

        if (path == null || path.length() == 0) {
            return result.toString();
        }

        String[] strs = path.split("/");

        Stack<String> stack = new Stack<String>();

        for (String s : strs) {

            if (s.length() == 0 || s.equals(".")) {

            } else if (s.equals("..")) {
                if (!stack.isEmpty()) {
                    stack.pop();
                }
            } else {
                stack.push(s);
            }

        }

        if (stack.isEmpty()) {
            result.append('/');

        } else {

            while (!stack.isEmpty()) {
                result.insert(0, stack.pop());
                result.insert(0, '/');
            }
        }

        return result.toString();
    }
}
