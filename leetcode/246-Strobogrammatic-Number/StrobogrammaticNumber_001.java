public class Solution {
    public boolean isStrobogrammatic(String num) {
        int size = num.length();
        if (size % 2 == 1) {
            String mid = num.substring(size / 2, size / 2 + 1);
            if (!mid.equals("0") && !mid.equals("1") && !mid.equals("8")) {
                return false;
            }
        }

        HashMap<String, String> pairs = new HashMap<String, String>();
        pairs.put("0", "0");
        pairs.put("1", "1");
        pairs.put("8", "8");
        pairs.put("6", "9");
        pairs.put("9", "6");

        for (int i = 0; i < (size + 1) / 2; i++) {
            String a = num.substring(i, i + 1);
            String b = num.substring(size - i - 1, size - i);
            if (!a.equals(pairs.get(b))) {
                return false;
            }
        }
        return true;
    }
}
