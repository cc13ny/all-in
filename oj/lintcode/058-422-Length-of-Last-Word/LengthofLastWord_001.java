public class Solution {
    /**
     * @param s A string
     * @return the length of last word
     */
    public int lengthOfLastWord(String s) {
        // Write your code here
        String[] words = s.trim().split("\\s+");
        if (words.length == 0)
            return 0;
        return words[words.length - 1].length();
    }
}