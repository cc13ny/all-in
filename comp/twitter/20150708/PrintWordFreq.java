import java.util.ArrayList;
import java.util.HashMap;
import java.util.Set;

public class PrintWordFreq {

    public static void main(String[] args) {
        // for testing
        ArrayList<String> tests = new ArrayList<String>();
        tests.add(" I want to count the frequency of the words in the   input");

        for (String test : tests)
            wordFreq(test);
    }

    public static void wordFreq(String sentence) {
        String[] words = sentence.trim().split("\\s+");
        HashMap<String, Integer> wordfreq = new HashMap<String, Integer>();
        ArrayList<String> wordlist = new ArrayList<String>();

        // Calculate word frequency
        for (String word : words) {
            if (wordfreq.containsKey(word)) {
                wordfreq.put(word, wordfreq.get(word) + 1);
            } else {
                wordfreq.put(word, 1);
                wordlist.add(word);
            }
        }

        // Find the maxlen : len(word) + len(freq)
        int maxlen = 0;
        Set<String> wordset = wordfreq.keySet();
        for (String word : wordset) {
            int wordlen = word.length();
            int freqlen = Integer.toString(wordfreq.get(word)).length();
            if ((wordlen + freqlen) > maxlen)
                maxlen = wordlen + freqlen;
        }

        // Print the format
        int linelen = maxlen + 10;
        for (String word : wordlist) {
            int freq = wordfreq.get(word);
            int wordlen = word.length();
            int freqlen = Integer.toString(freq).length();
            int ndots = linelen - wordlen - freqlen;

            String dots = "";
            for (int i = 0; i < ndots; i++)
                dots += ".";
            System.out.println(word + dots + freq);
        }
    }
}
