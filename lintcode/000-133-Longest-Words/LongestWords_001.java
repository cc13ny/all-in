class Solution {
    /**
     * @param dictionary: an array of strings
     * @return: an arraylist of strings
     */
    ArrayList<String> longestWords(String[] dictionary) {
        // write your code here
        ArrayList<String> longestWords = new ArrayList<String>();
        int maxlen = 0;
        for (String word : dictionary) {
            if (word.length() > maxlen) {
                maxlen = word.length();
                longestWords = new ArrayList<String>();
                longestWords.add(word);
            } else if (word.length() == maxlen) {
                longestWords.add(word);
            }
        }
        
        return longestWords;
    }
};