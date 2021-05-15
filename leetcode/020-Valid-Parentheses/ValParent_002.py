public


class Solution {
public boolean isValid(String s) {
HashMap < Character, Character > pairs = new HashMap < Character, Character > ();
pairs.put('(', ')');
pairs.put('[', ']');
pairs.put('{', '}');

Stack < Character > stack = new Stack < Character > ();

for (int i = 0; i < s.length(); i++) {
char c = s.charAt(i);

if (pairs.containsKey(c)) {
stack.push(c);
} else {
if (stack.empty()) {


return false;
} else {
char
t = stack.pop();
if (pairs.get(t) != c) {
return false;
}
}
}
}

if (stack.empty()) {
return true;
}

return false;
}
}
