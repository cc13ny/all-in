class ValidWordAbbr(object):

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        wordset = set()
        abbr2cnt = {}
        for word in dictionary:
            if len(word) > 2:
                abbr = word[0] + str(len(word) - 2) + word[-1]
            else:
                abbr = word
            if word not in wordset:
                abbr2cnt[abbr] = abbr2cnt.get(abbr, 0) + 1
            wordset.add(word)
        self.wordset = wordset
        self.abbr2cnt = abbr2cnt

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def word2abbr(w):
            if len(w) > 2:
                abbr = w[0] + str(len(w)-2) + w[-1]
            else:
                abbr = w
            return abbr
        cnt  = self.abbr2cnt.get(word2abbr(word), 0)
        unique = (cnt == 0) or (word in self.wordset and cnt == 1)
        
        return unique

# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
