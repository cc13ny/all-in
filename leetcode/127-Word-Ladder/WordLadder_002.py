# Link: http://www.cnblogs.com/zuoyuan/p/3765858.html

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        wordList.add(endWord)
        q = []
        q.append((beginWord, 1))
        while q:
            curr = q.pop(0)
            currword = curr[0];
            currlen = curr[1]
            if currword == endWord: return currlen
            for i in range(len(beginWord)):
                part1 = currword[:i];
                part2 = currword[i + 1:]
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    if currword[i] != j:
                        nextword = part1 + j + part2
                        if nextword in wordList:
                            q.append((nextword, currlen + 1));
                            wordList.remove(nextword)
        return 0
