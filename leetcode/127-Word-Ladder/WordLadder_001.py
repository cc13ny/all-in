class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        if beginWord == endWord:
            return 1

        cnt = 1
        q = [beginWord]

        while q:
            nq = []
            for word in q:
                for i in range(len(beginWord)):
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        if j != word[i]:
                            nword = word[:i] + j + word[i + 1:]
                            if nword == endWord:
                                return cnt + 1
                            if nword in wordList:
                                nq.append(nword)
                                wordList.remove(nword)
            cnt += 1
            q = nq
        return 0
